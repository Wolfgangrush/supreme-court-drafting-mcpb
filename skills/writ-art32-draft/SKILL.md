---
name: writ-art32-draft
description: Draft a Writ Petition before the Supreme Court of India under Article 32 of the Constitution read with Order XXXVIII of the Supreme Court Rules, 2013. For direct enforcement of fundamental rights. Produces .docx containing Synopsis + List of Dates + Main Petition + Index + List of Annexures + AOR Certificate + Affidavit + (optional) Stay Application + (optional) Habeas Corpus prayer where the case requires. Auto-fires on "draft writ article 32" or "draft sc writ petition" or "article 32 writ".
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Writ Petition under Article 32 — Draft Skill

Extends: `${CLAUDE_PLUGIN_ROOT}/skills/_sc_pleading_base/SKILL.md`
Common rules: `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md`

## Case-type metadata

```yaml
case_type_line: WRIT PETITION (CIVIL/CRIMINAL)
case_short_code: WP(C)  # or WP(Crl) for habeas corpus / quashing of criminal action
sc_rules_order: Order XXXVIII of the Supreme Court Rules, 2013
constitutional_authority: |
  Article 32 of the Constitution of India
  (read with Articles 14, 19, 20, 21, 22, 25, and other fundamental rights
   provisions invoked in the case, as applicable)
jurisdiction_line: |
  CIVIL ORIGINAL JURISDICTION
  (or CRIMINAL ORIGINAL JURISDICTION for Habeas Corpus / quashing of FIR)
statutory_opening: |
  WRIT PETITION (CIVIL / CRIMINAL) UNDER ARTICLE 32 OF THE
  CONSTITUTION OF INDIA SEEKING [Mandamus / Certiorari / Habeas Corpus /
  Prohibition / Quo Warranto / Declaratory Writ in the nature of...]
  FOR ENFORCEMENT OF FUNDAMENTAL RIGHTS GUARANTEED UNDER
  ARTICLE(S) [14 / 19 / 20 / 21 / etc.] OF THE CONSTITUTION OF INDIA
limitation_period: |
  No statutory limitation prescribed for Art 32 (unlike Art 226, where state-specific HC rules may impose limits).
  However, the Supreme Court applies the doctrine of delay and laches —
  "the writ jurisdiction is to be invoked promptly; unreasonable delay
   may itself be a ground for refusal." (Tilokchand Motichand v. H.B. Munshi (1969) 1 SCC 110)
  The skill places a placeholder asking the Petitioner to disclose the
  cause-of-action date and explain any gap exceeding 6 months.
mandatory_paragraphs:
  - no_alternative_efficacious_remedy: |
      "The Petitioner has no other equally efficacious remedy available
       to enforce the fundamental right(s) invoked except by way of
       the present petition under Article 32 of the Constitution of India."
      (This is not strictly required under Art 32 — unlike Art 226 — but the
       SC discourages Art 32 petitions where an Art 226 remedy was available
       and not exhausted. The skill includes a placeholder paragraph addressing
       the choice of Art 32 over Art 226 in the case at hand.)
  - no_similar_petition_filed: |
      "No other writ petition seeking similar relief has been filed
       by the Petitioner before this Hon'ble Court or any other Court."
  - locus_standi: |
      For non-aggrieved Petitioners (PIL-style Art 32), a credentials
      paragraph per State of Uttaranchal v. Balwant Singh Chaufal (2010) 3 SCC 402.
mandatory_certificates:
  - "Advocate-on-Record Certificate under Order IV Rule 1(c) of the SC Rules 2013"
  - "Synopsis and List of Dates (SC Registry Practice Directions)"
  - "If filed as PIL: Disclosure of Petitioner's credentials and source of information (per Balwant Singh Chaufal)"
accompanying_applications:
  - stay_application                              # standard
  - ad_interim_mandamus_application               # for urgent positive-duty relief
  - exemption_from_filing_certified_copy
  - permission_to_appear_in_person                # if appearing without AOR — actually NOT permitted in SC except in narrow cases; verify
typical_annexure_order:
  - P-1: Government Order / Notification / Action being challenged
  - P-2: Representation(s) made by the Petitioner to the Authority
  - P-3: Replies received (if any)
  - P-4: Authority cited in the Petitioner's case (orders of subordinate courts/authorities, where relevant)
  - P-Subsequent: documentary support for individual grounds
```

## Reliefs available under Article 32

Article 32(2) empowers the Supreme Court to issue directions, orders, or writs, including writs in the nature of:

1. **Habeas Corpus** — direct production of a person in unlawful detention.
2. **Mandamus** — direction to a public authority to perform a statutory / constitutional duty.
3. **Prohibition** — restraint on an inferior court / authority exceeding jurisdiction.
4. **Certiorari** — quashing of an order of an inferior court / authority that is illegal / without jurisdiction / in violation of natural justice.
5. **Quo Warranto** — inquiry into the legal authority by which a public office is held.

The skill's Cause Title and Statutory Opening specify which writ(s) is sought; multiple writs may be sought in one petition where the relief requires it.

## Section-by-section structure

| # | Section | Art 32 specifics |
|---|---|---|
| 3 | Synopsis + List of Dates | Mandatory. Synopsis emphasises the fundamental right violation. List of Dates begins with the impugned action / notification. |
| 4 | Cause Title | Original jurisdiction (Civil or Criminal). No arising-out-of parenthetical (Art 32 is direct). |
| 7 | Statement of Facts | Chronology of the impugned action + the Petitioner's status + the locus standi (especially for PIL-Art 32). |
| 8 | Questions of Law | Each question identifies (a) the fundamental right invoked, (b) the impugned action, (c) the alleged violation. |
| 9 | Grounds | Each ground links the impugned action to the violation of a specific fundamental right (Art 14 / 19 / 20 / 21 / etc.) with authored-fresh legal reasoning. |
| 10 | Grounds for Interim Relief | Where stay / ad-interim mandamus is sought. |
| 11 | Main Prayer | The specific writ(s) sought, in writ-form language (e.g., "Issue a writ of mandamus directing Respondent No. 1 to..."). |
| 12 | Interim Prayer | Stay / ad-interim mandamus / production of detenu (Habeas Corpus interim). |

## Hard rules (in addition to those inherited)

1. **Fundamental-right limb mandatory.** Every Art 32 petition must invoke a specific fundamental right under Part III of the Constitution. The skill produces a `[FUNDAMENTAL RIGHT INVOKED]` placeholder at the very top of the Statutory Opening; Drafter fails the draft if this is empty in the case folder.
2. **Habeas Corpus variant has its own structure.** Where the case is Habeas Corpus, the Cause Title carries `CRIMINAL ORIGINAL JURISDICTION`, the prayer seeks production of the detenu, and the Petition Proper opens with the date of detention + the place of detention + the authority detaining. The skill auto-branches when the case folder marks the case as Habeas Corpus.
3. **PIL-Art 32 disclosure mandatory.** Where the Petitioner is not personally aggrieved (PIL-mode), the credentials paragraph per State of Uttaranchal v. Balwant Singh Chaufal (2010) 3 SCC 402 is auto-included. The Petitioner's credentials + source of information are placeholders to be filled.
4. **AOR Certificate language is verbatim from Rule.** Same as SLPs.
5. **Annexure marker is `P-N`.** SC convention.
6. **Where the Petitioner has an Art 226 remedy available**, the Petition includes a paragraph explaining the choice of Art 32 over Art 226 (e.g., the right invoked is one of the unenumerated rights under Art 21 where the SC has previously developed the doctrine, or the case raises an inter-State element where the HC remedy is fragmented). This paragraph is authored fresh.
7. **Drafted prose anti-fabrication:** every fact, every annexure reference, every date traces to the user-supplied case folder. Case citations NEVER generated from training memory.

## Format reference (case-type prose)

🟡 **Place the case-type-specific format text in the file referenced below.**

```
${CLAUDE_PLUGIN_ROOT}/skills/writ-art32-draft/format-from-user.md
```

User pastes preferred Art-32 style. Drafter uses for style alignment only. Fail-stop until file exists.

## Falsification triggers

- No fundamental right invoked in case folder → Drafter halts; case folder needs amendment.
- Registry rejects on format grounds → `format-from-user.md` needs amendment.
- AOR Certificate language differs from Rule → load-bearing bug.

## Provenance

Patterns encoded in this file trace to:
- Constitution of India, Articles 14, 19, 20, 21, 22, 25, 32
- Supreme Court Rules, 2013 — Order XXXVIII (Writ Petitions), Order IV (AOR)
- State of Uttaranchal v. Balwant Singh Chaufal (2010) 3 SCC 402 (PIL disclosure jurisprudence)
- Tilokchand Motichand v. H.B. Munshi (1969) 1 SCC 110 (delay and laches in writ jurisdiction)
- Cross-validation report `validation-writ.md` (Phase 03 of the India-Legal Corpus Pipeline)
- Cross-validation report `validation-petition.md` (mandatory paragraphs reference)

No drafted prose has been transcribed from the corpus.

---

## Status: SKELETON v0.0.1 — 2026-05-15

Pending pre-ship:
- [ ] `format-from-user.md` template
- [ ] Drafter agent Art-32 branch
- [ ] Habeas Corpus sub-branch testing
- [ ] PIL-mode credentials-paragraph testing
- [ ] Quality gate pass
