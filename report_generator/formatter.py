from tabulate import tabulate
from typing import List, Dict

def format_report(rows: List[Dict]) -> str:
    """Форматирует список записей в таблицу с колонками title, ctr, retention_rate."""
    if not rows:
        return "Нет видео, удовлетворяющих условиям."
    headers = ["title", "ctr", "retention_rate"]
    table = [[row[h] for h in headers] for row in rows]
    return tabulate(table, headers=headers, tablefmt="grid", floatfmt=".2f")
