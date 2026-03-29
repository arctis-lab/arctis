# Security policy

## Supported versions

We publish releases on [GitHub Releases](https://github.com/arctis-lab/arctis/releases). Security fixes land in the current minor line when practical; use the latest tagged release for production.

## Reporting a vulnerability

Please **do not** open a public issue for undisclosed security problems.

- Prefer **[GitHub Security Advisories](https://github.com/arctis-lab/arctis/security/advisories/new)** (private report to maintainers).
- If that is unavailable, contact the repository maintainers through a **private channel** agreed with your organization.

Include: affected version or commit, reproduction steps, and impact (confidentiality / integrity / availability).

## Operational hardening

Production-oriented guidance (auth, TLS, secrets, rate limits) lives in [`docs/security_production.md`](docs/security_production.md).

## Secret scanning

This repository uses [Gitleaks](https://github.com/gitleaks/gitleaks) in CI (`.github/workflows/gitleaks.yml`) with [`.gitleaks.toml`](.gitleaks.toml).
