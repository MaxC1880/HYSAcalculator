'''
This project is a GUI calculator for a high yield savings account. 
The GUI will display 4 input boxes. An intial deposit, monthly deposit, APY yield, and years to calculate
The result will be a number at the end of the year, as well as a graph that displays the growth of the account.
Possible extras could include a bar graph or just numbers that display how much of the final amount was the initial, monthly deposit,
or interest earned.
'''

#Imports
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

#Make tknter window with classname and size
m = tk.Tk(className="high yield savings calculator")
m.attributes('-fullscreen', True)

#Create canvas to draw and do animations
canvas = tk.Canvas(m, width=m.winfo_screenwidth(), height=m.winfo_screenheight())
canvas.create_line(0, 120, m.winfo_screenwidth(), 120, fill="black", width=2)
canvas.pack(fill="both", expand=True)

title = tk.Label(m, text="High Yield Savings Calculator", font=("Mistral 60 bold"))
title.pack()
screen_width = m.winfo_screenwidth()
center, quarter = screen_width // 2, screen_width // 1.5
title.place(x=center, y=18, anchor="n")

initial_var, monthly_var, APY_var, years_var = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()

def calculate(initial, monthly, APY, years):
    apy_ratio = APY / 100
    total_monthly = (monthly * 12) * years
    total_months = int((years * 12))
    count = years
    contribution_interest = 0
    for i in range (0, total_months):
        contribution_interest += (monthly * apy_ratio * count)
    
    total = initial  + total_monthly + contribution_interest
    return total, contribution_interest, total_monthly

total_bal = None
error_msg = None

def display_total_balance(total, contribution_interest, initial, total_monthly ):
    global total_bal

    if total_bal:
        total_bal.config(text='Total balance is $' + str(total))
    else:
        total_bal = tk.Label(m, text='Total balance is $' + str(total), fg='green', font=('Modern', 40))
        total_bal.place(x=quarter, y=165, anchor='n')

    display_pie_graph(initial, total_monthly, contribution_interest)

def display_pie_graph(initial, total_monthly, contribution_interest):
    fig = Figure(figsize=(6, 4), dpi=110)
    subplot = fig.add_subplot(111)

    # Prepare the data for the pie chart
    labels = ['Initial', 'Contributions', 'Interest']
    sizes = [initial, total_monthly, contribution_interest]
    explode = (0.1, 0.1, 0.1)  # Explode the second slice (optional)
    colors = ('yellow', 'cyan', 'green')
    wp = { 'linewidth' : 0.5, 'edgecolor' : "red" }
    # Create the pie chart
    wedges, texts, autotexts = subplot.pie(sizes,
                                  autopct = '%1.1f%%',
                                  explode = explode,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="black"))
    subplot.axis('equal')  # Equal aspect ratio ensures the pie is circular

    #Make legend, 1st and 2nd are location, 3rd and 4th are size 
    subplot.legend(wedges, labels,
          title ="Entries",
          bbox_to_anchor=(0.18, 1.1)) 
    
    
    # Create a FigureCanvasTkAgg widget to display the graph in the Tkinter window
    piegraph = FigureCanvasTkAgg(fig, master=m)
    piegraph.draw()

    # Place the graph in the Tkinter window
    piegraph.get_tk_widget().place(x=quarter, y=300, anchor = 'n')

def display_error_message():
    global error_msg

    if error_msg:
        error_msg.config(text='Please enter a valid number')
    else:  
        error_msg = tk.Label(m, text='Please enter a valid number', fg='red', font=('Georgia', 20), anchor='center')
        error_msg.place(x=center, y=165, anchor='n')

def remove_widgets():
    global total_bal, error_msg

    if total_bal:
        total_bal.destroy()
        total_bal = None

    elif error_msg:
        error_msg.destroy()
        error_msg = None

def submit():
    remove_widgets()

    try:
        initial = float(initial_var.get())
        monthly = float(monthly_var.get())
        APY = float(APY_var.get())
        years = int(years_var.get())

        # Calculate the total balance
        total, contribution_interest, total_monthly = calculate(initial, monthly, APY, years)

        # Display the total balance
        display_total_balance(total, contribution_interest, initial, total_monthly )

    except ValueError:
        # Display the error message
        display_error_message()

def main():

    #Label the questions
    initial_question = tk.Label(m, text='Initial Deposit:', font=('Georgia', 20), anchor = 'center')
    monthly_question = tk.Label(m, text='Monthly Deposit:', font=('Georgia', 20), anchor = 'center')
    APY_question = tk.Label(m, text='APY:', font=('Georgia', 20), anchor = 'center')  
    years_question = tk.Label(m, text='Years to calculate:', font=('Georgia', 20), anchor = 'center')

    #Place the questions
    initial_question.place(x=8, y=170)
    monthly_question.place(x=8, y=275)
    APY_question.place(x=8, y=380)
    years_question.place(x=8, y=485)

    #Make the input box
    initial_box = tk.Entry(m, textvariable = initial_var,  width=20, font=('Arial 22'))
    monthly_box = tk.Entry(m, textvariable = monthly_var, width=20, font=('Arial 22'))
    APY_box= tk.Entry(m, textvariable = APY_var, width=20, font=('Arial 22'))
    years_box = tk.Entry(m, textvariable = years_var, width=20, font=('Arial 22'))

    #Place the input boxes
    initial_box.place(x=10, y=220)
    monthly_box.place(x=10, y=315)
    APY_box.place(x=10, y=420)
    years_box.place(x=10, y=525)
    
    #Make and place the button
    button = tk.Button(text="Calculate", width=20, height=5, bg="black", fg="white", font = ('Georgia', 20), command = submit)
    button.place(x=10, y=650)

    m.mainloop()


main()



