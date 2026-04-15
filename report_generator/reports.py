from abc import ABC, abstractmethod
from typing import List, Dict

class BaseReport(ABC):
    """Базовый класс для всех отчётов."""

    @abstractmethod
    def generate(self, data: List[Dict]) -> List[Dict]:
        pass

class ClickbaitReport(BaseReport):
    """Отчёт о кликбейтных видео: ctr > 15, retention_rate < 40."""

    def generate(self, data: List[Dict]) -> List[Dict]:
        filtered = [
            item for item in data
            if item['ctr'] > 15 and item['retention_rate'] < 40
        ]
        sorted_data = sorted(filtered, key=lambda x: x['ctr'], reverse=True)
        return sorted_data
