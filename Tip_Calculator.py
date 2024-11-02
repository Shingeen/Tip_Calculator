print("Welcome to the Tip Calculator !")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10 15 20"))
people=int(input("How many people to split the bill? "))
bill_with_tip= tip / 100 * bill + bill
print(bill_with_tip)
bill_with_people=bill_with_tip / people
final_amount=round(bill_with_people, 2)
print(f"Each person should pay: $ {final_amount}")
input("\n\nAby zakończyć program , naciśnij klawisz enter.")