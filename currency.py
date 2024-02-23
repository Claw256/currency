"""
Currency Converter from Euros to GBP, USD, and Bitcoin

This script provides an easy-to-use currency converter that allows the user to convert an amount from euros to either
GBP, USD, or Bitcoin based on predefined conversion rates.

Author: Fearghal Hayes
Version: 1.0.1
"""

# Constants for conversion rates
CONVERSION_RATES = {
    'GBP': 0.85,
    'USD': 1.12,
    'BTC': 0.000028
}


def convert_currency(amount, currency):
    """
    Converts an amount from euros to the specified currency.

    Parameters:
        amount (float): Amount in euros to be converted.
        currency (str): Target currency for conversion.

    Returns:
        float: The converted amount in the target currency.
    """
    return amount * CONVERSION_RATES[currency]


def get_user_input():
    """
    Prompts the user to enter an amount in euros and the target currency for conversion.

    Returns:
        tuple: A tuple containing the amount in euros and the target currency.
    """
    while True:
        try:
            amount = float(input("Enter the amount in Euros: "))
            if amount < 0:
                raise ValueError("Amount must be positive.")
            currency = input("Enter the target currency (GBP, USD, BTC): ").upper()
            if currency not in CONVERSION_RATES:
                raise ValueError("Unsupported currency.")
            return amount, currency
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def main():
    """
    Main function to run the currency converter.
    """
    print("Welcome to the Currency Converter.")
    amount, currency = get_user_input()
    converted_amount = convert_currency(amount, currency)
    print(f"{amount} Euros is equivalent to {converted_amount} {currency}.")


if __name__ == "__main__":
    main()
