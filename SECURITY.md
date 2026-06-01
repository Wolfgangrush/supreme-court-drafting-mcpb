# Security Policy

## Execution model

This MCPB runs entirely on the user's local machine via the `uv` Python runtime. There is no remote server. There is no outbound network call from the connector code.

## Permissions requested

The connector reads and writes files only within paths the user explicitly passes to its tools. It does not silently scan, index, or transmit any other part of the file system.

## Reporting a Vulnerability

Report security issues by email to **wolfgangrush@gmail.com** with the subject line beginning `[SECURITY] wolfgang-supreme-court-drafting`.

Please do **not** open public GitHub Issues for security vulnerabilities. Use Issues only for non-security bugs and feature requests.

## Response Timeline (SLA)

- Acknowledgement of report: within **5 business days**
- Initial triage + severity assessment: within **10 business days**
- Fix or documented mitigation plan: within **30 business days** for High / Critical severity; **60 business days** for Medium; best-effort for Low

## Coordinated Disclosure

We follow a **90-day coordinated disclosure** policy:

- After acknowledgement, we aim to ship a fix within 90 days.
- We will coordinate a public disclosure date with the reporter.
- We credit the reporter in the changelog unless anonymity is requested.
- If a fix is not feasible within 90 days, we will communicate a revised timeline before the deadline.

## Supported Versions

| Version       | Supported           |
|---------------|---------------------|
| 0.1.6-alpha   | ✅ Yes (current)    |
| 0.1.5-alpha   | ✅ Yes              |
| < 0.1.5       | ❌ No               |

Pre-1.0 versions receive security fixes only for the latest two minor releases. After 1.0, a longer-term support window will be published.

## Out of Scope

- Vulnerabilities in Claude Desktop, the MCP protocol, or upstream dependencies — please report those to the respective maintainers.
- Issues that require physical access to the user's machine.
- Issues in user-supplied case-folder content (the plugin treats this as trusted input; users are responsible for the content they place there).
- Loss of advocate-client privilege if the user passes privileged material into a Claude Desktop conversation (governed by Anthropic's privacy policy, not by this connector).

## Dependencies

- `mcp[cli]>=1.0.0` — Anthropic's MCP Python SDK
- `pandoc` (system-level) — for .docx rendering
- `pdftotext` (system-level, optional) — for PDF case-file extraction

All Python dependencies are resolved by `uv` from PyPI at first run and cached locally. A dependency-currency audit is published in this repository (`DEPENDENCY_AUDIT.md`).

## Source transparency

All source code is published under MIT License at the repository URL recorded in `manifest.json`. No obfuscated binaries. No remote-loaded code paths.

## License

MIT.
