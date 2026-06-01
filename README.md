# Wolfgang Rush — Supreme Court Drafting

**MCPB Desktop Extension** for drafting pleadings before the Supreme Court of India.

Designed for Indian advocates using **Claude Desktop App**. Local-execution. Zero data collection.

> *Also available as a Claude Code Plugin (for developers using the Claude Code CLI):*
> *[github.com/Wolfgangrush/supreme-court-drafting-litigation](https://github.com/Wolfgangrush/supreme-court-drafting-litigation)*

---

## What this connector does

Exposes the Wolfgang Rush six-agent SC drafting pipeline as MCP tools that Claude can orchestrate from a Claude Desktop chat. Drafts the following case types:

| Case type | Statutory anchor |
|---|---|
| SLP (Civil) | Article 136 of the Constitution |
| SLP (Criminal) | Article 136 of the Constitution |
| Writ Petition (Article 32) | Article 32 of the Constitution |
| Transfer Petition | Section 25 CPC / Section 406 CrPC |
| Review Petition | Article 137 + Order XLVII SC Rules 2013 |
| Curative Petition | Rupa Hurra (2002) 4 SCC 388 framework |

Output is rendered as filing-grade `.docx` via pandoc using the bundled SC reference.docx (A4, Times New Roman 14, 1.5 line spacing, 4 cm left margin).

---

## Install

1. Open **Claude Desktop App**
2. **Settings → Extensions → Install Extension**
3. Select `wolfgang-supreme-court-drafting.mcpb`
4. Enable the extension
5. Start a new chat

## System requirements

- macOS, Windows, or Linux with Claude Desktop App ≥ 0.10.0
- Python ≥ 3.10 (Claude Desktop App bundles uv runtime automatically)
- **`pandoc`** for `.docx` output (`brew install pandoc` on macOS · `apt-get install pandoc` on Linux · download from pandoc.org on Windows)
- **`pdftotext`** for PDF reading (`brew install poppler` on macOS · `apt-get install poppler-utils` on Linux)

## Usage

In a Claude Desktop chat, simply describe what you want to draft. Claude will discover and call the connector's tools as needed.

Example prompts:

- *"Draft an SLP-civil under Article 136 against the Bombay HC dismissal dated 2026-04-10, with grounds based on perversity of finding on issue 3."*
- *"Draft a writ petition under Article 32 challenging Section X of [ACT-Y] on Article 14 and 21 grounds, with prayer for interim stay."*
- *"Draft a curative petition within the Rupa Hurra limbs — gross miscarriage of justice plus abuse of process."*

Claude will:
1. Call `list_case_types()` to discover available case types
2. Call `get_case_type_format(case_type)` to retrieve the drafting template
3. Call `get_pleading_base()` to retrieve the universal SC pleading structure
4. Optionally call `read_case_folder(path)` if you point it at a case-files folder
5. Draft the pleading
6. Optionally call `save_draft_as_docx(...)` to render the final `.docx`

## Tools

| Tool | Purpose |
|---|---|
| `list_case_types` | Discover available SC case types |
| `get_case_type_format` | Retrieve the drafting template for a specific case type |
| `get_agent_instructions` | Retrieve instructions for a stage in the six-agent pipeline |
| `get_pleading_base` | Retrieve the universal SC pleading skeleton + Registry formatting |
| `read_case_folder` | Read files in a case folder for fact extraction |
| `save_draft_as_docx` | Render markdown as filing-grade .docx |

## Privacy

This connector collects **zero** user data. All processing happens on the user's machine. The publisher (Wolfgang Rush) never receives any user data.

The connector applies a three-layer privacy firewall recommended for all case-folder work:
- **L1 substitution** — real party names, case numbers, financial figures replaced with neutral placeholders before any text is sent to Claude
- **L2 LLM-blind** — Claude sees only placeholders, never the real privileged data
- **L3 re-substitution** — placeholders mapped back to real values at the `.docx` render stage on the user's machine

Read the canonical privacy policy at **<https://wolfgangrush.github.io/privacy/>**.

## Confidentiality and professional privilege

Case-folder contents passed to this connector may include material attracting attorney-client privilege under **Section 132 of the Bharatiya Sakshya Adhiniyam 2023** / **Section 126 of the Indian Evidence Act 1872**. Decisions about what material to supply remain the user's professional responsibility consistent with applicable Bar Council of India rules and client-engagement terms.


## ⚠️ AI verification disclaimer · 🔒 Pseudonymisation procedure

> **⚠️ AI can make mistakes — please verify the information before filing.**
> Every draft produced by this connector is a STARTING POINT. The Verifier
> agent runs an anti-hallucination firewall and the Overseer agent runs an
> opposing-counsel review, but neither replaces an advocate's independent
> verification of statutory references, citation accuracy, factual fidelity,
> and Registry-formatting compliance with the user's High Court / forum.
> The advocate filing the pleading remains responsible for the contents.
>
> **🔒 Protected by pseudonymisation procedure.** The Reader agent applies a
> domain-specific privacy firewall as the first step of the pipeline — party
> names, addresses, identifying numbers (FIR / CR / Crime / Suit / Diary /
> SLP / lower-court case numbers), PAN / Aadhaar references, financial
> figures, witness names, and statutory-notice references are substituted
> with structural placeholders BEFORE any downstream agent sees the facts.
> The Drafter, Verifier, Refiner, and Overseer agents process placeholders
> only. Real values are re-substituted at the final docx render step on the
> user's local machine. No real identifying data leaves the case folder.

## License

MIT. See LICENSE.

## Publisher

**Rushikesh R. Mahajan**, Advocate, Bombay High Court (Nagpur Bench), publishing as **Wolfgang Rush**.

Contact: advrushikeshravindramahajan@gmail.com

## Source

<https://github.com/Wolfgangrush/supreme-court-drafting-mcpb>

## Sample cases

See `SAMPLE-CASES/` for three anonymised fact patterns the reviewer can use to invoke the tools.
