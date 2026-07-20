from typing import Dict

class RiskAssessor:
    """
    Categorizes the risk level of a country based on its NDRS.
    """

    # Thresholds for risk levels (based on total score 0-1000)
    THRESHOLDS = {
        "Critical": 300, # < 300
        "High": 500,     # 300 - 500
        "Medium": 750,   # 500 - 750
        "Low": 1000      # 750 - 1000
    }

    @classmethod
    def assess_risk(cls, total_score: float) -> str:
        """
        Returns the risk level based on the total score.
        """
        if total_score < cls.THRESHOLDS["Critical"]:
            return "Critical"
        elif total_score < cls.THRESHOLDS["High"]:
            return "High"
        elif total_score < cls.THRESHOLDS["Medium"]:
            return "Medium"
        else:
            return "Low"

    @classmethod
    def get_risk_color(cls, risk_level: str) -> str:
        """Returns a hex color for the risk level to be used in the UI."""
        colors = {
            "Critical": "#FF0000", # Red
            "High": "#FF8C00",     # DarkOrange
            "Medium": "#FFFF00",   # Yellow
            "Low": "#00FF00"       # Green
        }
        return colors.get(risk_level, "#FFFFFF")
