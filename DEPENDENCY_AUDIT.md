# Dependency Audit — Wolfgang Rush MCPB Family

**Audit date:** 2026-06-01
**Auditor:** Publisher (Wolfgang Rush)
**Scope:** All 14 MCPB Desktop Extensions in this family.

This file is the family-level dependency-currency attestation referenced by each plugin's `SECURITY.md` ("Dependencies" section) for Anthropic Software Directory Policy clause 5G compliance.

---

## Python runtime dependencies

Every plugin in this family declares the same Python-side dependency in its `pyproject.toml`:

| Dependency | Pin | Latest on PyPI (2026-06-01) | Status |
|---|---|---|---|
| `mcp[cli]` | `>=1.0.0` | `1.27.2` (released 2026-05-29) | ✅ Supported. The `>=1.0.0` floor admits all 1.x releases; `uv` resolves to the latest at install. No CVE-flagged versions in the 1.x line as of audit date. |

All plugins use the same `uv` server runtime declared in `manifest.json`:

```json
"server": {
  "type": "uv",
  "entry_point": "server/main.py",
  "mcp_config": { "command": "uv", "args": ["--directory", "${__dirname}", "run", "server/main.py"] }
}
```

`uv` is provided by Claude Desktop at install time; no plugin embeds or vendors `uv`.

## System-level dependencies (user-provided)

| Tool | Purpose | Required / Optional |
|---|---|---|
| `pandoc` | `.docx` rendering at the `save_draft_as_docx` step | Required for `.docx` output. Optional if user accepts markdown-only drafts. |
| `pdftotext` (Poppler) | PDF text extraction at the Reader stage | Optional. Reader falls back to text/markdown inputs if `pdftotext` is unavailable. |

Both are mainstream OSS distributed by Linux package managers, Homebrew (macOS), and official Windows installers. The plugins do not bundle, ship, or auto-install these system tools.

## Build-time dependencies

| Dependency | Pin | Notes |
|---|---|---|
| `hatchling` | `requires = ["hatchling"]` | Standard PEP 517 build backend. Used only at build time, never at runtime. |

## No node_modules

These plugins are pure Python via `uv`. There is no `node_modules` directory, no Node.js dependency tree, and no JavaScript runtime requirement. Anthropic Software Directory Policy §5G's `node_modules`-currency requirement is not applicable.

## Vulnerability-scan posture

Publisher commits to re-running this audit:

- **On every release** of any plugin in the family.
- **Within 7 days** of a CVE disclosure affecting `mcp`, `hatchling`, `pandoc`, or `pdftotext`.
- **Within 30 days** of any major-version bump in `mcp` (currently `1.x`).

Report findings (or stale audit) to **wolfgangrush@gmail.com** with subject line `[SECURITY] DEPENDENCY_AUDIT`.

## Per-plugin pin reference

All 14 plugins declare the identical Python dependency set:

```toml
dependencies = ["mcp[cli]>=1.0.0"]
```

Verified across:

1. wolfgang-district-court-drafting
2. wolfgang-indian-banking-drafting
3. wolfgang-indian-company-drafting
4. wolfgang-indian-consumer-drafting
5. wolfgang-indian-contracts-drafting
6. wolfgang-indian-family-drafting
7. wolfgang-indian-hc-drafting
8. wolfgang-indian-ip-drafting
9. wolfgang-indian-labour-drafting
10. wolfgang-indian-mact-drafting
11. wolfgang-indian-property-drafting
12. wolfgang-indian-rent-control-drafting
13. wolfgang-indian-tax-drafting
14. wolfgang-supreme-court-drafting

---

*This document is shipped at the family root and referenced by each plugin's SECURITY.md. It will be re-published on each release.*
