#Welcome user
print("Welcome to the tip calculator. ")

#Ask for total bill
total_bill = float(input("What was the total bill? $"))

#Tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

#Number of people splitting the bill
number_of_people = int(input("How many people to split the bill? "))

#Each person's share
share = round(total_bill * (1+tip_percentage/100) / number_of_people, 2)

#Format final share to 2 decimal points
final_share = "{:.2f}".format(share)

#print results
print(f"Each person should pay: ${final_share}")