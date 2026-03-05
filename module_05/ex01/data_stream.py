from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        # Default filtering logic
        return data_batch if not criteria else [d for d in data_batch if criteria in str(d)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"status": "active"}

class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            return f"Sensor {self.stream_id} processed {len(data_batch)} readings."
        except Exception:
            return "Error processing batch"

class StreamProcessor:
    # Notice how the type hint is the base class!
    def handle_stream(self, stream: DataStream, batch: List[Any]) -> str:
        # Polymorphism in action: calling the interface method
        filtered = stream.filter_data(batch)
        return stream.process_batch(filtered)