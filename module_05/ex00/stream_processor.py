from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # Default implementation (NO @abstractmethod)
    def format_output(self, result: str) -> str:
        return f"Output: {result}"

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            # Using try/except for validation since isinstance is not authorized yet
            _ = [float(x) for x in data]
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Invalid data"
        total = sum(data)
        return self.format_output(f"Processed numeric values, sum={total}")

# TextProcessor and LogProcessor would follow a similar structure...
class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            # Trick to check if it behaves like a string without using isinstance!
            _ = data + "" 
            return True
        except TypeError:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid data")
            
        # len() counts chars, .split() breaks the string into a list of words
        char_count = len(data)
        word_count = len(data.split())
        
        return self.format_output(f"Processed text: {char_count} characters, {word_count} words")
    
class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            # Duck typing: Does it have a split method? Does it split into at least 2 parts?
            parts = data.split(":")
            return len(parts) >= 2
        except (AttributeError, TypeError):
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.format_output("Invalid data")
            
        # Split into ['ERROR', ' Connection timeout']
        parts = data.split(":", 1) 
        level = parts[0].strip()
        message = parts[1].strip()
        
        # Specialized behavior based on the log level
        prefix = "[ALERT]" if level == "ERROR" else f"[{level}]"
        
        return self.format_output(f"{prefix} {level} level detected: {message}")