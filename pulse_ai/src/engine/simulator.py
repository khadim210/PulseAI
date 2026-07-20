from typing import Dict, List

class DisasterSimulator:
    """
    Simulates the impact of disasters on the National Digital Resilience Score (NDRS).
    Uses a Degradation Matrix to apply multipliers to specific dimensions.
    """

    # Degradation Matrix: { DisasterType: { Dimension: ImpactMultiplier } }
    # Multiplier < 1.0 means score decreases.
    # Example: 0.7 means 30% loss of resilience in that dimension.
    DEGRADATION_MATRIX = {
        "Cyber Attack": {
            "Cybersecurity": 0.4,
            "Data Governance": 0.5,
            "Critical Services Continuity": 0.7,
            "Telecommunications Connectivity": 0.8,
            "Interoperability": 0.8
        },
        "Earthquake": {
            "Energy Resilience": 0.3,
            "Telecommunications Connectivity": 0.5,
            "Critical Services Continuity": 0.6,
            "Emergency Communications": 0.7,
            "Inclusion and Accessibility": 0.8
        },
        "Flood": {
            "Energy Resilience": 0.5,
            "Telecommunications Connectivity": 0.6,
            "Critical Services Continuity": 0.7,
            "Emergency Communications": 0.8,
            "Inclusion and Accessibility": 0.8
        },
        "Pandemic": {
            "Critical Services Continuity": 0.8,
            "Inclusion and Accessibility": 0.7,
            "Data Governance": 0.9,
            "Interoperability": 0.8
        }
    }

    @classmethod
    def apply_disaster(cls, disaster_type: str, current_scores: Dict[str, float]) -> Dict[str, float]:
        """
        Applies a disaster event to the current scores.
        :param disaster_type: Key from DEGRADATION_MATRIX.
        :param current_scores: Dict of current dimension scores.
        :return: New scores after degradation.
        """
        if disaster_type not in cls.DEGRADATION_MATRIX:
            return current_scores.copy()

        impacts = cls.DEGRADATION_MATRIX[disaster_type]
        new_scores = current_scores.copy()

        for dim, multiplier in impacts.items():
            if dim in new_scores:
                new_scores[dim] *= multiplier

        return new_scores

    @classmethod
    def get_available_disasters(cls) -> List[str]:
        return list(cls.DEGRADATION_MATRIX.keys())
