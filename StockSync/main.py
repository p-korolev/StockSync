# Does everything from the UI standpoint
# Opens tkinter UI, allows stock entry, performs graph generation

import tkinter as tk
from tkinter import ttk
from stockplot import plot

time_range_list = ['YTD', '5y', '2y', '1y', '6mo', '3mo', '1mo', 'YTD']
FIELD_WIDTH = 13
FRAME_PADDING = str(10)

def main():

    # On-click function - calls plot function
    def compare():
        stock1 = stock1_var.get()
        stock2 = stock2_var.get()
        time_range = time_var.get()
        try:
            plot(stock1, stock2, time_range)
        except IndexError and ZeroDivisionError:
            print("Error, Please try again.")

    # Creating root ui
    root = tk.Tk()
    root.title("Simple Stock Price Regression Model")
    root.geometry("350x200")
    frame = ttk.Frame(root, padding = FRAME_PADDING)
    frame.grid(row = 0, column = 0, sticky = "NSEW")

    # Creating Stock 1 entry field
    stock1_var = tk.StringVar()
    stock1_dropdown = ttk.Entry(frame, textvariable = stock1_var, width = FIELD_WIDTH)
    stock1_dropdown.grid(row = 0, column = 1, padx = 10, pady = 10)
    ttk.Label(frame, text = "Select Stock 1:").grid(row = 0, column = 0)

    # Creating Stock 2 entry field
    stock2_var = tk.StringVar()
    stock2_dropdown = ttk.Entry(frame, textvariable=stock2_var, width = FIELD_WIDTH)
    stock2_dropdown.grid(row = 1, column = 1, padx = 10, pady = 10)
    ttk.Label(frame, text = "Select Stock 2:").grid(row = 1, column = 0)

    # Creating Time Period Dropdown Menu
    time_var = tk.StringVar()
    time_var.set(time_range_list[0])
    time_range_dropdown = ttk.OptionMenu(frame, time_var, *time_range_list)
    time_range_dropdown.grid(row = 2, column = 1, padx = 10, pady = 10)
    ttk.Label(frame, text = "Period Range:").grid(row = 2, column = 0)

    # Create plot button
    plot_button = ttk.Button(frame, text = "Plot Regression", command = compare)
    plot_button.grid(row = 3, column = 0, columnspan = 2, pady = 20)

    # Run loop
    root.mainloop()

if __name__ == "__main__":
    main()