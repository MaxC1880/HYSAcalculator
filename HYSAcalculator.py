'''
This project is a GUI calculator for a high yield savings account. 
The GUI will display 4 input boxes. An intial deposit, monthly deposit, APY yield, and years to calculate
The result will be a number at the end of the year, as well as a graph that displays the growth of the account.
Possible extras could include a bar graph or just numbers that display how much of the final amount was the initial, monthly deposit,
or interest earned.
'''




def calculator(initial, monthly, APY, years):
    total_bal = 0
    apy_ratio = APY / 100
    monthly_contribute = monthly * (years * 12)

    contribution_interest = 0
    months_count = (years * 12)

    for i in (0, (years * 12)):
        contribution_interest += (monthly * apy_ratio * months_count)
        months_count -= 1
    
    total_bal = initial  + monthly_contribute + contribution_interest
    printResults(initial, monthly, APY, years, total_bal)


def printResults(initial, monthly, APY, years, total_bal):
    print('\nYour initial deposit was: $' + str(initial) + '\nYour monthly contributions were: $' + str(monthly) + '\nYour APY was: ' + str(APY) + '%' +  
          '\nYour years looking to calcualte was: ' + str(years) + ' years \nYour total balance in your savings after ' + str(years) + ' years is: $' + str(total_bal))

def main():

    while True:
        try:
            initial = float (input ('Initial deposit: '))
            monthly = float (input ('Monthly Contribution: '))
            apy = float (input ('APY: '))
            years = int (input ('Years (in whole numebrs): '))
            break
            

        except(ValueError):
            print('Wrong input try again\n')
        

    calculator(initial, monthly, apy, years)


main()