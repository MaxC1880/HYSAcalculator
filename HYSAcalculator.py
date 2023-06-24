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
    month_contribute = monthly * years 
    intial_interest = initial * apy_ratio

    contribution_interest = 0
    years_count = years
    
    for i in years:
        contribution_interest += (monthly * apy_ratio) * years_count
        years_count -= 1


    #End balance is intial contribution + total monthly contribution + initial interest + monthly contribution interest


def main():

    while True:
        try:
            initial = float (input ('Initial deposit: '))
            monthly = float (input ('Monthly Contribution: '))
            apy = float (input ('APY: '))
            years = float (input ('Years: '))
            break
            

        except(ValueError):
            print('Wrong')
        

    calculator(initial, monthly, apy, years)


main()