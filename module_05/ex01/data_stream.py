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
        # 1. THE TYPE CHECK (Using the newly authorized isinstance)
        # This elegantly stops bad data types before they even enter the logic.
        if not isinstance(data_batch, list):
            return "Error: Expected a list of data."
            
        # 2. THE STREAM PROTECTION (Using try/except)
        # Even if it IS a list, the actual processing inside might still crash!
        # The try/except acts as the shield to prevent the whole program from dying.
        try:
            # Imagine complex sensor math happens here that might divide by zero
            # or fail to parse a specific string inside the list.
            readings_count = len(data_batch)
            return f"Sensor {self.stream_id} processed {readings_count} readings."
            
        except Exception as e:
            # If the math fails, the stream survives and just returns an error string.
            return f"Error processing batch: {e}"

class StreamProcessor:
    # Notice how the type hint is the base class!
    def handle_stream(self, stream: DataStream, batch: List[Any]) -> str:
        # Polymorphism in action: calling the interface method
        filtered = stream.filter_data(batch)
        return stream.process_batch(filtered)