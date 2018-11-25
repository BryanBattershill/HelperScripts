while (True):
    unit = input("input unit")
    amount = float(input("value"))

    if unit == "atm":
        print("Pa", amount*101325)
        print("Bar", amount*1.01325)
    else:
        amount = amount*133.322
        print("Pa", amount)
        print("Bar", amount/100000)
