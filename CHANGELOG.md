# Changelog
See [README.md](./README.md) for current version's documentation.

Notable changes and release notes will be documented in this file.

## Early development
**Early development release. Not yet usable for serious work.**

Currently functional on **Windows 11 via PowerShell,** all instructions for PowerShell if not otherwise specified. Other platforms remain untested.

***Install***

**Requires uv**, if not installed follow https://docs.astral.sh/uv/getting-started/installation/

**Then in PowerShell:**
```powershell
# Replace version tag "v0.1.0-alpha" with desired version tag
uv tool install git+https://github.com/AkiPoh/akidocs.git@v0.1.0-alpha#subdirectory=akidocs-core
```

**See https://github.com/AkiPoh/akidocs/tree/v0.1.0-alpha for this version's documentation.** Replace version tag with right one.

**Full Changelog: https://github.com/AkiPoh/akidocs/compare/v0.0.1-alpha...v0.1.0-alpha.** Replace version tag with right one.

### Akidocs - v0.1.0-alpha / 0.1.0a0 - 2025-12.26
#### What's New
- Inline text formatting
  - `*Italics*` is *Italics*
  - `**Bold**` is **Bold**
  - `***Bold and Italic***` is ***Bold and Italic***
  - Nested styles, for example `**bold with *italic* inside**` is **bold with *italic* inside** works correctly
- New CLI flags
  - `-h` or `--help` for help information
  - `-v` or `--version` for version information
  - `-o` or `--open` to open the PDF after creation
  
#### What's New Internally
- New inline tokenizer system for parsing formatted text
- Included significant changes and refactors throughout codebase, especially as many before mentioned changes were considerable

### Akidocs - v0.0.1-alpha / 0.0.1a0 - 2025-12.25
#### What's New
- Better handling of Markdown headline edge cases (7+ hashes, missing space after #, etc.)
- Windows line endings (CRLF) now parse correctly
- Removed installing from source from suggested installation methods in README.md, instead installing from source is now under development section

#### What's New Internally
- General internal improvements and refactoring.
- Extracted style constants to the top of renderer
- Now uses points for all styling constants instead of millimeters
- Refactored renderer and tokenizer internals

### Akidocs - v0.0.0-alpha / 0.0.0a0 - 2025-12.25

#### Features
- Takes in a Markdown file, parses it, and outputs it as a PDF
- Headers (levels 1-6)
- Paragraphs
- Usable as a CLI tool (`aki`)
