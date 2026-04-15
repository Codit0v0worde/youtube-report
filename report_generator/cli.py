import argparse
import sys
from report_generator.data_loader import load_csv
from report_generator.reports import ClickbaitReport
from report_generator.formatter import format_report

REPORTS = {
    "clickbait": ClickbaitReport,
}

def main():
    parser = argparse.ArgumentParser(description="Генератор отчётов по метрикам YouTube.")
    parser.add_argument("--files", nargs="+", required=True, help="Пути к CSV файлам")
    parser.add_argument("--report", required=True, choices=REPORTS.keys(), help="Тип отчёта")
    args = parser.parse_args()

    try:
        data = load_csv(args.files)
    except Exception as e:
        print(f"Ошибка при чтении файлов: {e}", file=sys.stderr)
        sys.exit(1)

    report_class = REPORTS[args.report]
    report = report_class()
    result = report.generate(data)

    print(format_report(result))

if __name__ == "__main__":
    main()
