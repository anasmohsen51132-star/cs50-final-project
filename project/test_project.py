import pytest
from project import add_swimmer, mark_paid, unpaid_swimmers


def test_add_swimmer():
    swimmers = []
    s = add_swimmer(swimmers, "  Ahmed ", "12", "Saturday", "17:00")
    assert s["name"] == "Ahmed"
    assert s["age"] == 12
    assert s["training_day"] == "saturday"
    assert s["training_time"] == "17:00"
    assert s["paid"] is False
    assert 1000 <= s["id"] <= 9999
    assert swimmers == [s]


def test_add_swimmer_unique_ids():
    swimmers = []
    for i in range(50):
        add_swimmer(swimmers, f"Swimmer{i}", 10, "monday", "16:30")
    ids = [s["id"] for s in swimmers]
    assert len(ids) == len(set(ids))


def test_add_swimmer_invalid():
    swimmers = []
    with pytest.raises(ValueError):
        add_swimmer(swimmers, "   ", 12, "saturday", "17:00")
    with pytest.raises(ValueError):
        add_swimmer(swimmers, "Ali", "abc", "saturday", "17:00")
    with pytest.raises(ValueError):
        add_swimmer(swimmers, "Ali", None, "saturday", "17:00")
    with pytest.raises(ValueError):
        add_swimmer(swimmers, "Ali", 2, "saturday", "17:00")
    with pytest.raises(ValueError):
        add_swimmer(swimmers, "Ali", 100, "saturday", "17:00")
    with pytest.raises(ValueError):
        add_swimmer(swimmers, "Ali", 12, "funday", "17:00")
    with pytest.raises(ValueError):
        add_swimmer(swimmers, "Ali", 12, "saturday", "25:00")
    with pytest.raises(ValueError):
        add_swimmer(swimmers, "Ali", 12, "saturday", "5pm")
    assert swimmers == []


def test_mark_paid():
    swimmers = []
    a = add_swimmer(swimmers, "Ahmed", 12, "saturday", "17:00")
    b = add_swimmer(swimmers, "Sara", 10, "monday", "16:30")
    result = mark_paid(swimmers, b["id"])
    assert result is b
    assert b["paid"] is True
    assert a["paid"] is False


def test_mark_paid_not_found():
    swimmers = []
    a = add_swimmer(swimmers, "Ahmed", 12, "saturday", "17:00")
    with pytest.raises(ValueError):
        mark_paid(swimmers, a["id"] + 1)
    with pytest.raises(ValueError):
        mark_paid([], 1234)
    assert a["paid"] is False


def test_unpaid_swimmers():
    swimmers = []
    a = add_swimmer(swimmers, "Ahmed", 12, "saturday", "17:00")
    b = add_swimmer(swimmers, "Sara", 10, "monday", "16:30")
    c = add_swimmer(swimmers, "Omar", 14, "friday", "18:00")
    mark_paid(swimmers, b["id"])
    result = unpaid_swimmers(swimmers)
    assert result == [a, c]
    assert len(swimmers) == 3


def test_unpaid_swimmers_edge_cases():
    assert unpaid_swimmers([]) == []
    swimmers = []
    a = add_swimmer(swimmers, "Ahmed", 12, "saturday", "17:00")
    mark_paid(swimmers, a["id"])
    assert unpaid_swimmers(swimmers) == []