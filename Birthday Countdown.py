import tkinter as tk
from datetime import datetime

def calculate_days_left():
    date_str = entry.get()
    birthday = datetime.strptime(date_str, "%d-%m-%Y")
    today = datetime.now()
    
   
    birthday = birthday.replace(year=today.year)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        
    remaining = birthday - today
    result_label.config(text=f"Days left for birthday: {remaining.days}")


window = tk.Tk()
window.title("Birthday Countdown")
window.geometry("300x200")


label = tk.Label(window, text="Enter your birthday (DD-MM-YYYY):")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Calculate Days", command=calculate_days_left)
button.pack(pady=10)


result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()