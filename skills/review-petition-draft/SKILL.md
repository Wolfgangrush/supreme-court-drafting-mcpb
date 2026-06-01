---
name: review-petition-draft
description: Draft a Review Petition before the Supreme Court of India under Article 137 of the Constitution read with Order XLVII of the Supreme Court Rules, 2013 and Order XLVII of the Code of Civil Procedure 1908. Filed against a Supreme Court order/judgment on the limited grounds of (a) discovery of new and important matter, (b) mistake or error apparent on the face of the record, or (c) any other sufficient reason. Auto-fires on "draft review petition sc" or "sc review" or "review of supreme court order".
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Review Petition (Supreme Court) — Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_sc_pleading_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: REVIEW PETITION
case_short_code: RP
constitutional_authority: |
  Article 137 of the Constitution of India
  (Subject to the provisions of any law made by Parliament or any
   rules made under Article 145, the Supreme Court shall have power
   to review any judgment pronounced or order made by it.)
sc_rules_order: Order XLVII of the Supreme Court Rules, 2013
procedural_authority_civil: Order XLVII Rule 1 of the Code of Civil Procedure, 1908
procedural_authority_criminal: |
  Review in criminal matters is restricted to errors apparent on the face
  of the record (P.N. Eswara Iyer v. Registrar, Supreme Court of India
  (1980) 4 SCC 680 — Constitution Bench)
jurisdiction_line: |
  CIVIL APPELLATE JURISDICTION
  (or CRIMINAL APPELLATE JURISDICTION, mirroring the order under review)
statutory_opening: |
  REVIEW PETITION UNDER ARTICLE 137 OF THE CONSTITUTION OF INDIA
  READ WITH ORDER XLVII OF THE SUPREME COURT RULES, 2013
  AND ORDER XLVII RULE 1 OF THE CODE OF CIVIL PROCEDURE, 1908
  FOR REVIEW OF THE JUDGMENT / ORDER DATED <DD.MM.YYYY> PASSED BY
  THIS HON'BLE COURT IN [Case Type & Number]
limitation_period_days: 30
limitation_source: |
  Order XLVII Rule 1(2) of the Supreme Court Rules, 2013 — "An application
  for review shall be filed within 30 days from the date of the judgment
  or order sought to be reviewed."
grounds_for_review:
  - rule: "Order XLVII Rule 1 CPC (applied to SC review by Order XLVII SC Rules 2013)"
    grounds:
      - "Discovery of new and important matter or evidence which, after the exercise of due diligence, was not within the knowledge of the Petitioner or could not be produced at the time the judgment was passed."
      - "Mistake or error apparent on the face of the record."
      - "Any other sufficient reason."
  - jurisprudential_limit: |
      "The scope of review is narrow. Review does not lie merely because
       another view is possible (Northern India Caterers (India) Ltd. v.
       Lt. Governor of Delhi (1980) 2 SCC 167). Review is not an appeal
       in disguise (Lily Thomas v. Union of India (2000) 6 SCC 224)."
hearing_procedure:
  - civil: |
      Under Order XLVII Rule 3 of the SC Rules 2013, a Review Petition
      is, AS A RULE, decided in CHAMBERS by circulation without oral hearing.
      Oral hearing is granted only by special leave of the Court.
  - criminal: |
      Under Order XLVII Rule 1(5) of the SC Rules 2013, criminal Review
      Petitions are also decided in chambers by circulation, subject to
      the limited oral hearing carved out in Mohd. Arif v. Registrar,
      Supreme Court of India (2014) 9 SCC 737 (oral hearing in chambers
      for death-sentence Review Petitions).
bench_composition: |
  Under Order XLVII Rule 1(4) of the SC Rules 2013, the Review Petition
  is heard, as far as practicable, by the SAME BENCH which passed the
  order under review. The Petition is filed and addressed accordingly.
mandatory_certificates:
  - "Advocate-on-Record Certificate under Order IV Rule 1(c) of the SC Rules 2013 (the SAME AOR who filed the original proceeding ordinarily files the review; if a different AOR is engaged, a No-Objection from the original AOR is recommended though not strictly mandatory)"
  - "Synopsis and List of Dates (SC Registry Practice Directions)"
  - "Affidavit by the Petitioner verifying contents"
  - "Certificate of Counsel as to the review being filed on legitimate grounds (Order XLVII Rule 2 SC Rules 2013) — to be appended"
accompanying_applications:
  - condonation_of_delay              # if filed beyond 30 days
  - stay_of_operation                 # of the order under review, pending disposal
  - prayer_for_oral_hearing           # request for oral hearing under the special-leave carve-out
  - exemption_from_filing_certified_copy
typical_annexure_order:
  - P-1: Certified copy of the impugned judgment / order of this Hon'ble Court (the order sought to be reviewed)
  - P-2: Certified copy of the pleadings before this Hon'ble Court in the original proceeding
  - P-3: Documents constituting the "new and important matter" (if that ground is invoked)
  - P-4: Material indicating the "error apparent on the face of the record"
  - P-Subsequent: documentary support for the "sufficient reason" ground
```

## Section-by-section structure

| # | Section | Review-Petition specifics |
|---|---|---|
| 3 | Synopsis + List of Dates | Synopsis identifies the order under review and the precise grounds for review. List of Dates includes the original judgment date prominently. |
| 4 | Cause Title | Mirrors the original case (Civil/Criminal Appellate). Adds: `(Review Petition arising out of the judgment / order dated <DD.MM.YYYY> passed by this Hon'ble Court in [Case Type & Number])`. |
| 7 | Statement of Facts | Brief; assumes the Court's familiarity with the original record. Focus on the fact-pattern relevant to the review grounds. |
| 9 | Grounds | Each ground must be expressly framed as one of (a) new evidence + due diligence, (b) error apparent on the face of the record, (c) any other sufficient reason. The skill produces a placeholder marker for each ground category; Drafter authors fresh prose for each invoked category. |
| 11 | Main Prayer | "Review and set aside / modify / recall the judgment / order dated <DD.MM.YYYY> passed in [Case Type & Number]". |
| 12 | Interim Prayer | Stay of operation of the order under review, pending disposal of the Review Petition. |

## Hard rules

1. **30-day limitation is strict.** If the case folder shows filing beyond 30 days, the skill auto-includes a Condonation of Delay application. The application must explain the delay with reference to specific dates and events.
2. **Grounds must be one of the three statutory limbs.** A Review Petition that argues "the Court was wrong on the merits" without bringing the argument within one of the three limbs is liable to dismissal. The skill enforces the three-limb framing via Drafter placeholders.
3. **No re-arguing of merits.** The Drafter is explicitly instructed not to draft a ground that reads as "the Court should have held X" without specifying which limb (new evidence / error apparent / sufficient reason) the ground falls within.
4. **Same Bench rule.** The Petition is addressed to the same Bench (where practicable). The Drafter produces a placeholder for the Bench composition; the AOR confirms or updates at filing.
5. **Counsel's Certificate** under Order XLVII Rule 2 of the SC Rules 2013 (certifying the review is filed on legitimate grounds and not as a re-argument) is mandatory — the skill produces a verbatim Rule-recitation block with placeholder for Counsel's name and signature.
6. **AOR Certificate verbatim.** As in SLPs.
7. **Annexure prefix `P-N`.**
8. **Drafted prose anti-fabrication.** Every "new matter" reference traces to a document in the case folder. The Verifier flags any claim of "new evidence" not backed by an annexed document.

## Format reference

🟡 **Place the case-type-specific format text in:**

```
${CLAUDE_PLUGIN_ROOT}/skills/review-petition-draft/format-from-user.md
```

Fail-stop until file exists.

## Provenance

- Constitution of India, Article 137
- Supreme Court Rules, 2013 — Order XLVII, Order IV
- Code of Civil Procedure 1908, Order XLVII Rule 1
- P.N. Eswara Iyer v. Registrar, Supreme Court of India (1980) 4 SCC 680
- Northern India Caterers (India) Ltd. v. Lt. Governor of Delhi (1980) 2 SCC 167
- Lily Thomas v. Union of India (2000) 6 SCC 224
- Mohd. Arif v. Registrar, Supreme Court of India (2014) 9 SCC 737
- Cross-validation reports `validation-slp.md` and `validation-petition.md`

Case-law cited as authority only; no prose lifted. The Petition's own grounds are authored fresh from the case folder.

---

## Status: SKELETON v0.0.1 — 2026-05-15

Pending:
- [ ] `format-from-user.md` template
- [ ] Drafter three-limb branching
- [ ] Counsel's Certificate block
- [ ] Quality gate pass
