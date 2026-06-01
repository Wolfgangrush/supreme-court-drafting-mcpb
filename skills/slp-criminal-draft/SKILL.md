---
name: slp-criminal-draft
description: Draft a Special Leave Petition (Criminal) before the Supreme Court of India under Article 136 of the Constitution read with Order XXII of the Supreme Court Rules, 2013. Produces .docx containing Synopsis + List of Dates + Main Petition + Index + List of Annexures + AOR Certificate + Affidavit + (optional) Suspension of Sentence Application + (optional) Bail Application. Auto-fires on "draft slp criminal" or "draft special leave petition criminal" or "criminal slp".
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Special Leave Petition (Criminal) — Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_sc_pleading_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: SPECIAL LEAVE PETITION (CRIMINAL)
case_short_code: SLP(Crl)
sc_rules_order: Order XXII of the Supreme Court Rules, 2013
form_reference: Form 32 of the Supreme Court Rules, 2013
constitutional_authority: Article 136 of the Constitution of India
jurisdiction_line: CRIMINAL APPELLATE JURISDICTION
statutory_opening: |
  SPECIAL LEAVE PETITION (CRIMINAL) UNDER ARTICLE 136 OF THE
  CONSTITUTION OF INDIA READ WITH ORDER XXII OF THE
  SUPREME COURT RULES, 2013
limitation_period_days: 90
limitation_period_days_special: |
  (i) 90 days from date of judgment / order sought to be appealed against
  (ii) 60 days if certificate of fitness under Article 134A has been refused by the High Court
  (iii) 30 days where the SLP arises out of a Tribunal order (case-type specific; verify with AOR)
limitation_source: |
  Article 134 of the Constitution of India read with the Limitation Act, 1963
  and Order XXII Rule 1(1) of the Supreme Court Rules, 2013
mandatory_declarations:
  - rule: "Rule 2(2) of Order XXII, SC Rules 2013"
    content: "No other petition seeking leave to appeal has been filed against the impugned judgment / order."
  - rule: "Rule 4 of Order XXII, SC Rules 2013"
    content: "The annexures filed are true copies of pleadings or documents that formed part of the record in the Court below."
mandatory_certificates:
  - "Advocate-on-Record Certificate under Order IV Rule 1(c) of the SC Rules 2013"
  - "Synopsis and List of Dates (SC Registry Practice Directions)"
dual_citation_required: true
dual_citation_note: |
  Where the impugned order applies the Code of Criminal Procedure 1973 (CrPC),
  the Indian Penal Code 1860 (IPC), or the Indian Evidence Act 1872 (IEA),
  the SLP must use the dual-citation pattern: cite the current statute
  (BNSS / BNS / BSA) with parenthetical fallback to the corresponding old
  section, where the offence is registered before 1 July 2024 OR where
  the trial was conducted under the old code.

  Example:
    "Section 482 of the Bharatiya Nagarik Suraksha Sanhita 2023
    (corresponding to Section 528 of the Code of Criminal Procedure 1973,
    applicable where the prosecution was instituted prior to 1 July 2024)"
accompanying_applications:
  - suspension_of_sentence        # where the petitioner is in custody and seeks suspension
  - bail_application              # standalone bail application accompanying the SLP
  - condonation_of_delay          # where filed beyond the limitation window
  - exemption_from_filing_certified_copy
  - exemption_from_filing_official_translation  # where impugned order is in regional language
  - permission_to_appear_in_person  # where Petitioner appears in person
typical_annexure_order:
  - P-1: Certified copy of the impugned judgment / order of the High Court
  - P-2: Copy of the trial court judgment (where applicable)
  - P-3: Copy of the FIR
  - P-4: Copy of the chargesheet
  - P-5: Copy of the depositions of material witnesses (often Colly)
  - P-Subsequent: documents supporting individual grounds
```

## Section-by-section structure

The universal section order from `_sc_pleading_base` applies. SLP-Criminal-specific notes:

| # | Section | SLP-Criminal specifics |
|---|---|---|
| 3 | Synopsis + List of Dates | Mandatory. Synopsis ≤ 3 pages. List of Dates begins with FIR registration date, runs through chargesheet, trial court judgment, HC judgment, ending with impugned order. |
| 4 | Cause Title | `IN THE SUPREME COURT OF INDIA / CRIMINAL APPELLATE JURISDICTION / Special Leave Petition (Criminal) No. _____ of [Year] / (Arising out of impugned judgment / order dated <DD.MM.YYYY> passed by the Hon'ble High Court of [   ] at [   ] in [Case Type & Number])` |
| 7 | Statement of Facts | Chronological from FIR through HC judgment. Custody status of accused (in jail / on bail / on anticipatory bail) is stated in the opening paragraph. |
| 8 | Questions of Law | At least one substantial question of law warranting interference under Art. 136. The "gross injustice" limb is independently available where the case turns on facts (Pritam Singh v. State AIR 1950 SC 169 line). |
| 9 | Grounds | Authored fresh from the facts. Common SLP-Criminal grounds include: (i) erroneous appreciation of evidence, (ii) non-consideration of material defence evidence, (iii) reversal of acquittal without strong reasons (where applicable), (iv) sentencing disproportionality, (v) violation of fair-trial procedure. **Each ground is authored fresh; corpus prose is NEVER reproduced.** |
| 10 | Grounds for Interim Relief | Where the petitioner is in custody: grounds for suspension of sentence and grant of bail pending the SLP. Where the petitioner is the State / complainant appealing acquittal: grounds for stay of release / interim custody arrangements. |
| 11 | Main Prayer | Grant of leave to appeal + setting aside the impugned judgment / order. |
| 12 | Interim Prayer | Suspension of sentence + grant of bail pending disposal of the SLP (where applicable). |
| 13 | Declarations | Rule 2(2) declaration (no other SLP filed) + Rule 4 declaration (true copies). Verbatim from Rule. |
| 15 | AOR Certificate | Order IV Rule 1(c) — verbatim Rule recitation; placeholders for AOR name, code, signature, date. |

## Limitation computation

```
limitation_window =
  if (impugned_order_is_tribunal_specific_origin):
    case_type_specific (verify; usually 30-60 days)
  elif (certificate_of_fitness_under_Art_134A_was_refused):
    60 days from date of refusal
  else:
    90 days from date of impugned order
```

If the case folder shows filing beyond the window, the skill auto-includes a **Condonation of Delay application** in the output bundle, with placeholders for explanation paragraphs (Drafter authors original explanation prose from case facts; never from corpus).

## Format reference (case-type prose)

🟡 **Place the case-type-specific format text in the file referenced below.**

```
${CLAUDE_PLUGIN_ROOT}/skills/slp-criminal-draft/format-from-user.md
```

User pastes their preferred SLP-Criminal style references. Drafter uses for style alignment only, not for content. **Fail-stop until `format-from-user.md` exists.**

## Hard rules (in addition to those inherited)

1. **Custody status is foregrounded.** The Statement of Facts opens by stating whether the accused-petitioner is in custody, on bail, or on anticipatory bail, with the date and the court that granted bail (if any).
2. **Dual citation discipline is mandatory.** Every reference to CrPC / IPC / IEA must be paired with the corresponding BNSS / BNS / BSA section (or vice versa) per the dual-citation pattern in the case-type metadata above. The Format agent enforces this; the Verifier flags any single-citation reference for review.
3. **AOR Certificate language is verbatim from Rule.** Same as Civil SLP.
4. **Annexure marker is `P-N`.** SC Registry convention; HC conventions do not apply.
5. **Where the SLP is against acquittal**, the grounds must address the higher threshold for reversing an acquittal (the appellate court's reluctance to disturb a considered acquittal absent perversity / illegality) — Drafter places a placeholder reminder for this point; advocate fills in the substantive ground from the facts.
6. **Where the impugned order is from a Bench other than a High Court** (e.g., AFT, NCDRC for criminal-track if applicable, criminal contempt by HC), the Cause Title's arising-out-of parenthetical is adjusted accordingly.
7. **Drafted prose anti-fabrication:** every fact, every annexure reference, every date traces to the user-supplied case folder, verified by the Verifier before refinement. Case citations are NEVER generated from training memory — every citation traces to the user's citation list, or appears as `[CITATION NEEDED]`.

## Falsification triggers

- Registry rejects on format grounds → `format-from-user.md` needs amendment; raise `FORMAT.FAIL` in audit log.
- AOR Certificate language differs from Rule recitation → load-bearing bug; halt all drafts and patch base.
- Limitation computation produces a negative window → date-parsing bug; halt and patch.
- Single-citation (only CrPC, no BNSS pair, or vice versa) detected in output → Verifier flags for dual-citation completion.

## Provenance

Patterns encoded in this file trace to:
- Constitution of India, Article 136, Article 134, Article 134A
- Supreme Court Rules, 2013 — Order XXII (Criminal SLP), Order IV (AOR), Schedule Form 32
- Limitation Act 1963
- Bharatiya Nagarik Suraksha Sanhita 2023 (BNSS) and the Code of Criminal Procedure 1973 (transitional)
- SC Registry Practice Directions
- Cross-validation report `validation-slp.md` (Phase 03 of the India-Legal Corpus Pipeline)
- Pritam Singh v. State AIR 1950 SC 169 (citation for the "substantial question of law / gross injustice" jurisprudence under Art 136; quoted only as authority, no prose lifted)

No drafted prose has been transcribed from the corpus or from any third-party advocate's drafts.

---

## Status: SKELETON v0.0.1 — 2026-05-15

Authored Sprint 1 Day 1. Pending pre-ship:
- [ ] `format-from-user.md` template page
- [ ] Drafter agent SLP-Criminal branch in `agents/drafter/drafter.md`
- [ ] Verifier SC-specific checks (dual-citation enforcement, custody-status presence, AOR cert verbatim, annexure prefix)
- [ ] Worked-example case-folder template under `examples/slp-criminal-example/` (placeholders only)
- [ ] Quality gate pass per `05-quality-gates.md`
