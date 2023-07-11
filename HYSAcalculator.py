'''
This project is a GUI calculator for a high yield savings account. 
The GUI will display 4 input boxes. An intial deposit, monthly deposit, APY yield, and years to calculate
The result will be a number at the end of the year, as well as a graph that displays the growth of the account.
Possible extras could include a bar graph or just numbers that display how much of the final amount was the initial, monthly deposit,
or interest earned.
'''
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

m = tk.Tk(className="high yield savings calculator")
m.attributes('-fullscreen', True)

canvas = tk.Canvas(m, width=400, height=300)
canvas.create_line(0, 120, m.winfo_screenwidth(), 120, fill="black", width=2)
canvas.pack(fill="both", expand=True)

title = tk.Label(m, text="High Yield Savings Calculator", font=("Mistral 60 bold"))
title.pack()
screen_width = m.winfo_screenwidth()
x_coordinate = screen_width // 2
title.place(x=x_coordinate, y=18, anchor="n")

initial_var = tk.StringVar()
monthly_var = tk.StringVar()
APY_var = tk.StringVar()
years_var = tk.StringVar()

def submit():
 
    initial = initial_var.get()
    monthly=monthly_var.get()
    APY = APY_var.get()
    years = years_var.get()
     
    print("The initial is : " + initial)
    #initial_question = tk.Label(m, text='Initial Deposit:', font=('Times', 20))
    #initial_question.place(x=400, y=170)
    #initial_question = tk.Label(m, text=initial, font=('Times', 20))
    #initial_question.place(x=550, y=170) 

def main():

    '''Label the questions'''
    initial_question = tk.Label(m, text='Initial Deposit:', font=('Georgia', 20), anchor = 'center')
    monthly_question = tk.Label(m, text='Monthly Deposit:', font=('Georgia', 20), anchor = 'center')
    APY_question = tk.Label(m, text='APY:', font=('Georgia', 20), anchor = 'center')  
    years_question = tk.Label(m, text='Years to calculate:', font=('Georgia', 20), anchor = 'center')

    '''Place the questions'''
    initial_question.place(x=8, y=170)
    monthly_question.place(x=8, y=275)
    APY_question.place(x=8, y=380)
    years_question.place(x=8, y=485)

    '''Make the input box'''
    initial_box = tk.Entry(m, textvariable = initial_var,  width=20, font=('Arial 22'))
    monthly_box = tk.Entry(m, textvariable = monthly_var, width=20, font=('Arial 22'))
    APY_box= tk.Entry(m, textvariable = APY_var, width=20, font=('Arial 22'))
    years_box = tk.Entry(m, textvariable = years_var, width=20, font=('Arial 22'))

    '''Place the input boxes'''
    initial_box.place(x=10, y=220)
    monthly_box.place(x=10, y=315)
    APY_box.place(x=10, y=420)
    years_box.place(x=10, y=525)

    button = tk.Button(text="Bar Graph", width=20, height=5, bg="black", fg="white", font = ('Georgia', 20), command = submit)
    button.place(x=10, y=650)

    m.mainloop()


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