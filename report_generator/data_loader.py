import csv
from typing import List, Dict

def load_csv(file_paths: List[str]) -> List[Dict]:
    """Загружает данные из нескольких CSV файлов и возвращает список словарей."""
    all_rows = []
    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['ctr'] = float(row['ctr'])
                row['retention_rate'] = float(row['retention_rate'])
                all_rows.append(row)
    return all_rows
