'''
This project is a GUI calculator for a high yield savings account. 
The GUI will display 4 input boxes. An intial deposit, monthly deposit, APY yield, and years to calculate
The result will be a number at the end of the year, as well as a graph that displays the growth of the account.
Possible extras could include a bar graph or just numbers that display how much of the final amount was the initial, monthly deposit,
or interest earned.
'''
import tkinter

def calculator(initial, monthly, APY, years):
    apy_ratio = APY / 100
    total_monthly = (monthly * 12) * years
    total_months = int((years * 12))
    count = years

    contribution_interest = 0

    for i in range (0, total_months):
        contribution_interest += (monthly * apy_ratio * count)
    
    total_bal = initial  + total_monthly + contribution_interest
    printResults(initial, monthly, APY, years, total_bal)



def printResults(initial, monthly, APY, years, total_bal):
    print('\nYour initial deposit was: $' + str(initial) + '\nYour monthly contributions were: $' + str(monthly) + '\nYour APY was: ' + str(APY) + '%' +  
          '\nYour years looking to calcualte was: ' + str(years) + ' years \nYour total balance in your savings after ' + str(years) + ' years is: $' + str(total_bal))

def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error, input cannot be less than 0")
            else:
                return value
        except ValueError:
            print("Invalid input, please enter a valid number")

initial = get_positive_float_input("Initial deposit: ")
monthly = get_positive_float_input("Monthly contributions: ")
apy = get_positive_float_input("APY percentage: ")
years = get_positive_float_input("Years to calculate: ")

        
def main():
    calculator(initial, monthly, apy, years)    

main()

