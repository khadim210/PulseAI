import requests
import random
from typing import Dict, List, Optional

class ClimateAPIClient:
    """
    Connects to public APIs to fetch real-time disaster alerts.
    In a real production environment, this would use official API keys.
    """
    GDACS_URL = "https://www.gdacs.org/xml/rss.xml" # Simplified for demo

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    def fetch_active_disasters(self) -> List[Dict]:
        """
        Fetches a list of ongoing global disasters.
        Returns a mock list if the API is unreachable or for demo purposes.
        """
        try:
            # In reality, we would parse the GDACS RSS/XML feed
            # response = requests.get(self.GDACS_URL, timeout=5)
            # return self._parse_gdacs(response.text)

            # For the demo, we simulate a real-time feed based on current date
            # but with a chance of "Live" events.
            events = [
                {"type": "Earthquake", "coords": [35.6, 139.6], "intensity": 6.2, "region": "Japan"},
                {"type": "Storm", "coords": [15.5, -61.3], "intensity": 1.5, "region": "Caribbean"},
                {"type": "Flood", "coords": [23.1, 90.3], "intensity": 1.2, "region": "Bangladesh"},
            ]
            return random.sample(events, random.randint(1, 3))
        except Exception as e:
            print(f"API Error: {e}")
            return []

    def check_region_risk(self, lat: float, lon: float) -> Optional[Dict]:
        """
        Checks if a specific coordinate is within the impact zone of an active disaster.
        """
        active_events = self.fetch_active_disasters()
        for event in active_events:
            # Simple distance check (Haversine could be used here)
            dist = ((event["coords"][0] - lat)**2 + (event["coords"][1] - lon)**2)**0.5
            if dist < 5.0: # Within 5 degrees
                return event
        return None
