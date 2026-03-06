"""
Offline-capable currency converter powered by the 'currency_converter' 
library. Demonstrates efficient use of local data sets and clean 
control flow for multi-source conversions to USD.
"""

from currency_converter import CurrencyConverter

c = CurrencyConverter()

while True:
    print("==================")
    print("Currency Converter")
    print("==================")
    print("1) BRL (Brazilian Real) to USD (US Dollar)")
    print("2) EUR (Euro) to USD (US Dollar)")
    print("3) GBP (British Pound) to USD (US Dollar)")
    print("0) Exit")

    choice = int(input("Select the option you want from (1-4): "))

    # Check if the user wants to exit the program or if they have entered an invalid option
    if choice == 0:
        print("Exiting the program. Goodbye!")
        break
    if choice < 0 or choice > 3:
        print("Invalid option. Please select a valid option (1-4).\n")
        continue
    
    amount = float(input("Amount in BRL (R$) you want to convert: "))

    if choice == 1:
        converted = c.convert(amount, 'BRL', 'USD')
    elif choice == 2:
        converted = c.convert(amount, 'EUR', 'USD')
    elif choice == 3:
        converted = c.convert(amount, 'GBP', 'USD')

    print(f"\nConverted amount: U$ {converted:.2f} USD\n")