from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol

# 1. Duck Typing Protocol (No inheritance needed for children)
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass

# Stages implement the Protocol implicitly just by having a process() method
class InputStage:
    def process(self, data: Any) -> Dict:
        return {"raw": data}

# 2. Abstract Base Class
class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[ProcessingStage] = []
        
    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

# 3. Concrete Adapters inheriting from ABC
class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        # Logic running data through self.stages
        return f"JSON pipeline {self.pipeline_id} processed data."

class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []
        
    # Orchestrating pipelines polymorphically
    def process_all(self, data: Any):
        for pipeline in self.pipelines:
            pipeline.process(data)