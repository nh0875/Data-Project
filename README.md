# AdMatrix Analyzer

A lightweight Python tool to turn raw ad copy or video transcripts into structured, quant-ready insights across five MarTech dimensions (Concept, Trigger, Driver Persona, Format, Hook Type). This version runs **offline with heuristic rules** (no API key required) to demo the workflow quickly while keeping humans in control of final strategic decisions.

## What it does
- Ingests raw ad text from `input_ads.csv`.
- Applies a deterministic keyword-based classifier (no external calls) to label each ad.
- Writes a clean `analyzed_output.csv` ready for Google Sheets.
- Captures per-row issues in `error_message` so one noisy ad does not stop the batch.

## Why it matters
Marketing research teams lose time normalizing qualitative ads. This script standardizes the classification step so analysts can focus on interpreting patterns (which still requires human judgment). The framework is deliberately opinionated to keep outputs comparable across campaigns and channels.

## File map
- `main.py` — orchestrates load → analyze → export.
- `analyzer.py` — Offline heuristic classifier (keyword rules for the five dimensions).
- `data_loader.py` — CSV ingestion helper.
- `input_ads.csv` — demo inputs.
- `analyzed_output.csv` — generated output (created at runtime).
- `requirements.txt` — pinned dependencies.

## Setup
1) Python 3.10+.
2) Install deps:
   ```bash
   pip install -r requirements.txt
   ```
 3) No API key needed for the offline demo.

## Usage
```bash
python main.py --input input_ads.csv --output analyzed_output.csv --model gpt-4o-mini
```
Arguments:
- `--input` (default `input_ads.csv`)
- `--output` (default `analyzed_output.csv`)
- `--model` (kept for interface parity; ignored in offline mode)

## The Matrix (required dimensions)
- **Concept (Angle):** The core persuasion angle (e.g., saving money, status, convenience).
- **Trigger:** The event or moment that makes the viewer care now (e.g., New Year, sudden problem).
- **Driver Persona:** Who the ad speaks to (e.g., busy mom, tech-savvy early adopter).
- **Format:** Content style (e.g., UGC, unboxing, green screen, testimonial montage).
- **Hook Type:** Attention grabber (e.g., shocking stat, rhetorical question, bold claim).

## Rule design (offline heuristic)
- Keyword buckets map common phrases to each dimension; defaults keep the JSON schema complete.
- Rationale notes which buckets were hit so the demo stays auditable and deterministic (no API variance).

## Error handling
- Each ad is wrapped in try/except; failures are logged in `error_message` while the loop continues.
- CSV order preserves `raw_text` next to labels for quick auditing.

## Extending to Anthropic or OpenAI
- Swap `AdMatrixAnalyzer` with an API-backed variant (see earlier commit history) while keeping the same schema.
- Keep temperature low (≤0.3) to reduce label drift if you re-enable an API model.

## AI Philosophy
This tool accelerates analysts by batch-structuring qualitative ad data, but it does not replace human strategic judgment. The model proposes classifications; a human researcher should validate patterns, adjust the framework if campaign goals shift, and decide how insights translate into creative strategy.

## Sample workflow for Sheets
1) Run the script.
2) Open `analyzed_output.csv` in Google Sheets or import via `File → Import`.
3) Add filters/pivots by Concept, Trigger, Persona to find winning themes.
4) Spot-check a handful of rows to ensure labels match brand context before scaling.

## Testing tips
- Start with the provided `input_ads.csv` to verify pipeline and JSON parsing.
- Add noisy or edge-case ads (typos, emojis) to ensure the classifier remains stable.
- If you see parsing errors, lower `temperature` further or tighten prompt examples.
