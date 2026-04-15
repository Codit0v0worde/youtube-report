import pytest

@pytest.fixture
def sample_data():
    return [
        {"title": "Video A", "ctr": 18.2, "retention_rate": 35.0},
        {"title": "Video B", "ctr": 22.5, "retention_rate": 28.0},
        {"title": "Video C", "ctr": 9.5, "retention_rate": 82.0},   # не подходит (ctr <= 15)
        {"title": "Video D", "ctr": 25.0, "retention_rate": 22.0},
        {"title": "Video E", "ctr": 19.0, "retention_rate": 38.0},
        {"title": "Video F", "ctr": 21.0, "retention_rate": 35.0},
        {"title": "Video G", "ctr": 16.5, "retention_rate": 42.0},   # не подходит (retention >= 40)
    ]