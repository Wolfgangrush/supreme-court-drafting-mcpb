---
name: _sc_pleading_base
description: Universal pleading skeleton for the Supreme Court of India. Shared base referenced by every case-type-specific drafting skill in this plugin (slp-civil-draft, slp-criminal-draft, writ-art32-draft, transfer-petition-draft, review-petition-draft, curative-petition-draft). Not auto-fired by user prompts; loaded via @-reference from case-type skills.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Supreme Court Pleading — Universal Base

Every Supreme Court drafting skill in this plugin extends this base. It encodes the structural skeleton mandated by:

- The Constitution of India (Articles 32, 136, 137, 142)
- The Supreme Court Rules, 2013 (Orders XXI, XXII, XL, XLVII, XLVIII, IV, V)
- The Supreme Court Registry Practice Directions and Office Procedure Handbook

The skeleton itself is uncopyrightable (universal section headers mandated by procedural law). The placeholders are filled at runtime from a user-supplied case folder. **No drafted prose from any external source is encoded; every connective phrase is original or directly recited from statute / Rule.**

---

## 1. Universal section order (every SC pleading)

A Supreme Court pleading produced by this plugin contains the following sections in this exact order. Case-type skills (SLP / WP / Transfer / Review / Curative) override individual section content; the order does not change.

1. **COVER PAGE** — Registry-prescribed format (A4, white paper, one-side print).
2. **INDEX** — list of documents in the paperbook with page numbers.
3. **SYNOPSIS AND LIST OF DATES** — mandatory under SC Registry Practice Directions. Synopsis = case summary. List of Dates = chronological table of events.
4. **CAUSE TITLE** — Court name, jurisdiction line, statutory reference, case-type and number placeholder, party block (Petitioner v. Respondent with status in lower court).
5. **OPENING ADDRESS** — `"To, The Hon'ble Chief Justice of India and his Companion Justices."`
6. **PETITION PROPER** — opens with `"The Humble Petition of the Petitioner above-named MOST RESPECTFULLY SHOWETH:"`
7. **STATEMENT OF FACTS** — chronological narration of facts giving rise to the petition. Placeholders only.
8. **QUESTIONS OF LAW** — enumerated questions requiring the Supreme Court's intervention (mandatory for SLP and Article 32 WP).
9. **GROUNDS** — enumerated legal and factual grounds. Authored fresh; never lifted from external corpus.
10. **GROUNDS FOR INTERIM RELIEF** — where interim relief is sought (stay, suspension of sentence, ad-interim mandamus).
11. **MAIN PRAYER** — substantive relief sought.
12. **INTERIM PRAYER** — interim relief sought pending disposal of the petition.
13. **DECLARATIONS** — statutory declarations under the relevant SC Rules order (case-type specific).
14. **SIGNATURE BLOCK** — Petitioner-in-person OR Counsel for Petitioner (with `"Drawn by"`, `"Drawn on"`, `"Filed on"` markers).
15. **CERTIFICATE BY ADVOCATE-ON-RECORD** — mandatory under Order IV Rule 1(c) of the SC Rules 2013.
16. **AFFIDAVIT** — verifying the contents of the petition; sworn before a Notary / Oath Commissioner.
17. **ANNEXURE INDEX** — list of Petitioner's annexures using the SC-prescribed `P-1, P-2, P-3 ...` prefixing convention.

---

## 2. Cause Title — universal format

```
IN THE SUPREME COURT OF INDIA
[CIVIL / CRIMINAL] APPELLATE JURISDICTION

[Case Type] No. [        ] of [Year]

[(Arising out of impugned order / judgment dated <DD.MM.YYYY> passed
by the Hon'ble High Court of [    ] at [    ] in [Case Type & Number])]

  IN THE MATTER OF:

  [Petitioner Name]                                ... Petitioner
  [Status in lower court — Appellant / Petitioner / Original Plaintiff / Respondent]

                          VERSUS

  [Respondent Name]                                ... Respondent
  [Status in lower court]
```

The bracketed jurisdiction line ("Civil Appellate" or "Criminal Appellate") and the statutory reference are filled by the case-type skill.

---

## 3. Annexure marker convention

Every annexure produced under this plugin uses the SC Registry convention:

- Petitioner's annexures: `P-1`, `P-2`, `P-3`, ...
- Respondent's annexures (in counter-affidavit / reply): `R-1`, `R-2`, `R-3`, ...
- True Copy markings: each annexure carries `"True copy"` stamp placeholder.
- The Annexure Index lists each annexure with description and page span.

---

## 4. Limitation discipline (case-type specific, computed by skill)

The case-type skill computes limitation from the impugned-order date in the user-supplied case folder. The universal rule set is:

- **SLP (Civil / Criminal)** under Art. 136 — 90 days from the date of the judgment / order sought to be appealed against (60 days where a certificate of fitness has been refused) — Article 133 / 134 of the Constitution and Limitation Act 1963.
- **Writ Petition under Art. 32** — no limitation prescribed by statute, but the Court applies delay-and-laches doctrine; the skill places a placeholder for the Petitioner to disclose the period.
- **Transfer Petition** under Sec. 25 CPC / Sec. 406 BNSS — no limitation; computed from the cause for transfer.
- **Review Petition** under Order XLVII CPC read with Order XLVIII SC Rules 2013 — 30 days from the date of the order.
- **Curative Petition** (Rupa Ashok Hurra (2002) 4 SCC 388) — no statutory period; filed as soon as the ground crystallises after review dismissal.

---

## 5. Formatting (Supreme Court Registry mandate)

- **Paper:** A4 white, one-side printing.
- **Font:** Times New Roman, 14 point body text, 1.5 line spacing.
- **Margins:** 4 cm left (binding side), 2.5 cm top / bottom / right.
- **Page numbers:** centered at the bottom; the paperbook is paginated continuously.
- **Color of folder:** as prescribed by Registry for the case type (e.g., white folder for SLP Civil, blue for SLP Criminal — verified at filing).
- **Pagination of annexures:** continuous with the main petition.

These are Court Rule / Registry mandates and are encoded directly per the encoding-rules.md Rule 6 (Court Rules trump informal practice).

---

## 6. The Advocate-on-Record (AOR) Certificate — load-bearing

Under Order IV Rule 1(c) of the Supreme Court Rules, 2013, no petition / appeal can be filed or admitted unless presented through an Advocate-on-Record. The AOR Certificate is mandatory and its language is word-perfect under Rule 1(c):

> The Advocate-on-Record certifies that the petition is confined to the pleadings before the Court / Tribunal whose order is challenged and the other statutory requirements of the Supreme Court Rules 2013 have been complied with.

The skill renders the AOR Certificate block with placeholders for AOR name, code, signature, and date. **The plugin does not draft the AOR Certificate language; the language is recited verbatim from the Rule (public-domain, statutory).**

---

## 7. Hard rules (inherited from `_drafting_common`)

All rules from `${CLAUDE_PLUGIN_ROOT}/skills/_drafting_common/SKILL.md` apply, plus the SC-specific rules above. In any conflict, **the SC Rules 2013 / Constitution wins over the general drafting-common rules.**

---

## 8. Authority hierarchy (per `04-encoding-rules.md` of the corpus pipeline)

When the case-type skills encode patterns, the order of authority is:

1. Constitution of India (Articles 32, 136, 137, 142)
2. Supreme Court Rules, 2013 (with their Schedules / Forms 28, 32, etc.)
3. Supreme Court Registry Practice Directions and Office Procedure Handbook
4. Leading procedural textbook (M.A. Qureshi, V. Sudhish Pai) — for understanding only, not for verbatim copy
5. Corpus pattern — **never authoritative; only confirms which forms are used in practice**

This base file embeds rules 1-3 directly. Case-type skills must encode patterns traceable to one of these layers; any pattern that traces only to corpus is dropped per the pipeline's Phase 04 encoding rules.

---

## 9. Provenance

This base file was authored fresh in May 2026 with reference only to:
- Public statutory text (Constitution, Supreme Court Rules 2013)
- Public-domain procedural textbooks (citation-only, no verbatim copy)
- Cross-validation report `validation-slp.md` from the India-Legal Corpus Pipeline Phase 03

No drafted prose from any external source has been transcribed into this file. The author certifies compliance with the NOTICE.md doctrine of this plugin.
