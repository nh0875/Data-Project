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
<img width="212" height="223" alt="image" src="https://github.com/user-attachments/assets/05062ebb-c257-411b-8cb8-100f49b86e73" />


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
<img width="806" height="288" alt="image" src="https://github.com/user-attachments/assets/a5c4ebf2-30dc-40be-b717-a1338051a7cd" />


## Rule design (offline heuristic)
- Keyword buckets map common phrases to each dimension; defaults keep the JSON schema complete.
- Rationale notes which buckets were hit so the demo stays auditable and deterministic (no API variance).

## Error handling
- Each ad is wrapped in try/except; failures are logged in `error_message` while the loop continues.
- CSV order preserves `raw_text` next to labels for quick auditing.
<img width="200" height="263" alt="image" src="https://github.com/user-attachments/assets/3b309a7c-4eef-4766-aebd-93e5d4965469" />


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

<img width="1419" height="206" alt="image" src="https://github.com/user-attachments/assets/e14497cf-afb5-4448-9995-3ed32a001011" />

## Testing tips
- Start with the provided `input_ads.csv` to verify pipeline and JSON parsing.
- If you see parsing errors, lower `temperature` further or tighten prompt examples.

## Dashboard using Sheets
<img width="1918" height="910" alt="image" src="https://github.com/user-attachments/assets/aebf636d-02f5-485f-94ec-fb03d09fa449" />







