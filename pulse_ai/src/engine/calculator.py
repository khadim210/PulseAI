from typing import Dict

class NDRSCalculator:
    """
    Implements the National Digital Resilience Score (NDRS) calculation.
    Formula: NDRS = Sum of 10 dimensions (each 0-100).
    Total max score: 1000.
    """
    DIMENSIONS = [
        "Telecommunications Connectivity",
        "Emergency Communications",
        "Digital Sovereignty",
        "Critical Services Continuity",
        "Cybersecurity",
        "Data Governance",
        "Inclusion and Accessibility",
        "AI and IoT Readiness",
        "Energy Resilience",
        "Interoperability"
    ]

    @staticmethod
    def calculate_score(scores: Dict[str, float], weights: Dict[str, float] = None) -> float:
        """
        Calculates the total NDRS.
        :param scores: Dictionary of dimension names to values (0-100).
        :param weights: Optional dictionary of weights for each dimension.
                        If None, equal weighting (1.0) is used.
        """
        total_score = 0.0

        for dim in NDRSCalculator.DIMENSIONS:
            val = scores.get(dim, 0.0)
            # Ensure value is within [0, 100]
            val = max(0.0, min(100.0, val))

            weight = 1.0
            if weights and dim in weights:
                weight = weights[dim]

            total_score += val * weight

        return total_score

    @staticmethod
    def get_percentage(score: float) -> float:
        """Returns the NDRS as a percentage of the theoretical maximum (1000)."""
        # Note: This assumes equal weighting. For custom weights, max would change.
        return (score / 1000.0) * 100
