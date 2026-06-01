# Privacy Policy

This connector follows the canonical Wolfgang Rush privacy policy.

**Full text:** <https://wolfgangrush.github.io/privacy/>

## Summary

- **Data collected:** none
- **Server operated by Publisher:** none
- **Telemetry / analytics:** none
- **Third-party sharing:** none
- **Data retention:** none

All processing happens on the user's machine. The Publisher (Wolfgang Rush) never receives any user data.

## Claude memory · chat history · uploaded files

This connector does **not** read, query, or extract data from Claude memory, chat history, conversation summaries, or user-uploaded files. It operates **only** on files the user explicitly places in the case-folder argument passed to its tools (`read_case_folder(path)` and equivalents).

## Pseudonymisation firewall

The connector applies a three-layer privacy firewall (L1 substitution → L2 LLM-blind → L3 re-substitution) for all case-folder work, preventing real party names, case numbers, and financial figures from leaving the user's machine in identifiable form.

## Contact

wolfgangrush@gmail.com
