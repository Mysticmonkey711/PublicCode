''' Type your code here. '''
'''Going to modulo inputs down decrimenting by change value'''
input_amount = 45 #int(input())
if input_amount <= 0:
    print('No change')
else:
    Quarter_Remainder = input_amount % 100
    Dollars = (input_amount - Quarter_Remainder) / 100
    if Dollars > 0:
        if Dollars == 1:
            print(int(Dollars), "Dollar")
        else:
            print(int(Dollars), "Dollars")

    Dime_Remainder = Quarter_Remainder % 25
    Quarters = (Quarter_Remainder - Dime_Remainder) / 25
    if Quarters > 0:
        if Quarters == 1:
            print(int(Quarters), "Quarter")
        else:
            print(int(Quarters), "Quarters")

    Nickel_Remainder = Dime_Remainder % 10
    Dimes = (Dime_Remainder - Nickel_Remainder) / 10
    if Dimes > 0:
        if Dimes == 1:
            print(int(Dimes), "Dime")
        else:
            print(int(Dimes), "Dimes")

    Penny_Remainder = Nickel_Remainder % 5
    Nickels = (Nickel_Remainder - Penny_Remainder) / 5
    if Nickels > 0:
        if Nickels == 1:
            print(int(Nickels), "Nickel")
        else:
            print(int(Nickels), "Nickels")

    Final_Remainder = Penny_Remainder % 1
    Pennies = (Penny_Remainder - Final_Remainder) / 1
    if Pennies > 0:
        if Pennies == 1:
            print(int(Pennies), "Penny")
        else:
            print(int(Pennies), "Pennies")