---
name: transfer-petition-draft
description: Draft a Transfer Petition before the Supreme Court of India under Section 25 of the Code of Civil Procedure 1908 (Civil) or Section 406 of the Bharatiya Nagarik Suraksha Sanhita 2023 (Criminal) — corresponding to Section 406 of the Code of Criminal Procedure 1973. Produces .docx for transfer of a case, suit, or proceeding from one State High Court or subordinate court to another, or from one State to another. Auto-fires on "draft transfer petition" or "transfer petition sc" or "tp draft".
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Transfer Petition — Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_sc_pleading_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: TRANSFER PETITION (CIVIL/CRIMINAL)
case_short_code: TP(C)  # or TP(Crl) for criminal
statutory_authority_civil: |
  Section 25 of the Code of Civil Procedure, 1908
  (Power of the Supreme Court to transfer suits, etc., from one State to another)
statutory_authority_criminal: |
  Section 406 of the Bharatiya Nagarik Suraksha Sanhita, 2023
  (corresponding to Section 406 of the Code of Criminal Procedure, 1973 —
   applicable where the underlying proceeding was instituted prior to 1 July 2024)
sc_rules_reference: |
  Supreme Court Rules, 2013 — practice as governed by Order LVI (Miscellaneous Petitions)
  and the Registry Practice Directions on Transfer Petitions
jurisdiction_line: |
  CIVIL ORIGINAL JURISDICTION
  (or CRIMINAL ORIGINAL JURISDICTION for criminal TPs)
statutory_opening_civil: |
  TRANSFER PETITION (CIVIL) UNDER SECTION 25 OF THE CODE OF CIVIL
  PROCEDURE, 1908 FOR TRANSFER OF [Case Type & Number] PENDING BEFORE
  THE [Court Name] AT [Place], [State] TO THE [Receiving Court Name] AT
  [Receiving Place], [Receiving State]
statutory_opening_criminal: |
  TRANSFER PETITION (CRIMINAL) UNDER SECTION 406 OF THE BHARATIYA
  NAGARIK SURAKSHA SANHITA, 2023 (corresponding to Section 406 of the
  Code of Criminal Procedure, 1973) FOR TRANSFER OF [Case Type & Number]
  PENDING BEFORE THE [Court Name] AT [Place], [State] TO THE [Receiving
  Court Name] AT [Receiving Place], [Receiving State]
limitation_period: |
  No statutory limitation. The Transfer Petition is filed when the
  cause for transfer arises. Delay-and-laches applies if the cause
  for transfer crystallised long before the petition.
mandatory_paragraphs:
  - underlying_proceeding_status: |
      "The proceeding sought to be transferred is currently at the
       stage of [Stage], next listed for [Purpose] on <DD.MM.YYYY>
       before the Hon'ble [Court Name] at [Place]."
  - grounds_for_transfer: |
      Common grounds (case-specific factual basis required):
      (i) The Petitioner is unable to attend the existing court due to
          personal hardship, medical reasons, or distance.
      (ii) There is a reasonable apprehension that the Petitioner will
           not receive a fair trial at the existing court.
      (iii) The convenience of witnesses and parties requires transfer.
      (iv) Concurrent / connected proceedings are pending in the
           receiving court and consolidation is necessary in the
           interest of justice.
      Each ground requires SUPPORTING FACTS — Drafter authors fresh
      from the case folder; never lifted from corpus.
mandatory_certificates:
  - "Advocate-on-Record Certificate under Order IV Rule 1(c) of the SC Rules 2013"
  - "Synopsis and List of Dates (SC Registry Practice Directions)"
  - "Affidavit by the Petitioner verifying contents"
accompanying_applications:
  - stay_of_existing_proceedings        # to prevent further proceedings pending transfer
  - exemption_from_filing_certified_copy  # of pleadings before existing court
  - condonation_of_delay                # rare, only if extreme delay needs explanation
typical_annexure_order:
  - P-1: Copy of the plaint / complaint / charge-sheet initiating the underlying proceeding
  - P-2: Copy of the most recent order in the underlying proceeding (showing case stage)
  - P-3: Documents supporting the ground for transfer (medical certificate / police complaint / hardship affidavit / etc.)
  - P-4: Receiving court's confirmation of caseload / consolidation interest (if relevant)
  - P-Subsequent: documentary support for individual grounds
```

## Civil vs Criminal — branching

The skill branches at the case-folder level. The user marks the case as `civil` or `criminal` in the case folder's CLAUDE.md (or via the Reader agent's detection).

- **Civil branch:** Section 25 CPC. The Supreme Court considers (a) convenience of the parties, (b) interest of justice, (c) avoidance of multiplicity of proceedings, (d) substantial connection between the relief sought and the receiving forum.
- **Criminal branch:** Section 406 BNSS (Section 406 CrPC). The Supreme Court is empowered to transfer any case or appeal from one High Court to another, or from one criminal court in one State to a criminal court in another. The threshold is "expedient for the ends of justice" — interpreted by jurisprudence including Maneka Sanjay Gandhi v. Rani Jethmalani (1979) 4 SCC 167 and subsequent decisions.

The criminal branch additionally requires:
- Identification of the offence(s) and statute(s) involved (with the dual-citation pattern where the old codes are referenced)
- Bail status of the accused-petitioner
- A specific articulation of why a fair trial is unlikely at the existing court (if that is the ground)

## Section-by-section structure

| # | Section | Transfer Petition specifics |
|---|---|---|
| 4 | Cause Title | Original jurisdiction (Civil or Criminal). No arising-out-of parenthetical. |
| 7 | Statement of Facts | Identifies the underlying proceeding, its current stage, the parties, and the cause for transfer. |
| 8 | Questions of Law | Usually a single question: whether the transfer sought is expedient in the interest of justice / for convenience of parties. |
| 9 | Grounds | Each ground = a factual basis + a legal proposition. Authored fresh. |
| 11 | Main Prayer | Specific direction: transfer of [Case Type & Number] from [existing court] to [receiving court]. |
| 12 | Interim Prayer | Stay of further proceedings in the existing court pending disposal of the Transfer Petition. |

## Hard rules

1. **Receiving court must be named with specificity.** "Transfer to any court in [State]" is insufficient; the receiving court must be a named, jurisdictionally competent court. The skill produces a `[RECEIVING COURT NAME REQUIRED]` placeholder; Drafter halts if blank.
2. **Dual citation for criminal TPs.** Where the underlying proceeding involves CrPC / IPC, the dual-citation pattern applies per `_drafting_common/SKILL.md`.
3. **AOR Certificate verbatim.**
4. **Annexure prefix `P-N`.**
5. **Drafted prose anti-fabrication.** Every ground traces to facts in the case folder; case citations trace to user-supplied list.

## Format reference

🟡 **Place the case-type-specific format text in:**

```
${CLAUDE_PLUGIN_ROOT}/skills/transfer-petition-draft/format-from-user.md
```

Fail-stop until file exists.

## Provenance

- Section 25 CPC 1908
- Section 406 BNSS 2023 / Section 406 CrPC 1973
- Supreme Court Rules 2013 — Order LVI, Order IV
- Maneka Sanjay Gandhi v. Rani Jethmalani (1979) 4 SCC 167 (citation for "ends of justice" threshold under criminal transfer; quoted only as authority)
- Cross-validation report `validation-petition.md` (mandatory paragraph references)

No drafted prose transcribed from corpus.

---

## Status: SKELETON v0.0.1 — 2026-05-15

Pending:
- [ ] `format-from-user.md` template
- [ ] Drafter Civil + Criminal branching
- [ ] Quality gate pass
