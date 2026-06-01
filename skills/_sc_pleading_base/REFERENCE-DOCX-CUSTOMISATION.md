# `reference.docx` — Customisation Guide

The `reference.docx` in this folder is the **pandoc template** the Drafter agent uses when converting markdown drafts to `.docx`. Without customisation, pandoc uses its default styles. **For Supreme Court Registry compliance, customise this file once.**

---

## Why customise

The Supreme Court Registry rejects petitions on minor formatting deviations. Pandoc's default `.docx` styles are office-document-generic, not SC-Registry-compliant. Customising `reference.docx` once aligns every future Drafter output with SC Registry requirements.

---

## SC Registry formatting mandate

| Element | Specification |
|---|---|
| Paper size | A4 |
| Print | One-side |
| Font (body) | Times New Roman, 14 point |
| Line spacing | 1.5 |
| Left margin (binding side) | 4 cm |
| Top / bottom / right margin | 2.5 cm |
| Section headers | Title Case, bold, 14 point |
| Page numbers | Centred at bottom of page |
| Folder colour at filing | White for SLP Civil · Blue for SLP Criminal (per Registry direction; verified at filing — not a `.docx` property) |

---

## How to customise (one-time, ~10 minutes)

1. **Open the file in Microsoft Word or LibreOffice:**
   ```bash
   open "<your-anthropic-plugins-folder>/supreme-court-drafting/skills/_sc_pleading_base/reference.docx"
   ```

2. **Set page size and margins** (Layout / Page Setup):
   - Paper size: A4
   - Margins: Top 2.5 cm · Bottom 2.5 cm · Left 4 cm · Right 2.5 cm

3. **Set body style** (Home / Styles / Normal):
   - Font: Times New Roman, 14 point
   - Line spacing: 1.5 lines (Paragraph dialog → Line spacing → 1.5 lines)

4. **Set heading styles** (Heading 1, Heading 2, Heading 3):
   - Font: Times New Roman, 14 point, bold
   - Spacing before: 12 pt · Spacing after: 6 pt
   - Same line spacing as body

5. **Add page numbers** (Insert / Page Number):
   - Position: Bottom of page, centred

6. **Save the file** (Cmd-S / Ctrl-S). Keep the filename `reference.docx`.

7. **Verify pandoc uses it** by running the Drafter on a sample case folder and inspecting the output `.docx` — open in Word, confirm font, spacing, margins.

---

## What NOT to customise

- **Do not add content** (no headers, no footers with text, no watermarks). The reference.docx is a STYLE template; pandoc populates the content from the markdown.
- **Do not change the file location.** The Drafter looks for `reference.docx` in this `_sc_pleading_base/` folder. Moving / renaming breaks the pandoc command.
- **Do not commit a `reference.docx` with case-specific content.** The `.gitignore` excludes draft `.docx` files; the reference template itself stays in the repository.

---

## How the Drafter uses it

The Drafter renders markdown to `.docx` via:

```bash
pandoc draft-v1.md -o draft-v1.docx \
  --reference-doc="${CLAUDE_PLUGIN_ROOT}/skills/_sc_pleading_base/reference.docx"
```

Pandoc reads the styles from your customised `reference.docx` and applies them to every section of the draft. Body text → Normal style. Section headings → Heading 1 / 2 / 3 styles. Tables → Table style.

---

## Fallback if pandoc is unavailable

The Drafter falls back to `python-docx` (which uses simpler default styles). This produces a usable `.docx` but does not match SC Registry formatting precisely. For Registry-compliant output, install pandoc:

```bash
# macOS
brew install pandoc

# Linux (Debian/Ubuntu)
sudo apt install pandoc
```
