# Security Posture

## Execution model

This MCPB runs entirely on the user's local machine via the `uv` Python runtime. There is no remote server. There is no outbound network call from the connector code.

## Permissions requested

The connector reads and writes files only within paths the user explicitly passes to its tools. Specifically:

- `read_case_folder(path)` reads files within the supplied folder
- `save_draft_as_docx(output_path)` writes a single .docx file to the supplied path

The connector does not silently scan, index, or transmit any other part of the file system.

## Dependencies

- `mcp[cli]>=1.0.0` — Anthropic's MCP Python SDK
- `pandoc` (system-level) — for .docx rendering
- `pdftotext` (system-level, optional) — for PDF case-file extraction

All Python dependencies are resolved by `uv` from PyPI at first run and cached locally.

## Source transparency

All source code is published under MIT License at <https://github.com/Wolfgangrush/supreme-court-drafting-mcpb>. No obfuscated binaries. No remote-loaded code paths.

## Security disclosure

Report security issues to **advrushikeshravindramahajan@gmail.com** with the subject line beginning `[SECURITY]`. Public disclosure should follow a 30-day responsible-disclosure window where practicable.

## Threat model — what this connector does NOT protect against

- Loss of advocate-client privilege if the user passes privileged material into a Claude Desktop conversation (governed by **Anthropic's privacy policy** at <https://www.anthropic.com/legal/privacy>, not by this connector)
- Disclosure of case-folder contents to other applications that have file-system access on the user's machine
- Compromise of the user's machine via unrelated vectors

## License

MIT.
