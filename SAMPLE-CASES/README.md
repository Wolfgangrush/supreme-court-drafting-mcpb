# Sample Cases — Reviewer Examples

Three anonymised SC fact patterns the Anthropic reviewer can use to invoke the connector's tools and exercise the drafting pipeline.

All party names are placeholders. No real client data appears here.

---

## Example 1 — SLP (Civil) under Article 136

**Prompt to use in Claude Desktop chat:**

> *"Draft an SLP (Civil) under Article 136 against the Bombay HC dismissal dated 2026-04-10 in [PARTY-A] vs [PARTY-B] (Second Appeal No. 1234/2024). Grounds: perversity of finding on Issue 3 (whether the suit property is joint family property) and incorrect application of Mulla on Hindu Law. Limitation: 90 days, filing within time. Custody status: not applicable. Prayer: leave to appeal + setting aside of HC order + decree of partition."*

**Expected tool sequence:**
1. `list_case_types()` → confirms slp-civil available
2. `get_case_type_format("slp-civil")` → retrieves SLP-civil drafting template
3. `get_pleading_base()` → retrieves SC pleading skeleton + Registry formatting
4. Drafts the SLP using statutory anchors (Article 136, Order XXI SC Rules 2013)
5. `save_draft_as_docx(markdown, "/path/draft-slp-civil.docx")` → renders filing-grade .docx

---

## Example 2 — Writ Petition under Article 32

**Prompt to use in Claude Desktop chat:**

> *"Draft a writ petition under Article 32 challenging the constitutional validity of Section [SECTION-X] of [ACT-Y]-Act, 2024 on grounds of violation of Articles 14, 19(1)(a), and 21. Petitioner is a registered association of [STAKEHOLDERS-Z]. Prayer: declare Section [SECTION-X] ultra vires + writ of mandamus restraining enforcement + interim stay during pendency."*

**Expected tool sequence:**
1. `list_case_types()` → confirms writ-art32 available
2. `get_case_type_format("writ-art32")` → retrieves Article 32 writ drafting template
3. `get_pleading_base()` → retrieves SC pleading skeleton
4. Drafts the writ using fundamental-rights framework (Article 13, 14, 19, 21, Article 32)
5. `save_draft_as_docx(markdown, "/path/draft-writ-art32.docx")` → renders filing-grade .docx

---

## Example 3 — Curative Petition (Rupa Hurra)

**Prompt to use in Claude Desktop chat:**

> *"Draft a curative petition in [MATTER-CODE] against the SC judgment dated 2025-11-15 in Review Petition No. 567/2025. Curative limbs to plead: (1) gross miscarriage of justice on Issue [ISSUE-Q], (2) violation of principles of natural justice (no opportunity to address point raised suo motu by the Court), (3) abuse of process. Senior counsel certificate attached."*

**Expected tool sequence:**
1. `list_case_types()` → confirms curative-petition available
2. `get_case_type_format("curative-petition")` → retrieves curative drafting template
3. `get_pleading_base()` → retrieves SC pleading skeleton
4. Drafts the curative within the Rupa Hurra (2002) 4 SCC 388 limbs
5. `save_draft_as_docx(markdown, "/path/draft-curative.docx")` → renders filing-grade .docx

---

## Notes for the reviewer

- These examples use placeholder party names (`[PARTY-A]`, `[PARTY-B]`, `[SECTION-X]`, `[ACT-Y]`, etc.) — no real client data.
- The connector does not require any external API keys or accounts.
- The `read_case_folder(path)` tool is optional and only used when the user has prepared a case-files folder on their machine; the three examples above do not require it.
- The `save_draft_as_docx` tool requires `pandoc` to be installed on the user's machine — see the connector's `README.md` for install instructions.
- The connector applies a three-layer privacy firewall throughout — no real party names need ever be sent to Claude in identifiable form.
