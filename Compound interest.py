while (True):
    base = float(input("Base amount?"))
    interestRate = float(input("Interest rate?"))
    compound = input("Compound rate? (m/y value)")
    duration = input("Duration? (m/y value)")
    if (compound[0] == "y"):
        compound = int(compound[2:])*12
    else:
        compound = int(compound[2:])
    if (duration[0] == "y"):
        duration = int(duration[2:])*12
    else:
        duration = int(duration[2:])
    pastPayment = base;
    for x in range(duration//compound):
        thisPayment = base*(1+(interestRate*compound/12))**(x+1)
        print("Payment " + str(x) + ": " + str(thisPayment-pastPayment))
        pastPayment = thisPayment
    print(base*(1+(interestRate*compound/12))**(duration//compound))
