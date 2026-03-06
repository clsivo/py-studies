"""
Real-time currency converter utilizing the AwesomeAPI to fetch live 
exchange rates. Features a dynamic user interface with session 
management and real-time JSON data parsing for BRL pairs.
"""

import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL"

response = requests.get(url)
data = response.json()

usd_rate = float(data['USDBRL']['bid'])
eur_rate = float(data['EURBRL']['bid'])
gbp_rate = float(data['GBPBRL']['bid'])

while True:
    print("==================")
    print("Currency Converter")
    print("==================")
    print("1) USD - US Dollar")
    print("2) EUR - Euro")
    print("3) GBP - British Pound")
    print("4) Exit")

    choice = int(input("\nSelect the currency you want to convert to BRL (1, 2, 3 or 4): "))

    if choice == 4:
        print("\nExiting the program. Goodbye!")
        break
    
    brl_amount = float(input("\nEnter the amount in BRL: "))

    if choice == 1:
        converted_amount = brl_amount / usd_rate
        print(f"\nR${brl_amount:.2f} is equal to ${converted_amount:.2f}")
        print("\nDo you wanna a new conversion? (yes/no)")
        answer = input().lower()
        if answer == "no":
            print("\nExiting the program. Goodbye!")
            break
        elif answer == "yes":
            continue
        else: 
            print("\nInvalid input. Exiting the program. Goodbye!")
            break

    elif choice == 2:
        converted_amount = brl_amount / eur_rate
        print(f"\nR${brl_amount:.2f} is equal to €{converted_amount:.2f}")
        print("\nDo you wanna a new conversion? (yes/no)")
        answer = input().lower()
        if answer == "no":
            print("\nExiting the program. Goodbye!")
            break
        elif answer == "yes":
            continue
        else: 
            print("\nInvalid input. Exiting the program. Goodbye!")
            break

    elif choice == 3:
        converted_amount = brl_amount / gbp_rate
        print(f"\nR${brl_amount:.2f} is equal to £{converted_amount:.2f}")
        print("\nDo you wanna a new conversion? (yes/no)")
        answer = input().lower()
        if answer == "no":
            print("\nExiting the program. Goodbye!")
            break
        elif answer == "yes":
            continue
        else: 
            print("\nInvalid input. Exiting the program. Goodbye!")
            break