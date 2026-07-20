import random
import time
from typing import List, Dict

class AnomalySimulator:
    """
    Simulates a stream of network health metrics and identifies anomalies.
    Used to demonstrate how AI would monitor infrastructure in real-time.
    """

    def __init__(self):
        self.metrics = ["Latency", "Packet Loss", "Jitter", "Throughput"]

    def generate_metric_stream(self, is_disaster: bool = False) -> Dict[str, float]:
        """
        Generates a snapshot of network metrics.
        If is_disaster is True, metrics will be degraded and more volatile.
        """
        snapshot = {}
        for metric in self.metrics:
            if is_disaster:
                # High volatility and poor values
                val = random.uniform(10.0, 100.0) if metric == "Throughput" else random.uniform(100.0, 1000.0)
            else:
                # Stable, healthy values
                if metric == "Throughput":
                    val = random.uniform(800.0, 1000.0)
                else:
                    val = random.uniform(10.0, 50.0)
            snapshot[metric] = val
        return snapshot

    def detect_anomalies(self, snapshot: Dict[str, float]) -> List[str]:
        """
        Detects anomalies based on thresholding.
        """
        anomalies = []
        # Simple heuristic thresholds
        thresholds = {
            "Latency": 200.0,
            "Packet Loss": 5.0,
            "Jitter": 30.0,
            "Throughput": 300.0 # Low throughput is an anomaly
        }

        for metric, val in snapshot.items():
            if metric == "Throughput":
                if val < thresholds[metric]:
                    anomalies.append(f"Critical drop in {metric}: {val:.2f}")
            else:
                if val > thresholds[metric]:
                    anomalies.append(f"Spike in {metric}: {val:.2f}")

        return anomalies
