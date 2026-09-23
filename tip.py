def tip_calculator():
    bill=float(input("How much was your bill?"))
    service_unformatted=input("How would you rate your service, using 'bad', 'okay', 'good', or 'great'?")
    service = service_unformatted.lower()

    if service == "bad":
        print("You should tip absolutely 0 dollars!")
    elif service == "okay":
        print(f"You should tip {bill*0.15} dollars.")
    elif service == "good":
        print(f"You should tip {bill*0.20} dollars.")
    elif service == "great":
        print(f"You should tip {bill*0.25} dollars.")
    else:
        print("Not an accepted answer, restart program to try again.")

tip_calculator()