---
name: curative-petition-draft
description: Draft a Curative Petition before the Supreme Court of India under the jurisprudence laid down in Rupa Ashok Hurra v. Ashok Hurra (2002) 4 SCC 388, read with Order XLVIII of the Supreme Court Rules, 2013. Filed AFTER a Review Petition has been dismissed, on the narrow grounds of (a) violation of principles of natural justice or (b) judge bias / apprehension of bias. The last available remedy within the Supreme Court. Auto-fires on "draft curative petition" or "curative sc" or "rupa hurra petition".
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Curative Petition — Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_sc_pleading_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: CURATIVE PETITION
case_short_code: CP (or Curative)
jurisprudential_authority: |
  Rupa Ashok Hurra v. Ashok Hurra (2002) 4 SCC 388 (Constitution Bench)
  — the foundational decision establishing the Curative Petition as the
  Supreme Court's residual mechanism to prevent miscarriage of justice
  AFTER dismissal of a Review Petition.
sc_rules_order: Order XLVIII of the Supreme Court Rules, 2013
inherent_powers: |
  The Curative Petition jurisdiction is exercised in the inherent
  plenary power of the Supreme Court under Article 142 read with
  Article 145 of the Constitution of India.
jurisdiction_line: |
  CIVIL APPELLATE JURISDICTION
  (or CRIMINAL APPELLATE JURISDICTION, mirroring the original proceeding)
statutory_opening: |
  CURATIVE PETITION UNDER ORDER XLVIII OF THE SUPREME COURT RULES, 2013
  READ WITH ARTICLE 142 OF THE CONSTITUTION OF INDIA AND THE INHERENT
  POWERS OF THIS HON'BLE COURT AS RECOGNISED IN RUPA ASHOK HURRA v.
  ASHOK HURRA (2002) 4 SCC 388
limitation_period: |
  No statutory limitation. Filed as soon as the ground for curative
  intervention crystallises (typically after dismissal of the Review
  Petition). Substantial delay must be explained in a Condonation of
  Delay application or in the Petition body itself.
mandatory_pre_conditions:
  - review_petition_dismissed: |
      "A Review Petition arising from the same judgment / order has
       been dismissed by this Hon'ble Court on <DD.MM.YYYY> in [Review
       Petition Case Number]."
       (Curative is NOT available if Review has not been filed and
        dismissed. The skill halts if the case folder does not show
        a dismissed Review.)
  - senior_advocate_certification: |
      Per Rupa Ashok Hurra (para 51): the Curative Petition must be
      certified by a SENIOR ADVOCATE as containing a substantial
      ground for curative intervention falling within the narrow
      Rupa Hurra parameters. This certification is mandatory.
grounds_for_curative_intervention:
  - violation_of_natural_justice: |
      "The Petitioner was not heard or was inadequately heard before
       the impugned judgment / order was passed, in violation of the
       principles of natural justice (audi alteram partem)."
       The ground must point to a SPECIFIC procedural defect — not
       a substantive disagreement with the judgment.
  - judge_bias_or_apprehension_of_bias: |
      "There existed circumstances raising a reasonable apprehension
       of bias on the part of the Hon'ble Judge(s) who passed the
       impugned judgment, which circumstances were not within the
       knowledge of the Petitioner at the time of the original
       proceeding / Review Petition."
       The ground must point to a SPECIFIC fact establishing the
       apprehension (e.g., a financial connection / relationship /
       prior expressed view that the Petitioner could not have
       known of earlier).
  - other_substantial_curative_ground: |
      "Any other ground showing that, absent curative intervention,
       the judgment will perpetuate a manifest miscarriage of justice."
       This third limb is read NARROWLY in subsequent jurisprudence
       (e.g., Yakub Memon v. State of Maharashtra (2015) 9 SCC 552).
       The skill flags any ground in this limb for senior-advocate
       certification scrutiny.
mandatory_certificates:
  - "Certification by a Senior Advocate that the Petition contains a substantial ground for curative intervention (Rupa Ashok Hurra para 51) — VERBATIM CERTIFICATE BLOCK with placeholder for the Senior Advocate's name, registration number, signature, and date"
  - "Advocate-on-Record Certificate under Order IV Rule 1(c) of the SC Rules 2013"
  - "A copy of the order of dismissal of the Review Petition (Annexure P-1)"
  - "A copy of the original judgment / order under challenge (Annexure P-2)"
chamber_procedure: |
  Under Order XLVIII Rule 4 of the SC Rules 2013, the Curative Petition
  is CIRCULATED to the same Bench (where practicable) that passed the
  original judgment, AND to the three senior-most Judges of the Supreme
  Court. If a majority of this circulated Bench is of the opinion that
  the Petition deserves consideration, ONLY THEN is it listed for hearing
  in chambers (without oral arguments, unless the Court directs otherwise).
accompanying_applications:
  - condonation_of_delay         # if filed substantially after Review dismissal
  - stay_of_operation            # of the judgment under curative challenge
  - exemption_from_filing_certified_copy
typical_annexure_order:
  - P-1: Certified copy of the order dismissing the Review Petition
  - P-2: Certified copy of the original judgment / order under curative challenge
  - P-3: Certified copy of the pleadings before this Hon'ble Court in the original proceeding
  - P-4: Senior Advocate's separate certification (alternatively included as a Certificate Block within the Petition body)
  - P-5: Documents establishing the violation of natural justice / apprehension of bias / other ground
  - P-Subsequent: support material
```

## Section-by-section structure

| # | Section | Curative-Petition specifics |
|---|---|---|
| 3 | Synopsis + List of Dates | Synopsis identifies the original judgment, the Review dismissal, and the precise curative ground invoked. List of Dates runs from the original proceeding through the Review dismissal. |
| 4 | Cause Title | Mirrors original. Adds: `(Curative Petition arising out of dismissal of Review Petition (No. _____ of [Year]) dated <DD.MM.YYYY>, which Review Petition itself arose from the judgment / order dated <DD.MM.YYYY> passed in [Original Case Type & Number])`. |
| 7 | Statement of Facts | Brief, narrowly focused on the curative ground. Assumes Court's familiarity with the underlying record. |
| 9 | Grounds | Each ground MUST fall within Rupa Hurra parameters — natural justice violation OR judge bias OR other substantial curative ground. The skill produces three placeholder slots; Drafter authors fresh prose only for those invoked. |
| 11 | Main Prayer | "Reopen the judgment / order dated <DD.MM.YYYY> and pass such orders as are necessary to prevent the miscarriage of justice that would otherwise result." |
| 12 | Interim Prayer | Stay of operation of the judgment under curative challenge, pending disposal. |

## Hard rules

1. **Review Petition dismissal is a hard pre-condition.** The Curative Petition CANNOT be filed unless a Review Petition has been filed and dismissed against the same judgment. The skill halts if the case folder does not contain a Review dismissal order.
2. **Grounds are limited to the Rupa Hurra parameters.** Any ground that does not fall within natural-justice-violation / judge-bias / other-substantial-curative-ground is liable to summary dismissal. The Drafter enforces the three-limb framing.
3. **Senior Advocate certification is mandatory.** Per Rupa Hurra para 51, a Senior Advocate must certify that the Petition contains a substantial ground for curative intervention. The skill produces a placeholder Certificate Block; the AOR must arrange Senior Advocate engagement before filing.
4. **AOR Certificate verbatim** as in SLPs.
5. **Annexure prefix `P-N`.**
6. **Listed in chambers, no oral arguments by default.** The Petition is drafted as a written submission complete in itself; the Drafter authors a complete written argument within the Grounds section, anticipating that there will be no oral hearing.
7. **Drafted prose anti-fabrication.** Every claim of natural-justice violation or bias must be supported by a specific fact in the case folder with a citation to the supporting annexure.

## Format reference

🟡 **Place the case-type-specific format text in:**

```
${CLAUDE_PLUGIN_ROOT}/skills/curative-petition-draft/format-from-user.md
```

Fail-stop until file exists.

## Provenance

- Constitution of India, Articles 142, 144, 145
- Supreme Court Rules, 2013 — Order XLVIII, Order IV
- Rupa Ashok Hurra v. Ashok Hurra (2002) 4 SCC 388 (Constitution Bench)
- Yakub Memon v. State of Maharashtra (2015) 9 SCC 552 (narrow reading of the "other ground" limb)

Case-law cited as authority only; no prose lifted. The Petition's own grounds are authored fresh.

---

## Status: SKELETON v0.0.1 — 2026-05-15

Pending:
- [ ] `format-from-user.md` template
- [ ] Drafter Rupa-Hurra three-limb branching
- [ ] Senior Advocate Certificate Block design
- [ ] Quality gate pass
