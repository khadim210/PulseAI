from typing import List, Dict

class PredictiveModule:
    """
    Predicts potential failure points in the digital ecosystem.
    In a production environment, this would use ML models.
    Here, it uses a heuristic-based approach based on the current resilience scores.
    """

    @staticmethod
    def predict_failures(scores: Dict[str, float], disaster_type: str) -> List[str]:
        """
        Analyzes which dimensions are most likely to collapse under a specific disaster.
        :param scores: Current dimension scores.
        :param disaster_type: The disaster scenario.
        :return: List of dimensions at high risk of failure.
        """
        risky_dimensions = []

        # Threshold for "likely failure": if current score is low AND disaster heavily impacts it
        # Or if the impact would bring it below a critical threshold (e.g., 40).

        # We import the matrix here to avoid circular imports if needed, but it's safe in this structure.
        from pulse_ai.src.engine.simulator import DisasterSimulator

        matrix = DisasterSimulator.DEGRADATION_MATRIX.get(disaster_type, {})

        for dim, multiplier in matrix.items():
            current_val = scores.get(dim, 0.0)
            predicted_val = current_val * multiplier

            if predicted_val < 40:
                risky_dimensions.append(f"{dim} (Predicted: {predicted_val:.1f})")

        if not risky_dimensions:
            # If nothing is critical, list the top 2 most impacted
            sorted_impacts = sorted(matrix.items(), key=lambda x: x[1])
            for dim, mult in sorted_impacts[:2]:
                risky_dimensions.append(f"{dim} (High Impact: {mult})")

        return risky_dimensions
