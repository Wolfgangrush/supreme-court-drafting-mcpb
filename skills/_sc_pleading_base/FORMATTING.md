# FORMATTING.md — Supreme Court of India formatting specification

Plain-language formatting reference for `supreme-court-drafting`. SC Registry rejects on minor formatting deviations — verify each setting before filing.

---

## Paper & layout

- **Paper size:** A4 white paper
- **Print:** **one-side only** — SC Rules 2013 mandate

## Typography

- **Font family:** Times New Roman
- **Font size body:** 14 point
- **Font size headings:** 14 point bold
- **Line spacing:** 1.5 lines

## Margins

- **Left (binding side):** 4 cm — mandatory
- **Top / bottom / right:** 2.5 cm

## Page numbers

- Centred at bottom
- Continuous pagination — main petition through annexures through accompanying applications

## Folder colour at filing

- **SLP Civil:** white folder
- **SLP Criminal:** blue folder
- (Per SC Registry direction — verified at the filing counter, not a `.docx` property)

## Section headers

- Title Case, bold, 14 point
- Spacing before heading: 12 pt · spacing after heading: 6 pt

## Cause Title block

- Court header (centred, all caps):
  ```
  IN THE SUPREME COURT OF INDIA
  ```
- Jurisdiction line (centred, all caps):
  - `CIVIL APPELLATE JURISDICTION` (SLP Civil, Review of civil judgment)
  - `CRIMINAL APPELLATE JURISDICTION` (SLP Criminal, Review of criminal judgment)
  - `CIVIL ORIGINAL JURISDICTION` (Writ Petition under Article 32 — civil)
  - `CRIMINAL ORIGINAL JURISDICTION` (Writ Petition under Article 32 — habeas corpus / quashing)
- Case number line: `Special Leave Petition (Civil) No. _____ of [Year]` (or as applicable)
- Arising-out-of parenthetical (for SLP/Appeals):
  ```
  (Arising out of impugned judgment / order dated <DD.MM.YYYY> passed by
   the Hon'ble High Court of [State] at [Place] in [Case Type & Number])
  ```

## Annexure marker convention (SC-specific)

- Petitioner's annexures: `ANNEXURE P-1`, `ANNEXURE P-2`, ...
- Respondent's annexures (in Counter-Affidavit / Reply): `ANNEXURE R-1`, `ANNEXURE R-2`, ...
- Collective annexures: `ANNEXURE P-N (COLLY)`
- True-copy markings: each annexure carries `"True copy"` stamp
- Inline marker pattern: `...a true copy whereof is annexed hereto and marked as ANNEXURE P-[N]`
- Consolidated `Annexure Index` at end of petition

## Synopsis + List of Dates (MANDATORY)

- Synopsis: ≤ 3 pages · prefixed to the main petition body OR filed as separate document per Registry direction
- List of Dates: tabular format (NOT narrative prose)
  - Two-column table: Date | Event
  - Begins with the earliest material date; ends with the date of the impugned order

## AOR Certificate (Order IV Rule 1(c) SC Rules 2013 — verbatim)

The AOR Certificate language is recited verbatim from the Rule:

> The Advocate-on-Record certifies that the petition is confined to the pleadings before the Court / Tribunal whose order is challenged and the other statutory requirements of the Supreme Court Rules 2013 have been complied with.

Placeholder block for AOR name + registration code + signature + date.

## Affidavit verification

- Per Order IX SC Rules 2013 + CPC Order XIX
- Sworn before a Notary / Oath Commissioner in New Delhi or wherever the petitioner is located
- Layout per the affidavit verification baseline in each case-type `format-from-user.md`

## Limitation block (case-type-specific)

- SLP (Civil / Criminal): 90 days from date of impugned order (60 days where certificate of fitness refused)
- Review Petition: 30 days from date of order under review (Order XLVII Rule 1(2) SC Rules 2013)
- Writ under Article 32: no statutory limitation (Tilokchand Motichand line — delay and laches doctrine)
- Transfer Petition: no statutory limitation; computed from cause for transfer
- Curative Petition: no statutory period; filed as ground crystallises post-Review dismissal

## Accompanying applications (case-type-specific)

- Each application repeats own Cause Title + own facts + own prayer + own Affidavit + own AOR Certificate
- Listed in the petition's Index

---

## How to apply these in Microsoft Word / LibreOffice

Same as the indian-hc-drafting FORMATTING.md instructions, with:
- Paper size: A4 (mandatory)
- Line spacing: 1.5 (mandatory)
- One-side print (mandatory)

---

**This is the formatting spec. The `reference.docx` in this folder is a pre-configured binary template. Use either.**
