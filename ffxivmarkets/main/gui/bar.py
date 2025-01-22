from ffxivmarkets.main.db.data_processor import calculate_daily_profits, plot_profit_barchart
from ffxivmarkets.main.db.db_connector import connect_to_database, fetch_sales_data_w_days
import tkinter as tk
from tkinter import ttk


def refresh_barchart(days_ago):
    conn = connect_to_database()
    sales_data = fetch_sales_data_w_days(conn, days_ago)
    conn.close()
    daily_profits, item_names = calculate_daily_profits(sales_data)
    plot_profit_barchart(daily_profits, item_names)


def on_enter(event):
    try:
        days_ago = int(days_entry.get())
        refresh_barchart(days_ago)
    except ValueError:
        error_label.config(text="Please enter a valid number.")


def mainBars():
    root = tk.Tk()
    root.title("Sales Data Viewer")

    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text="Days Ago:").grid(row=0, column=0, sticky=tk.W)

    global days_entry
    days_entry = ttk.Entry(frame, width=10)
    days_entry.grid(row=0, column=1)
    days_entry.bind("<Return>", on_enter)

    global error_label
    error_label = ttk.Label(frame, text="", foreground="red")
    error_label.grid(row=1, columnspan=2)

    ttk.Label(frame, text="Press Enter to refresh the bar chart.").grid(row=2, columnspan=2)

    root.mainloop()
