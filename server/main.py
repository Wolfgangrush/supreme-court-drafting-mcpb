"""Wolfgang Rush — Supreme Court Drafting MCPB.

Local-execution MCPB Desktop Extension for the Supreme Court of India. Exposes
the six-agent SC drafting pipeline and six case-type drafting templates as MCP
tools that Claude can orchestrate from a Claude Desktop chat.

Privacy posture: zero data collection. All processing happens on the user's
machine. The publisher (Wolfgang Rush) never receives any user data.

License: MIT
Source: https://github.com/Wolfgangrush/supreme-court-drafting-mcpb
Privacy policy: https://wolfgangrush.github.io/privacy/
"""

from __future__ import annotations

import re
import subprocess
from datetime import datetime
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

DEFAULT_DRAFTS_ROOT = Path.home() / "Downloads" / "Wolfgang-Rush-Drafts"
ALLOWED_ARTIFACT_NAMES = {
    "case-facts.md",
    "format-shell.md",
    "draft-v1.md",
    "draft-v1.docx",
    "verification-report.md",
    "draft-v2.md",
    "draft-v2.docx",
    "opposing-notes.md",
    "final-draft.md",
}

mcp = FastMCP("wolfgang-supreme-court-drafting")

BUNDLE_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = BUNDLE_ROOT / "skills"
AGENTS_DIR = BUNDLE_ROOT / "agents"

CASE_TYPES: list[str] = [
    "slp-civil",
    "slp-criminal",
    "writ-art32",
    "transfer-petition",
    "review-petition",
    "curative-petition",
]

CASE_TYPE_DESCRIPTIONS: dict[str, str] = {
    "slp-civil": "Special Leave Petition (Civil) under Article 136 of the Constitution",
    "slp-criminal": "Special Leave Petition (Criminal) under Article 136 of the Constitution",
    "writ-art32": "Writ Petition under Article 32 of the Constitution",
    "transfer-petition": "Transfer Petition under Section 25 CPC / Section 406 CrPC",
    "review-petition": "Review Petition under Article 137 read with Order XLVII Supreme Court Rules 2013",
    "curative-petition": "Curative Petition under the Rupa Hurra framework",
}

AGENT_NAMES: list[str] = [
    "reader",
    "format",
    "drafter",
    "verifier",
    "refiner",
    "overseer",
]




ACRONYM_TO_CASE_TYPE: dict[str, str] = {
    "SLP-C": "slp-civil",
    "SLP-Cr": "slp-criminal",
    "TP": "transfer-petition",
    "WP-Art32": "writ-art32",
    "Review": "review-petition",
    "Curative": "curative-petition",
}


FULL_ORCHESTRATION_SCRIPT = """# WOLFGANG RUSH — SUPREME COURT OF INDIA DRAFTING · FULL ORCHESTRATION SCRIPT

**YOU MUST execute every step below in order. DO NOT skip steps. DO NOT write
standalone python-docx, JavaScript, or shell scripts to generate output —
invoke the tools listed at each step.**


## STEP 0 PRE-CHECK — CASE-TYPE DISAMBIGUATION (CRITICAL — DO NOT GUESS)

Indian practice uses acronyms / form-references that are NOT phonetic. Read this
table BEFORE picking case_type. The user's ACRONYM or FORM REFERENCE is the
source of truth — DO NOT re-classify based on what the input "looks like."

| User typed | case_type value |
|------------|-----------------|
| **SLP-C** | `slp-civil` |
| **SLP-Cr** | `slp-criminal` |
| **TP** | `transfer-petition` |
| **WP-Art32** | `writ-art32` |
| **Review** | `review-petition` |
| **Curative** | `curative-petition` |

If the acronym is not in the table above, ask the user to spell it out.

## STEP 0 — CREATE THE CASE FOLDER

Call `create_case_folder(case_type)` where `case_type` is one of:
slp-civil, slp-criminal, writ-art32, transfer-petition, review-petition, curative-petition.

The tool returns `case_folder` — an absolute path. **Use this path in every
subsequent save_artifact and save_draft_as_docx call.**

## STEP 1 — MATERIALIZE THE USER'S INPUT DOCUMENTS

Every source document the user attached to this conversation must be saved to
disk before the Reader can run. For each attachment:

Call `save_artifact(case_folder, "inputs/source-document.txt", <extracted-text>)`

## STEP 2 — LOAD THE CASE-TYPE SKILL

Call `get_case_type_format(case_type)`. Read the returned SKILL.md carefully.

## STEP 3 — LOAD THE PLEADING BASE

Call `get_pleading_base()`. Read the universal skeleton + common drafting
discipline (citation rules, AI-fabricated-citation risk per HC cautions).

## STEP 4 — RUN THE READER AGENT (APPLIES PRIVACY FIREWALL)

Call `get_agent_instructions("reader")` to load the Reader persona. The Reader
applies the privacy firewall — substitutes party names, addresses, identifying
numbers, financial figures, statutory-notice references with structural
placeholders BEFORE any downstream agent processes the facts.

Save the output via `save_artifact(case_folder, "case-facts.md", <content>)`.

## STEP 5 — RUN THE FORMAT AGENT

Call `get_agent_instructions("format")`. Map case-facts.md (already privacy-
firewalled) into the SKILL.md placeholders.

Save via `save_artifact(case_folder, "format-shell.md", <content>)`.

## STEP 6 — RUN THE DRAFTER AGENT

Call `get_agent_instructions("drafter")`. Write the first complete draft using
format-shell.md as scaffold and case-facts.md as ground-truth.

Save markdown via `save_artifact(case_folder, "draft-v1.md", <content>)`. Then
`save_draft_as_docx(<markdown>, f"{case_folder}/draft-v1.docx")`.

## STEP 7 — RUN THE VERIFIER AGENT (ANTI-HALLUCINATION FIREWALL — DO NOT SKIP)

Call `get_agent_instructions("verifier")`. Compare draft-v1.md against
case-facts.md fact-by-fact. Flag every hallucinated date, fabricated citation,
unsupported assertion, orphan annexure marker, missing factual basis.

Save via `save_artifact(case_folder, "verification-report.md", <content>)`.

## STEP 8 — RUN THE REFINER AGENT

Call `get_agent_instructions("refiner")`. Apply every Verifier flag. Polish
language. Enforce Registry formatting.

Save via `save_artifact(case_folder, "draft-v2.md", <content>)` and
`save_draft_as_docx(<markdown>, f"{case_folder}/draft-v2.docx")`.

## STEP 9 — RUN THE OVERSEER AGENT (OPPOSING-COUNSEL LENS — DO NOT SKIP)

Call `get_agent_instructions("overseer")`. Read draft-v2.md with opposing-
counsel lens. Find weak prayers, contradictory facts, attackable defects.

Save via `save_artifact(case_folder, "opposing-notes.md", <content>)`. Then
apply hardening to produce final draft. Save via
`save_artifact(case_folder, "final-draft.md", <content>)` and
`save_draft_as_docx(<markdown>, f"{case_folder}/final-draft.docx")`.

## STEP 10 — REPORT TO THE USER

Return the absolute path to `final-draft.docx` and a one-paragraph summary.

---

**FALSIFICATION CHECK:** the case folder must contain at minimum:
1. case-facts.md
2. format-shell.md
3. draft-v1.docx (or draft-v1.md)
4. verification-report.md
5. draft-v2.docx (or draft-v2.md)
6. final-draft.docx

If any are missing, return to the matching STEP and produce it.

**REMINDER:** YOU MUST NOT write a standalone python-docx generator, a
JavaScript script, or any one-shot drafting program. The MCPB exposes every
required tool. Use them.
"""


@mcp.tool(annotations=ToolAnnotations(title="Get Pipeline Agent Instructions", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_agent_instructions(agent_name: str = "") -> str:
    """Get the instructions for the drafting pipeline.

    Default mode (no agent_name, or agent_name=""): returns the FULL orchestration
    script enumerating every step and tool call from case-folder creation through
    final-draft.docx. THIS IS THE MANDATORY FIRST CALL when the user asks you to
    draft anything.

    Single-agent mode (agent_name ∈ {reader, format, drafter, verifier, refiner,
    overseer}): returns that agent's persona instructions only.
    """
    if not agent_name or agent_name == "full":
        return FULL_ORCHESTRATION_SCRIPT
    if agent_name not in AGENT_NAMES:
        return (
            f"Error: unknown agent_name '{agent_name}'. "
            f"Available: {', '.join(AGENT_NAMES)}. "
            "Call with no arguments to receive the full orchestration script."
        )
    agent_md = AGENTS_DIR / agent_name / f"{agent_name}.md"
    if not agent_md.exists():
        return f"Error: agent file not found for '{agent_name}'."
    return agent_md.read_text(encoding="utf-8")


@mcp.tool(annotations=ToolAnnotations(title="Get Pleading Base Structure", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def get_pleading_base() -> str:
    """Get the shared SC pleading base structure used by all case-types.

    Returns the universal Supreme Court pleading skeleton (Cause Title
    to Synopsis to List of Dates to Statement of Facts to Questions of Law
    to Grounds to Main Prayer to Interim Prayer to Annexures), the SC
    Registry formatting rules (A4, Times New Roman 14, 1.5 line spacing,
    4 cm left margin), and the cross-cutting drafting discipline (citation
    discipline, AOR Certificate language, AI-fabricated-citation risk).
    """
    base_md = SKILLS_DIR / "_sc_pleading_base" / "SKILL.md"
    formatting_md = SKILLS_DIR / "_sc_pleading_base" / "FORMATTING.md"
    common_md = SKILLS_DIR / "_drafting_common" / "SKILL.md"

    parts: list[str] = []
    if base_md.exists():
        parts.append("# Supreme Court Pleading Base")
        parts.append("")
        parts.append(base_md.read_text(encoding="utf-8"))
    if formatting_md.exists():
        parts.append("")
        parts.append("---")
        parts.append("")
        parts.append("# Supreme Court Registry Formatting Rules")
        parts.append("")
        parts.append(formatting_md.read_text(encoding="utf-8"))
    if common_md.exists():
        parts.append("")
        parts.append("---")
        parts.append("")
        parts.append("# Common Drafting Discipline")
        parts.append("")
        parts.append(common_md.read_text(encoding="utf-8"))
    return "\n".join(parts)


@mcp.tool(annotations=ToolAnnotations(title="Read Case Folder Files", readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def read_case_folder(path: str) -> dict:
    """Read all files in a case folder on the user's machine for fact extraction.

    Walks the folder recursively, reads .md, .txt, .pdf (via pdftotext), and
    .docx (via pandoc) files, and returns their text content as a dict mapping
    relative filename to content. Hidden files (dot-prefixed) are skipped.
    Files that cannot be extracted are reported in the warnings list.

    Args:
        path: Absolute or relative path to the case folder on the user's machine.
    """
    folder = Path(path).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        return {
            "error": f"Path '{path}' is not a valid directory.",
            "files": {},
            "warnings": [],
            "file_count": 0,
        }

    files: dict[str, str] = {}
    warnings: list[str] = []

    for f in sorted(folder.rglob("*")):
        if not f.is_file():
            continue
        if any(part.startswith(".") for part in f.relative_to(folder).parts):
            continue
        rel = f.relative_to(folder).as_posix()
        ext = f.suffix.lower()

        try:
            if ext in (".md", ".txt"):
                files[rel] = f.read_text(encoding="utf-8", errors="replace")
            elif ext == ".pdf":
                try:
                    result = subprocess.run(
                        ["pdftotext", str(f), "-"],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )
                    if result.returncode == 0:
                        files[rel] = result.stdout
                    else:
                        warnings.append(f"pdftotext failed on {rel}: {result.stderr.strip()[:200]}")
                        files[rel] = f"[PDF file at {rel} — text not extracted]"
                except FileNotFoundError:
                    warnings.append(
                        "pdftotext not installed. Install via 'brew install poppler' "
                        "(macOS) or 'apt-get install poppler-utils' (Linux) to extract PDF text."
                    )
                    files[rel] = f"[PDF file at {rel} — pdftotext not installed]"
                except subprocess.TimeoutExpired:
                    warnings.append(f"pdftotext timed out on {rel}")
                    files[rel] = f"[PDF file at {rel} — extraction timed out]"
            elif ext == ".docx":
                try:
                    result = subprocess.run(
                        ["pandoc", "-f", "docx", "-t", "markdown", str(f)],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )
                    if result.returncode == 0:
                        files[rel] = result.stdout
                    else:
                        warnings.append(f"pandoc failed on {rel}: {result.stderr.strip()[:200]}")
                        files[rel] = f"[DOCX file at {rel} — text not extracted]"
                except FileNotFoundError:
                    warnings.append(
                        "pandoc not installed. Install via 'brew install pandoc' "
                        "(macOS) or 'apt-get install pandoc' (Linux)."
                    )
                    files[rel] = f"[DOCX file at {rel} — pandoc not installed]"
                except subprocess.TimeoutExpired:
                    warnings.append(f"pandoc timed out on {rel}")
                    files[rel] = f"[DOCX file at {rel} — extraction timed out]"
            else:
                warnings.append(f"Skipped unsupported file type: {rel}")
        except Exception as exc:
            warnings.append(f"Error reading {rel}: {exc}")

    return {
        "folder": str(folder),
        "files": files,
        "warnings": warnings,
        "file_count": len(files),
    }


@mcp.tool(annotations=ToolAnnotations(title="Save Draft as Filing-Grade DOCX", readOnlyHint=False, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def save_draft_as_docx(markdown_text: str, output_path: str) -> dict:
    """Save a draft pleading as a filing-grade .docx using pandoc.

    Renders the supplied markdown text to a Microsoft Word .docx file using
    pandoc, with the bundled SC reference.docx applied for filing-grade
    formatting (A4, Times New Roman 14, 1.5 line spacing, 4 cm left margin,
    underlined section headers, bold paragraph numbers).

    Args:
        markdown_text: The draft pleading content in markdown format.
        output_path: Absolute or relative path on the user's machine where the
                     .docx file should be saved. Parent directories are created
                     automatically if missing.
    """
    output = Path(output_path).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    reference_docx = SKILLS_DIR / "_sc_pleading_base" / "reference.docx"

    temp_md = output.parent / f".{output.stem}.tmp.md"
    temp_md.write_text(markdown_text, encoding="utf-8")

    cmd = ["pandoc", str(temp_md), "-o", str(output)]
    if reference_docx.exists():
        cmd.extend(["--reference-doc", str(reference_docx)])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        temp_md.unlink(missing_ok=True)

        if result.returncode != 0:
            return {
                "success": False,
                "error": result.stderr.strip()[:500],
                "output_path": str(output),
            }

        return {
            "success": True,
            "output_path": str(output),
            "file_size_bytes": output.stat().st_size,
            "reference_docx_applied": reference_docx.exists(),
        }
    except FileNotFoundError:
        temp_md.unlink(missing_ok=True)
        return {
            "success": False,
            "error": (
                "pandoc not installed. Install via 'brew install pandoc' (macOS), "
                "'apt-get install pandoc' (Linux), or download from pandoc.org (Windows)."
            ),
            "output_path": str(output),
        }
    except subprocess.TimeoutExpired:
        temp_md.unlink(missing_ok=True)
        return {
            "success": False,
            "error": "pandoc conversion timed out after 60 seconds.",
            "output_path": str(output),
        }


def _sanitise_path_component(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9._-]", "-", value.strip())
    cleaned = cleaned.strip(".-_") or "untitled"
    return cleaned[:80]


@mcp.tool(annotations=ToolAnnotations(title="Create Case Folder", readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=False))
def create_case_folder(case_type: str, base_dir: str = "") -> dict:
    """Create the case folder for a drafting session on the user's machine.

    Creates a timestamped folder under ~/Downloads/Wolfgang-Rush-Drafts/ (or the
    base_dir if supplied) named <case-type>-<YYYYMMDD-HHMMSS>/, with an inputs/
    subfolder for source documents. Cross-platform (macOS / Windows / Linux).
    """
    if case_type not in CASE_TYPES:
        return {"error": f"unknown case_type '{case_type}'. Available: {', '.join(CASE_TYPES)}."}
    parent = Path(base_dir).expanduser().resolve() if base_dir else DEFAULT_DRAFTS_ROOT
    parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    folder_name = f"{_sanitise_path_component(case_type)}-{timestamp}"
    case_folder = parent / folder_name
    inputs_folder = case_folder / "inputs"
    inputs_folder.mkdir(parents=True, exist_ok=True)
    readme = case_folder / "README.md"
    readme.write_text(
        f"# Wolfgang Rush Drafting Case Folder\n\n"
        f"- Case type: {case_type}\n"
        f"- Created: {datetime.now().isoformat(timespec='seconds')}\n\n"
        f"## Artifacts (pipeline output)\n"
        f"- `inputs/` — source documents\n"
        f"- `case-facts.md` — Reader output (privacy-firewalled)\n"
        f"- `format-shell.md` — Format output\n"
        f"- `draft-v1.docx` — Drafter output\n"
        f"- `verification-report.md` — Verifier output\n"
        f"- `draft-v2.docx` — Refiner output\n"
        f"- `opposing-notes.md` — Overseer output\n"
        f"- `final-draft.docx` — Final filing-grade output\n",
        encoding="utf-8",
    )
    return {
        "case_folder": str(case_folder),
        "inputs_folder": str(inputs_folder),
        "case_type": case_type,
        "timestamp": timestamp,
        "next_step": (
            "Save every source document the user attached to this conversation "
            f"into '{inputs_folder}' via save_artifact, then proceed to STEP 2 "
            "of the orchestration script (get_case_type_format)."
        ),
    }


@mcp.tool(annotations=ToolAnnotations(title="Save Pipeline Artifact", readOnlyHint=False, destructiveHint=False, idempotentHint=True, openWorldHint=False))
def save_artifact(case_folder: str, relative_path: str, content: str) -> dict:
    """Save a pipeline artifact or input document into the case folder.

    Required at the end of every agent step. Pipeline artifact names accepted at
    the root: case-facts.md, format-shell.md, draft-v1.md, draft-v1.docx,
    verification-report.md, draft-v2.md, draft-v2.docx, opposing-notes.md,
    final-draft.md. Input documents go under inputs/ (e.g.,
    'inputs/source-document.txt').
    """
    case_dir = Path(case_folder).expanduser().resolve()
    if not case_dir.exists() or not case_dir.is_dir():
        return {"success": False, "error": f"case_folder '{case_folder}' does not exist. Call create_case_folder first."}
    rel = Path(relative_path)
    if rel.is_absolute():
        return {"success": False, "error": "relative_path must not be absolute."}
    if any(part == ".." for part in rel.parts):
        return {"success": False, "error": "relative_path must not contain '..'."}
    is_root_artifact = len(rel.parts) == 1
    if is_root_artifact and rel.name not in ALLOWED_ARTIFACT_NAMES:
        return {"success": False, "error": f"'{rel.name}' is not a recognised root-level artifact. Allowed: {', '.join(sorted(ALLOWED_ARTIFACT_NAMES))}. Input documents must go under inputs/."}
    target = (case_dir / rel).resolve()
    try:
        target.relative_to(case_dir)
    except ValueError:
        return {"success": False, "error": "resolved path escapes the case_folder."}
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return {"success": True, "path": str(target), "file_size_bytes": target.stat().st_size, "relative_path": rel.as_posix()}


if __name__ == "__main__":
    mcp.run()
