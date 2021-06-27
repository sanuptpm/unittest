from test_fraud_example import the_mock

from unittest.mock import patch, MagicMock

def test_is_credit_card_fraud_context_handler():
    import fraud_example

    transaction = {"amount_usd": "9999.99", "overnight_shipping": True}
    with patch("fraud_example.dark_magic", the_mock):
        is_fraud = fraud_example.is_credit_card_fraud(transaction)
    assert is_fraud == True