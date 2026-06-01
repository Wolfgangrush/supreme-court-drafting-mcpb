# Case Facts Background — SLP (Civil) against HC dismissal in partition matter

All party names, survey numbers, village names, dates beyond the impugned-order date, and amounts are fictional placeholders.

## Parties

- **Petitioner (Original Plaintiff):** [Party-A] son of late [Father-A], elder brother of the Respondent. Aged about [Age-Placeholder] years. Cultivator.
- **Respondent (Original Defendant):** [Party-B] son of late [Father-A], younger brother of the Petitioner. In possession of the suit property since 2008.

## Suit property

- Survey No. [Survey-No-Placeholder], Village [Village-Placeholder], Taluka [Taluka-Placeholder], District [District-Placeholder], Maharashtra.
- Agricultural land admeasuring [Area-Placeholder] acres.
- Originally purchased by [Grand-Father-Placeholder] in 1972.

## Procedural history

- **2018** — Regular Civil Suit No. [RCS-N]/2018 filed by the Petitioner before the Civil Judge Sr. Div., [Placeholder-Court] for declaration that the suit property is joint family property + decree of partition.
- **[Trial-Judgment-Date-Placeholder]** — Trial Court dismisses the suit, holding on Issue No. 3 that the suit property is the self-acquired property of the Respondent (see `02-trial-court-judgment-issue-3-extract.docx`).
- **[FA-Date-Placeholder]** — Regular Civil Appeal No. [RCA-N]/[Year] preferred by the Plaintiff before the District Judge, [Placeholder-District].
- **[FA-Judgment-Date-Placeholder]** — First Appellate Court affirms Trial Court finding without independent evaluation.
- **[SA-Filing-Date-Placeholder]** — Second Appeal No. 1234/2024 filed before the Bombay High Court under Section 100 CPC.
- **10 April 2026** — High Court dismisses Second Appeal (see `01-impugned-hc-second-appeal-judgment-2026-04-10.docx`).
- **[Certified-Copy-Date-Placeholder]** — Certified copy issued; Article 117 of the Limitation Act 1963 90-day window begins.

## Forum and case type

- **Forum:** Supreme Court of India.
- **Case type:** `slp-civil` (Article 136 of the Constitution of India + Order XXI of the Supreme Court Rules 2013).
- **Limitation:** 90 days from date of HC judgment / refusal of certified copy (Article 133 / 117 Limitation Act 1963). Filing within time after deducting time for certified copy.
- **Custody status:** Not applicable (civil matter).
- **AOR Certificate:** Required (rule of the Supreme Court Rules 2013).

## Grounds (skeleton)

1. **Perversity of finding on Issue No. 3** — Trial Court's reliance on alleged oral severance was unsupported by any panchnama, document, or examined panchas. None of the alleged panchas were examined as witnesses. (Per Hari Singh v. Kanhaiya Lal — concurrent findings vitiated by perversity are open to scrutiny.)
2. **Failure to consider material evidence** — PW-3 (retired patwari) deposed that village land records continue to reflect dual cultivation entries and no mutation has happened pursuant to the alleged severance. This material evidence was not considered.
3. **Incorrect application of Mulla on Hindu Law** — joint-family-property presumption attaches once a foundational nucleus of joint family funds is established. The 1972 acquisition by the grandfather was admittedly out of joint family funds. The burden then shifts to the Defendant to prove severance, not merely register a later sale deed in his sole name.
4. **High Court's mechanical affirmation** — the impugned order is a non-speaking dismissal that does not engage with the substantial question of law as framed at the admission stage.
5. **Substantial question of law within Article 136** — the issue of joint-family-property presumption + burden-of-proof on severance is recurring and warrants authoritative pronouncement.

## Prayer

(a) Leave to appeal under Article 136 of the Constitution of India.
(b) Setting aside of the High Court's impugned judgment dated 10 April 2026 in Second Appeal No. 1234/2024.
(c) Setting aside of the concurrent findings of the Trial Court and First Appellate Court on Issue No. 3.
(d) Decree of partition allotting one-half share to the Petitioner in the suit property.
(e) Costs throughout.

## How to use this fixture

1. Point `read_case_folder(path)` at this directory.
2. Reader extracts facts from the 2 `.docx` files plus this `case-facts-background.md`.
3. Call `get_case_type_format("slp-civil")` for the SLP-Civil template.
4. The remaining 5 agents (Format → Drafter → Verifier → Refiner → Overseer) run end-to-end to produce `final-draft.docx` containing the SLP-Civil + Synopsis + List of Dates + Statement of Facts + Questions of Law + Grounds + Prayer + Annexure Index.
