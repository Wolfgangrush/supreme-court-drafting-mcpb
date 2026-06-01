---
name: slp-civil-draft
description: Draft a Special Leave Petition (Civil) before the Supreme Court of India under Article 136 of the Constitution read with Order XXI of the Supreme Court Rules, 2013. Produces .docx containing Synopsis + List of Dates + Main Petition + Index + List of Annexures + AOR Certificate + Affidavit + (optional) Stay Application. Auto-fires on "draft slp civil" or "draft special leave petition civil" or "civil slp".
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Special Leave Petition (Civil) — Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_sc_pleading_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md` *(inherited from the shared drafting-common base via the plugin family)*

## Case-type metadata

```yaml
case_type_line: SPECIAL LEAVE PETITION (CIVIL)
case_short_code: SLP(C)
sc_rules_order: Order XXI of the Supreme Court Rules, 2013
form_reference: Form 28 of the Supreme Court Rules, 2013
constitutional_authority: Article 136 of the Constitution of India
jurisdiction_line: CIVIL APPELLATE JURISDICTION
statutory_opening: |
  SPECIAL LEAVE PETITION (CIVIL) UNDER ARTICLE 136 OF THE
  CONSTITUTION OF INDIA READ WITH ORDER XXI OF THE
  SUPREME COURT RULES, 2013
limitation_period_days: 90
limitation_period_days_if_certificate_refused: 60
limitation_source: |
  Article 133 of the Constitution of India read with the Limitation Act, 1963
  and Order XXI Rule 3 of the Supreme Court Rules, 2013
mandatory_declarations:
  - rule: "Rule 3(2) of Order XXI, SC Rules 2013"
    content: "No other petition seeking leave to appeal has been filed against the impugned judgment / order."
  - rule: "Rule 5 of Order XXI, SC Rules 2013"
    content: "The annexures filed are true copies of pleadings or documents that formed part of the record in the Court below."
mandatory_certificates:
  - "Advocate-on-Record Certificate under Order IV Rule 1(c) of the SC Rules 2013"
  - "Synopsis and List of Dates (SC Registry Practice Directions)"
accompanying_applications:
  - stay_application        # only if interim relief (stay of impugned order) sought
  - condonation_of_delay    # only if filed beyond 90 days
  - permission_to_file_slp  # only where applicable (e.g. against an order not directly appealable)
  - exemption_from_filing_certified_copy  # standard registry application
typical_annexure_order:
  - P-1: Certified copy of the impugned judgment / order of the High Court
  - P-2: Copy of the order of the trial court / first appellate court (as relevant)
  - P-3: Pleadings before the High Court (memo of appeal / writ petition / counter)
  - P-4: Material documents that formed part of the record below
  - P-Subsequent: documents supporting individual grounds
```

## Section-by-section structure (extends `_sc_pleading_base` Section 1)

The universal section order from the base applies. Slot-specific notes for SLP (Civil):

| # | Section | SLP-Civil specifics |
|---|---|---|
| 3 | Synopsis + List of Dates | **Mandatory.** Synopsis ≤ 3 pages. List of Dates chronological, ending with the impugned order. |
| 4 | Cause Title | `IN THE SUPREME COURT OF INDIA / CIVIL APPELLATE JURISDICTION / Special Leave Petition (Civil) No. _____ of [Year] / (Arising out of impugned judgment / order dated <DD.MM.YYYY> passed by the Hon'ble High Court of [   ] at [   ] in [Case Type & No.])` |
| 6 | Petition Proper opener | `The Humble Petition of the Petitioner above-named MOST RESPECTFULLY SHOWETH:` |
| 8 | Questions of Law | At least one substantial question of law warranting interference under Art. 136. Authored fresh from the facts; never lifted. |
| 9 | Grounds | Enumerated A, B, C ... Each ground is a fresh original paragraph naming the legal proposition, the impugned reasoning, and the error. **Corpus prose is NEVER reproduced.** |
| 13 | Declarations | Rule 3(2) declaration (no other SLP filed) + Rule 5 declaration (true copies). Verbatim from Rule (public domain). |
| 15 | AOR Certificate | Order IV Rule 1(c) — verbatim Rule recitation; placeholders for name, code, signature, date. |

## Limitation computation

The skill computes limitation at draft time using:

```
limitation_window =
  if (certificate_of_fitness_under_Art_134A_was_refused):
    60 days from date of refusal
  else:
    90 days from date of impugned order
```

If the case folder shows filing beyond the window, the skill auto-includes a **Condonation of Delay application** in the output bundle, with placeholders for the explanation paragraphs (the Drafter agent authors original explanation prose from the case facts; never from corpus).

## Format reference (case-type prose)

🟡 **Place the case-type-specific format text in the file referenced below.**

```
${CLAUDE_PLUGIN_ROOT}/skills/slp-civil-draft/format-from-user.md
```

The user pastes their preferred canonical SLP-Civil format (their own drafting style for connective phrasing, paragraph numbering, prayer wording variants) into this file. The Drafter agent uses it as a style reference, not as a content source.

**DO NOT assume language. Fail-stop until `format-from-user.md` exists.**

The plugin's own SKILL files contain ONLY: statutory recitations, structural section headers, placeholders, and authored-fresh connective skeleton. No verbatim drafted prose from any external source has been transcribed.

## Hard rules (in addition to those inherited)

1. **Article 136 invocation must be substantively pleaded.** Mere recital of the article is insufficient under Pritam Singh v. State (AIR 1950 SC 169) line of authority. The skill produces a placeholder paragraph that the Drafter agent fills with the case-specific "substantial question of law / gross injustice" formulation.
2. **AOR Certificate language is verbatim from Rule.** The skill does not paraphrase Order IV Rule 1(c); it recites it. The AOR's name, code, signature, and date are placeholders.
3. **Synopsis ≤ 3 pages; List of Dates is a chronological table, not narrative prose.** Registry returns longer Synopses for re-filing.
4. **Annexure marker is `P-N`, not `Annexure-N` or `A-N`.** SC Registry convention; HC conventions do not apply.
5. **Where the impugned order is from a Bench other than a High Court (e.g., tribunal / Armed Forces Tribunal / NCDRC / etc.), the Cause Title's parenthetical arising-out-of line is adjusted accordingly.** The Format agent handles this branching.
6. **Currency of statute:** any reference to the old criminal codes (CrPC / IEA / IPC) must use the dual-citation pattern from encoding-rules.md Rule 9 (BNSS / BSA / BNS with parenthetical fallback). For pure Civil SLPs the criminal-code currency rule rarely applies.
7. **Drafted prose anti-fabrication:** the Drafter agent never invents facts. Every fact, every annexure reference, every date traces to the user-supplied case folder, verified by the Verifier agent before refinement.

## Falsification triggers

- Registry rejects the petition on format grounds → format-from-user.md needs amendment; raise a `FORMAT.FAIL` flag in the audit log.
- AOR Certificate language differs from the Rule recitation → load-bearing bug; halt all drafts and patch the base.
- Limitation computation produces a negative window or a date pre-impugned-order → date-parsing bug; halt and patch.

## Provenance

Patterns encoded in this file trace to:
- Constitution of India, Article 136
- Supreme Court Rules, 2013 — Order XXI (Civil SLP), Order IV (AOR), Schedule Form 28
- SC Registry Practice Directions (Synopsis / List of Dates / Annexure prefixing)
- Limitation Act, 1963 + Article 133 of the Constitution
- Cross-validation report `validation-slp.md` (Phase 03 of the India-Legal Corpus Pipeline)

No drafted prose has been transcribed from the corpus or from any third-party advocate's drafts. The Drafter agent authors fresh case-specific prose at runtime from the user-supplied case folder.

---

## Status: SKELETON v0.0.1 — 2026-05-15

This is the SKILL.md skeleton authored at Sprint 1 Day 1. Pending work before v0.1.0-alpha:

- [ ] `format-from-user.md` template page with placeholders for the user's preferred SLP-Civil format
- [ ] Drafter agent SLP-Civil branch in `agents/drafter/drafter.md`
- [ ] Verifier agent SC-specific checks (AOR Certificate verbatim match, annexure prefix `P-N`, limitation window sanity, etc.)
- [ ] Worked-example case-folder template (placeholders only) under `examples/slp-civil-example/`
- [ ] Quality gate pass per `05-quality-gates.md` of the corpus pipeline

These will be ticked off across Sprint 1 (Days 5-7 of HC summer vacation 2026).
