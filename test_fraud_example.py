from unittest.mock import patch, MagicMock


def the_mock(input):
    return 0.999


@patch("fraud_example.dark_magic", the_mock)
def test_is_credit_card_fraud():
    import fraud_example

    transaction = {"amount_usd": "9999.99", "overnight_shipping": True}
    is_fraud = fraud_example.is_credit_card_fraud(transaction)
    assert is_fraud == True