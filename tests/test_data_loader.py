import tempfile
import csv
from report_generator.data_loader import load_csv

def test_load_csv():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as f1:
        writer = csv.DictWriter(f1, fieldnames=["title","ctr","retention_rate","views"])
        writer.writeheader()
        writer.writerow({"title":"Test","ctr":"10.5","retention_rate":"50","views":"100"})
        temp_path1 = f1.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as f2:
        writer = csv.DictWriter(f2, fieldnames=["title","ctr","retention_rate","views"])
        writer.writeheader()
        writer.writerow({"title":"Test2","ctr":"12.3","retention_rate":"45","views":"200"})
        temp_path2 = f2.name

    data = load_csv([temp_path1, temp_path2])
    assert len(data) == 2
    assert data[0]["ctr"] == 10.5
    assert data[1]["retention_rate"] == 45.0