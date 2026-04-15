from report_generator.reports import ClickbaitReport

def test_clickbait_filtering_and_sorting(sample_data):
    report = ClickbaitReport()
    result = report.generate(sample_data)
    # Ожидаем 5 записей (исключены C и G)
    assert len(result) == 5
    # Проверяем сортировку по убыванию ctr
    assert result[0]["ctr"] == 25.0
    assert result[-1]["ctr"] == 18.2
    # Проверяем, что условия выполнены для всех
    for r in result:
        assert r["ctr"] > 15
        assert r["retention_rate"] < 40