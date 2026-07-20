from typing import Dict, List, Tuple
import random

class FragilityModel:
    """
    Implements scientific fragility curves for different ICT supports.
    Vulnerability is expressed as the probability of survival given a disaster.
    """
    # P(Survival | Disaster)
    # Values are simplified representative coefficients based on SOTA research.
    VULNERABILITY_MATRIX = {
        "Earthquake": {
            "fiber": 0.3,       # Highly vulnerable to ground displacement
            "cellular": 0.6,     # Tower collapse risk
            "satellite": 0.95    # Ground station mostly safe unless epicenter
        },
        "Flood": {
            "fiber": 0.6,       # Water ingress in conduits
            "cellular": 0.5,     # Base stations flooded
            "satellite": 0.8     # Ground terminal vulnerable
        },
        "Storm": {
            "fiber": 0.8,       # Only aerial fiber is very vulnerable
            "cellular": 0.4,     # Wind-borne debris / Tower collapse
            "satellite": 0.7     # Rain fade / Antenna misalignment
        },
        "CyberAttack": {
            "fiber": 1.0,       # Physical cable not affected
            "cellular": 0.8,     # Control plane attacks
            "satellite": 0.9     # Link stability
        }
    }

    @classmethod
    def get_survival_prob(cls, disaster_type: str, support: str) -> float:
        """Returns the probability of survival for a given support during a disaster."""
        return cls.VULNERABILITY_MATRIX.get(disaster_type, {}).get(support, 1.0)

class RegionalPredictionEngine:
    """
    Predicts regional NDRS degradation using a cascading failure model.
    """
    def __init__(self, geodata_path: str = "pulse_ai/data/geodata.json"):
        import json
        with open(geodata_path, 'r') as f:
            self.data = json.load(f)

    def predict_regional_impact(self, country_id: str, region_id: str, disaster_type: str, event_intensity: float = 1.0) -> Dict:
        """
        Calculates the predicted resilience of a specific region.
        :param event_intensity: Multiplier (e.g., 1.0 for standard, 2.0 for extreme)
        """
        country = self.data["countries"].get(country_id)
        if not country: return {"error": "Country not found"}

        region = country["regions"].get(region_id)
        if not region: return {"error": "Region not found"}

        baseline_scores = country["baseline_scores"]
        supports = region["supports"]
        energy_backup = region["energy_backup"]

        # 1. Calculate Weighted Survival Probability for the region
        # TotalSurvival = Sum( SupportProb * SupportWeight )
        total_survival_prob = 0.0
        for support, weight in supports.items():
            prob = FragilityModel.get_survival_prob(disaster_type, support)
            # Apply intensity (simplification: higher intensity reduces survival linearly)
            effective_prob = max(0.1, prob - (0.1 * (event_intensity - 1.0)))
            total_survival_prob += effective_prob * weight

        # 2. Energy Cascade Logic
        # If energy resilience is low, ICT survival is further capped
        # Probability of energy failure based on event intensity
        energy_failure_prob = 0.2 * event_intensity
        energy_survival = max(0.1, 1.0 - energy_failure_prob)

        # If energy survival is low, and region backup is low, ICT is crippled
        effective_ict_survival = total_survival_prob * (energy_survival + (1 - energy_survival) * energy_backup)

        # 3. Compute Predicted Scores for the 10 dimensions
        # We apply the effective survival to dimensions sensitive to infrastructure
        predicted_scores = {}
        infra_dims = ["Telecommunications Connectivity", "Emergency Communications", "Critical Services Continuity", "Energy Resilience"]

        for dim, score in baseline_scores.items():
            if dim in infra_dims:
                predicted_scores[dim] = score * effective_ict_survival
            else:
                # Non-infra dimensions (like Data Governance) are less affected by physical cuts
                # but still slightly degraded by lack of access
                predicted_scores[dim] = score * max(0.7, effective_ict_survival)

        return {
            "region_id": region_id,
            "predicted_scores": predicted_scores,
            "survival_prob": effective_ict_survival,
            "risk_level": "Critical" if effective_ict_survival < 0.4 else "High" if effective_ict_survival < 0.7 else "Moderate"
        }

class CableRiskEngine:
    """
    Models the impact of submarine cable ruptures on national interoperability.
    """
    @staticmethod
    def calculate_cable_impact(country_id: str, damaged_stations: List[str], geodata: Dict) -> float:
        """
        Returns a multiplier for 'Interoperability' and 'Connectivity' based on cable loss.
        """
        country = geodata["countries"].get(country_id)
        if not country: return 1.0

        stations = country.get("landing_stations", [])
        total_cables = sum(len(s["cables"]) for s in stations)

        if total_cables == 0: return 1.0

        lost_cables = 0
        for s in stations:
            if s["name"] in damaged_stations:
                lost_cables += len(s["cables"])

        # Resilience loss is not linear; losing the first cable is bad, losing the last is total.
        loss_ratio = lost_cables / total_cables
        # If we lose 50% of cables, the interoperability drops significantly due to BGP routing stress.
        impact = 1.0 - (loss_ratio * 0.8) # Max 80% drop
        return max(0.2, impact)
