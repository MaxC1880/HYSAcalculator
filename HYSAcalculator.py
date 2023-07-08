'''
This project is a GUI calculator for a high yield savings account. 
The GUI will display 4 input boxes. An intial deposit, monthly deposit, APY yield, and years to calculate
The result will be a number at the end of the year, as well as a graph that displays the growth of the account.
Possible extras could include a bar graph or just numbers that display how much of the final amount was the initial, monthly deposit,
or interest earned.
'''
import tkinter as tk
from tkinter import Label, font, Entry
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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

def get_inputs(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error, input cannot be less than 0")
            else:
                return value
        except ValueError:
            print("Invalid input, please enter a valid number")

def display_results():
 print()

def main():
    m = tk.Tk(className="high yield savings calculator")
    m.attributes('-fullscreen', True)

    canvas = tk.Canvas(m, width=400, height=300)
    canvas.create_line(0, 120, m.winfo_screenwidth(), 120, fill="black", width=2)
    canvas.pack(fill="both", expand=True)

    title = tk.Label(m, text="High Yield Savings Calculator", font=("Georgia", 40))
    title.pack()
    screen_width = m.winfo_screenwidth()
    x_coordinate = screen_width // 2
    title.place(x=x_coordinate, y=18, anchor="n")

    initial_question = tk.Label(m, text='Initial Deposit:', font=('Times', 20))
    initial_question.place(x=8, y=170)
    initial = tk.Entry(m, width=20, font=('Arial 22'))
    initial.place(x=10, y=220)

    monthly_question = tk.Label(m, text='Monthly Deposit:', font=('Times', 20))
    monthly_question.place(x=8, y=275)
    monthly = tk.Entry(m, width=20, font=('Arial 22'))
    monthly.place(x=10, y=315)

    APY_question = tk.Label(m, text='APY:', font=('Times', 20))
    APY_question.place(x=8, y=380)
    APY = tk.Entry(m, width=20, font=('Arial 22'))
    APY.place(x=10, y=420)

    years_question = tk.Label(m, text='Years to calculate:', font=('Times', 20))
    years_question.place(x=8, y=485)
    years = tk.Entry(m, width=20, font=('Arial 22'))
    years.place(x=10, y=525)

    button = tk.Button(text="Calculate", width=10, height=4, bg="black", fg="white", command=display_results)
    button['font'] = font.Font(size=15)
    button.place(x=650, y=400)

    m.mainloop()


'''
    initial = get_inputs("Initial deposit: ")
    monthly = get_inputs("Monthly contributions: ")
    apy = get_inputs("APY percentage: ")
    years = get_inputs("Years to calculate: ")
    calculator(initial, monthly, apy, years)    
'''
main()



'''
fig = Figure(figsize=(5, 4), dpi=100)
    subplot = fig.add_subplot(111)

    # Prepare the data for the pie chart
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # Explode the second slice (optional)

    # Create the pie chart
    subplot.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    subplot.axis('equal')  # Equal aspect ratio ensures the pie is circular

    # Create a FigureCanvasTkAgg widget to display the graph in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=m)
    canvas.draw()

    # Place the graph in the Tkinter window
    canvas.get_tk_widget().pack()
    '''