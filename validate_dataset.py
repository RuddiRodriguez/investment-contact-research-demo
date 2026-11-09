from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


DATA = Path(__file__).parent / "data" / "investment-professional-contacts.csv"
REQUIRED_COLUMNS = [
    "Company name",
    "Full name",
    "Current job title",
    "Professional email address",
    "Email verification status",
    "LinkedIn profile",
    "Source URL (current role)",
    "Email source URL",
    "Profile evidence URL",
    "Evidence notes",
]
FIRMS = {
    "Dalton Investments",
    "Elliott Investment Management",
    "ValueAct Capital",
    "Oasis Management",
    "Palliser Capital",
    "Asset Value Investors (AVI)",
    "3D Investment Partners",
}
SHARED_PREFIXES = {
    "admin",
    "careers",
    "contact",
    "enquiries",
    "info",
    "investors",
    "ir",
    "legal",
    "media",
    "press",
}


def is_http_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames == REQUIRED_COLUMNS, "Unexpected CSV columns"
        rows = list(reader)

    identities: set[tuple[str, str]] = set()
    firm_counts: Counter[str] = Counter()

    for row_number, row in enumerate(rows, start=2):
        company = row["Company name"]
        name = row["Full name"]
        title = row["Current job title"]
        email = row["Professional email address"].strip()
        status = row["Email verification status"]
        linkedin = row["LinkedIn profile"].strip()
        role_source = row["Source URL (current role)"].strip()
        email_source = row["Email source URL"].strip()

        assert company in FIRMS, f"Row {row_number}: unexpected company"
        assert name and title, f"Row {row_number}: missing identity or title"
        assert is_http_url(role_source), f"Row {row_number}: invalid role source"
        assert status in {"confirmed", "verified", "inferred", "unavailable"}, (
            f"Row {row_number}: invalid status"
        )

        identity = (company, name.casefold())
        assert identity not in identities, f"Row {row_number}: duplicate person"
        identities.add(identity)
        firm_counts[company] += 1

        if email:
            assert re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email), (
                f"Row {row_number}: invalid email"
            )
            assert email.split("@", 1)[0].casefold() not in SHARED_PREFIXES, (
                f"Row {row_number}: shared inbox presented as individual email"
            )
            assert status in {"confirmed", "verified", "inferred"}, (
                f"Row {row_number}: email has unavailable status"
            )
            assert is_http_url(email_source), f"Row {row_number}: missing email evidence"
        else:
            assert status == "unavailable", f"Row {row_number}: blank email has wrong status"
            assert not email_source, f"Row {row_number}: blank email has an email source"

        if linkedin:
            assert re.match(r"https://(?:[a-z]+\.)?linkedin\.com/in/", linkedin), (
                f"Row {row_number}: LinkedIn URL is not a personal profile"
            )

    assert set(firm_counts) == FIRMS, "One or more requested firms are missing"
    print(f"Validated {len(rows)} people across {len(firm_counts)} firms.")
    print(f"Published individual emails: {sum(bool(row['Professional email address']) for row in rows)}")
    print(f"Matched LinkedIn profiles: {sum(bool(row['LinkedIn profile']) for row in rows)}")


if __name__ == "__main__":
    main()

