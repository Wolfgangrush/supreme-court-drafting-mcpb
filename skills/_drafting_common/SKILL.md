---
name: _drafting_common
description: Shared reference for all Supreme Court of India drafting skills. Holds the enforcement rules, architecture constraints, and SC AI-use risk context. NOT invoked directly — referenced from every drafting skill via ${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md.
allowed-tools: []
---

# Shared Drafting Common — Rules & Constraints (Supreme Court of India)

This file is referenced from every drafting skill in the `supreme-court-drafting` plugin. It is NOT invoked on its own.

## THE ENFORCEMENT RULES (non-negotiable)

1. **No external-memory MCP tools in drafting skills.** Drafting skill `allowed-tools:` lists MUST exclude any external-memory, vault, or cloud-sync MCP tool. A drafting skill operates strictly on the case folder. Hard wall.

2. **Case-folder scoping.** Every drafting skill should auto-fire only when the user is working inside a case folder. The user configures the auto-fire path themselves. The plugin ships with NO hardcoded case path — the path is user-controlled.

3. **Per-case CLAUDE.md is OPT-IN, self-contained.** No external imports. No global-context inheritance. Case context only — parties, court (always "Supreme Court of India" in this plugin), Bench composition (if known), key dates, counsel's role, AOR's name and code (placeholder until filing).

4. **Drafting skills do not interact with any general note-taking / archive skill.** Out of scope for this plugin; documented as a hygiene recommendation.

5. **Any external diary / project tracker** that mentions case work should reference cases by code or pattern only, NEVER by quoting draft text or party names verbatim. Out of scope for this plugin but a sensible practice.

6. **🔴 LAYER 2 IS APPEND-ONLY FROM SKILL/AGENT SIDE.**
   - Skills/agents may: READ existing files in case folder, WRITE new draft files (case-facts.md, format-shell.md, draft-v*.docx, etc.), EDIT files they themselves created in this session
   - Skills/agents may NOT: rm, mv, rmdir, trash, rename, delete, overwrite-without-versioning
   - Enforcement recommendations:
     - `allowed-tools:` whitelist excludes destructive Bash patterns
     - User-side hook can block `rm`/`mv`/`rmdir`/`trash`/`unlink` on paths under the case folder
     - Periodic audit catches drift

6.1. **🔴 WORKING-COPY RULE — never operate on originals.**
   When an agent needs to convert / extract / transform an existing case file, it MUST:
   - Create a working subfolder: `~/.claude/working-copies/<case-name>/` (NOT inside the case folder)
   - Copy the original file there
   - Operate on the COPY only
   - Output produced in working-copies/ or /tmp/, never in the original case folder unless it's a final draft artifact
   - The original file is NEVER read, opened-for-write, or processed in place

## LOCKED CONSTRAINTS (Supreme Court AI-use risk)

> The Supreme Court of India and various High Courts have publicly cautioned advocates against AI-generated content with fabricated citations. The Supreme Court itself issued a circular dated 17 July 2023 (and subsequent communications) noting concern over unverified AI output in pleadings. **One hallucinated authority before the Supreme Court = career-threatening.**

These rules apply to every drafting agent:

- **NO internet for facts.** No WebSearch, no WebFetch for case content. Hardcoded sources only (the case folder + the law PDFs the user supplies).
- **Constitutional articles + statutes available from training data:** Constitution of India, Code of Civil Procedure 1908, Indian Penal Code 1860 / Bharatiya Nyaya Sanhita 2023, Code of Criminal Procedure 1973 / Bharatiya Nagarik Suraksha Sanhita 2023, Indian Evidence Act 1872 / Bharatiya Sakshya Adhiniyam 2023, Supreme Court Rules 2013. **All other statutes** (POCSO, NDPS, MV Act, IT Act, Arbitration and Conciliation Act, GST Acts, RTI Act, NSA, UAPA, PMLA, etc.) must be supplied by the user as PDF before they can be cited. Reader flags missing law PDFs and STOPS.
- **Case citations — STRICTER rule than HC plugin.** The Supreme Court itself has flagged AI-generated case citations as the highest-risk content. **Every case citation in the output MUST trace to either: (a) a citation supplied in the user's case folder, or (b) the user's manually-typed citation list.** Drafter NEVER generates a case name + citation pair from memory. If a ground requires support and no user-supplied citation matches, the Drafter writes a `[CITATION NEEDED: <legal proposition>]` placeholder and the Verifier flags it for the advocate to fill.
- **File-based pipeline.** Each agent writes its output to a file → next agent reads. Auditable chain of custody.
- **Triple-verify.** Verifier + Refiner + Overseer = 3 independent passes before the draft is shown to the user.
- **Final draft must be indistinguishable from an AOR-drafted pleading.** No "AI-style" markers: no "I'd be happy to," no bullet-list dumps where prose is expected, no markdown formatting in the .docx body, no first-person framing by the AI.
- **The user remains the responsible advocate / AOR.** The plugin is a drafting aid, not a substitute for professional judgment. Every draft must be reviewed before filing.

## SUPREME COURT FORMATTING CONVENTIONS

These conventions reflect the Registry practice of the Supreme Court of India, as derived from the Supreme Court Rules 2013, the Constitution, the Supreme Court Practice and Procedure (Office Procedure Handbook), and the Bar Council of India Standards of Professional Conduct and Etiquette. No template in this plugin reflects any specific client matter; the conventions are public procedural knowledge.

- **Court header:** `IN THE SUPREME COURT OF INDIA` (centred, all caps)
- **Jurisdiction line:** `CIVIL APPELLATE JURISDICTION` / `CRIMINAL APPELLATE JURISDICTION` / `CIVIL ORIGINAL JURISDICTION` (Art. 32) / `EXTRA-ORDINARY ORIGINAL JURISDICTION` (depending on case type)
- **Case number line:** `[CASE TYPE] (CIVIL/CRIMINAL) NO. _______ OF [YEAR]`
- **Arising-out-of parenthetical** (for SLP / Appeals): `(Arising out of impugned judgment / order dated <DD.MM.YYYY> passed by the Hon'ble High Court of [    ] at [    ] in [Case Type & Number])`
- **Parties separator:** `...VERSUS...` (preferred SC form)
- **Section heads:** Title Case with bold (`Statement of Facts`, `Questions of Law`, `Grounds`, `Prayer`)
- **Opening address:** `To, The Hon'ble Chief Justice of India and his Companion Justices.`
- **Salutation opener:** `The Humble Petition of the Petitioner above-named MOST RESPECTFULLY SHOWETH:`
- **Inline annexure marker:** `...a true copy whereof is annexed hereto and marked as ANNEXURE P-[N]`
- **Collective annexures:** `ANNEXURE P-[N] (COLLY)` for grouped documents
- **Main Prayer opener:** `In the premises aforesaid, it is most respectfully prayed that this Hon'ble Court may graciously be pleased to:`
- **Catchall prayer (last clause):** `Pass any further order(s) as this Hon'ble Court may deem fit and proper in the facts and circumstances of the case and in the interest of justice.`
- **Counsel block** (Petitioner-in-Person variant):
  ```
  NEW DELHI                                              [PETITIONER NAME]
  DATE: <DD.MM.YYYY>                                     PETITIONER-IN-PERSON
  ```
- **Counsel block** (Through AOR variant):
  ```
  NEW DELHI                                  ([AOR NAME], Advocate-on-Record)
  DATE: <DD.MM.YYYY>                         CODE: [AOR Registration No.]
                                             COUNSEL FOR THE PETITIONER
  ```

## ANNEXURE MECHANISM (SC convention)

Inline marker in Facts → consolidated table at end of pleading. SC uses the `P-N` (Petitioner) and `R-N` (Respondent) prefixes.

```
STATEMENT OF FACTS
- "...the impugned Order dated <DD.MM.YYYY> ... a true copy whereof is annexed hereto and marked as ANNEXURE P-1."
- "...the Petitioner's representation dated <DD.MM.YYYY> ... ANNEXURE P-2."
- "...witness depositions are annexed collectively as ANNEXURE P-3 (COLLY)."

LIST OF ANNEXURES
| Sr.No | Annexure | Particulars                            | Date            | Pages |
| 1     | P-1      | True copy of impugned Order [Case No.] | <DD.MM.YYYY>    | <N>   |
| 2     | P-2      | True copy of representation            | <DD.MM.YYYY>    | <N>   |
| 3     | P-3 (COLLY) | Depositions of <N> witnesses        | various         | <N>   |
```

Drafter MUST keep inline markers and List of Annexures in sync. Verifier checks for orphan markers (marker in Facts but not in List, or vice versa).

## STANDARD PLEADING SECTIONS (in order, all in one .docx)

For every SC petition / appeal, the .docx contains the universal SC section order from `_sc_pleading_base/SKILL.md`. To recap:

1. Cover Page (Registry format)
2. Index
3. Synopsis + List of Dates
4. Cause Title
5. Opening Address
6. Petition Proper
7. Statement of Facts
8. Questions of Law
9. Grounds
10. Grounds for Interim Relief
11. Main Prayer
12. Interim Prayer
13. Declarations (case-type-specific Rule reference)
14. Signature Block
15. AOR Certificate
16. Affidavit
17. Annexure Index + Annexures

Plus accompanying applications where the case type requires (Condonation of Delay, Stay, Exemption from filing certified copy, Permission to file SLP, etc.) — each accompanying application repeats its own Cause Title, Synopsis (if non-trivial), Affidavit, and Counsel / AOR block.

## OUTPUT FORMAT

- **File type:** `.docx` (so the user can open in Word and apply tracked-changes review)
- **Conversion tool:** pandoc (if installed) with a `reference.docx` template for SC formatting (A4, Times New Roman 14, 1.5 line spacing, 4cm left margin). Fallback: python-docx if pandoc unavailable.
- **Output filename convention:** `<case-type>_draft-v<N>_<YYYY-MM-DD>.docx`
   e.g., `slp-civil_draft-v1_2026-05-18.docx`
- **NEVER overwrite an existing draft.** Each run produces a new versioned file.

## RECOVERY / AUDIT

If anyone asks "how was this drafted":
1. Show the file chain: `case-facts.md` → `format-shell.md` → `draft-v1.docx` → `verification-report.md` → `draft-v2.docx` → `opposing-notes.md` → `final-draft.docx`
2. Each file has timestamp + agent that produced it
3. Inputs (source PDFs, law PDFs, citation list) all listed in `case-facts.md` Section 1
4. AOR signature and verification remain the AOR's responsibility — the audit trail goes up to the .docx produced; everything thereafter is the human AOR's review and signature

This is the audit-defense kit for any AI-use challenge before the Supreme Court.
