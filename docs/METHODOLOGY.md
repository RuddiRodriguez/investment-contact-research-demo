# Methodology

## Input contract

Each research run starts with:

- named firms;
- included seniority and investment roles;
- excluded functions;
- requested output fields;
- an evidence standard for roles, emails and profile links;
- an as-of date.

For this example, qualifying roles included founders, chief executives, chief investment officers, investment partners, portfolio managers, heads of investment or research, and senior investment directors. Investor relations, legal, compliance, operations, HR and administrative roles were excluded.

## Source order

Sources were reviewed in this order:

1. official firm team and biography pages;
2. current regulatory adviser filings;
3. current portfolio-company or issuer biographies;
4. SEC exhibits, shareholder agreements and campaign notices;
5. firm-authored policies, presentations and letters;
6. personal LinkedIn profiles matched by employer and role.

Contact databases and email-pattern sites were not accepted as proof. Shared inboxes did not become individual addresses.

## Separate evidence fields

The dataset keeps three evidence questions separate:

- `Source URL (current role)` supports the person's present title;
- `Email source URL` shows where the individual address was published;
- `Profile evidence URL` supports the LinkedIn match.

This prevents a current role page from making an old address look current, or an email pattern from looking like a published address.

## Status rules

### Confirmed

Use only when a public source explicitly ties an individual work address to the named person. The source may be old, so the notes must state the date or limitation. Confirmed does not mean delivery tested.

### Verified

Reserve for a separate, documented mailbox-verification step. No address in this example was tested or labelled verified.

### Inferred

Reserve for a proposed address derived from an observed firm pattern. This example contains no inferred addresses.

### Unavailable

Use when no acceptable individual address was found. Leave the email cell blank.

## Quality checks

The final review checks:

- all seven requested firms are represented;
- required identity and role fields are present;
- every email is syntactically valid and has its own source;
- no shared inbox is presented as a personal address;
- LinkedIn links point to individual profiles;
- the same person is not duplicated within a firm;
- summary counts reconcile to the detail rows;
- exported source links remain clickable.

## Completion boundary

This example establishes a documented public-source dataset as of the review date. It does not prove current mailbox delivery, complete staff coverage, permission to send outreach, or future accuracy after firms change their teams or websites.

