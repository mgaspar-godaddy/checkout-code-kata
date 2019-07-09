import pytest
from unittest.mock import MagicMock
from checkout import Checkout
from exceptions import ItemHasNoPriceError

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    return checkout

@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.__enter__.return_value.__iter__.return_value = ["c 3"]
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open

def test_calculate_total(checkout):
    checkout.add_item("a")
    assert checkout.calculate_total() == 1

def test_get_correct_total_for_multiple_items(checkout):
    checkout.add_item("a")
    checkout.add_item("b")
    assert checkout.calculate_total() == 3

def test_add_discount_rules(checkout):
    checkout.add_discount("a", 3, 2)

def test_apply_discount_rules(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")
    assert checkout.calculate_total() == 2

def test_calculate_total_without_discount(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    assert checkout.calculate_total() == 2

def test_add_item_without_price(checkout):
    with pytest.raises(ItemHasNoPriceError) as e:
        checkout.add_item("c")
    assert "Item c has no price" in str(e.value)

def test_read_prices_from_file(checkout, mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    checkout.get_prices("test_file")
    checkout.add_item("c")
    result = checkout.calculate_total()
    mock_open.assert_called_once_with("test_file", "r")
    assert result == 3

def test_read_from_file_exception(checkout, mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with pytest.raises(FileNotFoundError) as e:
        checkout.get_prices("test_file")
        print(str(e.value))
