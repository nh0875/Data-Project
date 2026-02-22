import argparse
import traceback
from typing import Any, Dict, List

import pandas as pd

from analyzer import AdMatrixAnalyzer
from data_loader import load_ads


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AdMatrix Analyzer: structure ad texts via LLM")
    parser.add_argument("--input", default="input_ads.csv", help="Path to input CSV with ad_text column")
    parser.add_argument("--output", default="analyzed_output.csv", help="Destination CSV for structured results")
    parser.add_argument("--model", default="gpt-4o-mini", help="LLM model name")
    return parser.parse_args()


def analyze_ads(ad_texts: List[str], model: str) -> List[Dict[str, Any]]:
    # Model parameter preserved for interface parity; unused in offline heuristic mode.
    analyzer = AdMatrixAnalyzer()

    results: List[Dict[str, Any]] = []
    for idx, ad_text in enumerate(ad_texts, start=1):
        try:
            structured = analyzer.analyze_text(ad_text)
            structured["ad_id"] = idx
            structured["raw_text"] = ad_text
            structured["error_message"] = ""
        except Exception as exc:
            # Capture errors per-ad to keep the batch moving.
            structured = {
                "ad_id": idx,
                "raw_text": ad_text,
                "concept": None,
                "trigger": None,
                "driver_persona": None,
                "format": None,
                "hook_type": None,
                "rationale": None,
                "error_message": f"{exc} | Traceback: {traceback.format_exc(limit=1)}",
            }
        results.append(structured)
    return results


def main() -> None:
    args = parse_args()
    ad_texts = load_ads(args.input)

    structured = analyze_ads(ad_texts, args.model)
    df = pd.DataFrame(structured)

    # Column order aligns with the framework: Concept, Trigger, Driver Persona, Format, Hook Type.
    ordered_cols = [
        "ad_id",
        "raw_text",
        "concept",
        "trigger",
        "driver_persona",
        "format",
        "hook_type",
        "rationale",
        "error_message",
    ]
    df = df.reindex(columns=ordered_cols)
    df.to_csv(args.output, index=False)
    print(f"Wrote structured output to {args.output}")


if __name__ == "__main__":
    main()
