from typing import Any, Dict


def _contains_any(text: str, keywords: Any) -> bool:
    return any(kw in text for kw in keywords)


class AdMatrixAnalyzer:
    """
    Offline heuristic classifier for the AdMatrix framework.

    This version avoids external APIs by using lightweight keyword rules.
    It is deterministic and fast, suitable for demos without credentials.
    """

    def __init__(self) -> None:
        # Rule buckets are intentionally simple for explainability in a demo.
        self.concept_rules = {
            "saving": "Saving money on utilities",
            "cost": "Saving money on utilities",
            "bill": "Saving money on utilities",
            "speed": "Performance and speed",
            "faster": "Performance and speed",
            "instant": "Performance and speed",
            "skin": "Beauty and skin health",
            "serum": "Beauty and skin health",
            "posture": "Habit formation and wellness",
            "routine": "Habit formation and wellness",
            "coffee": "Convenience and self-care",
        }

        self.trigger_rules = {
            "new year": "New Year reset",
            "new job": "Career change",
            "bill": "Recent spike in household bills",
            "crying": "Daily morning struggle",
            "6 am": "Daily morning struggle",
            "scroll": "Ongoing social feed browsing",
        }

        self.persona_rules = {
            "mom": "Busy mom juggling tasks",
            "baby": "Busy mom juggling tasks",
            "home": "Homeowner looking for efficiency",
            "laptop": "Young professional upgrading gear",
            "posture": "Desk worker worried about posture",
            "skin": "Beauty enthusiast seeking dermatologist-approved look",
        }

        self.format_rules = {
            "unbox": "Unboxing demo",
            "green": "Green screen demo",
            "routine": "Routine tutorial",
            "watch": "Tutorial walkthrough",
            "here's how": "Tutorial walkthrough",
        }

        self.hook_rules = {
            "what if": "Rhetorical question",
            "ask yourself": "Rhetorical question",
            "hate": "Contrarian claim",
            "cut": "Bold claim with quantified benefit",
            "30%": "Bold claim with quantified benefit",
            "5 seconds": "Time-based proof",
            "10 minutes": "Time-based proof",
        }

    def analyze_text(self, ad_text: str) -> Dict[str, Any]:
        normalized = ad_text.lower()

        # Concept (Angle): persuasion angle.
        concept = self._match_rule(normalized, self.concept_rules, "General benefit")
        # Trigger: moment that makes the ad relevant now.
        trigger = self._match_rule(normalized, self.trigger_rules, "General need state")
        # Driver Persona: who the ad speaks to.
        driver = self._match_rule(normalized, self.persona_rules, "General consumer")
        # Format: style/content type.
        content_format = self._match_rule(normalized, self.format_rules, "UGC testimonial")
        # Hook Type: how attention is captured.
        hook = self._match_rule(normalized, self.hook_rules, "Direct statement")

        rationale = (
            f"Heuristic labels based on detected keywords for concept={concept}, trigger={trigger}, "
            f"persona={driver}, format={content_format}, hook={hook}."
        )

        return {
            "concept": concept,
            "trigger": trigger,
            "driver_persona": driver,
            "format": content_format,
            "hook_type": hook,
            "rationale": rationale,
        }

    def _match_rule(self, text: str, rules: Dict[str, str], default: str) -> str:
        for keyword, label in rules.items():
            if keyword in text:
                return label
        return default
