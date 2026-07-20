import json
from pydantic import BaseModel, Field
from typing import Dict

class CountryScores(BaseModel):
    name: str
    profile: str
    scores: Dict[str, float] = Field(..., description="Map of dimensions to scores 0-100")

class DataManager:
    def __init__(self, file_path: str = "pulse_ai/data/countries.json"):
        self.file_path = file_path

    def load_countries(self) -> Dict[str, CountryScores]:
        with open(self.file_path, 'r') as f:
            data = json.load(f)

        # Validate each country using Pydantic
        validated_data = {}
        for key, value in data.items():
            validated_data[key] = CountryScores(**value)
        return validated_data

    def save_countries(self, data: Dict[str, CountryScores]):
        with open(self.file_path, 'w') as f:
            # Convert Pydantic models back to dict for JSON storage
            serializable_data = {k: v.model_dump() for k, v in data.items()}
            json.dump(serializable_data, f, indent=2)
