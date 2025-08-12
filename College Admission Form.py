import tkinter as tk
from tkinter import messagebox

def submit_form():
    
    name = e1.get()
    age = e2.get()
    course = e3.get()
    phone_number = e4.get()
    selected_city = e5.get()
    
    
    if not name or not age or not course or not phone_number or not selected_city:
        messagebox.showwarning("Input Error", "Please fill all fields")
        return
    
    
    form_data = f"Name: {name}\nAge: {age}\nCourse: {course}\nPhone Number: {phone_number}\nCity: {selected_city}"
    messagebox.showinfo("Form Submitted", form_data)


window = tk.Tk()
window.title("College Admission Form")



l1 = tk.Label(window, text="Full Name:")
l1.grid(row=0, column=0, padx=10, pady=30)
e1 = tk.Entry(window,width=40)
e1.grid(row=0, column=1)

l2 = tk.Label(window, text="Age:")
l2.grid(row=1, column=0, padx=10, pady=30)
e2 = tk.Entry(window, width=40)
e2.grid(row=1, column=1)

l3 = tk.Label(window, text="Course:")
l3.grid(row=2, column=0, padx=10, pady=30)
e3 = tk.StringVar()
dropdown = tk.OptionMenu(window, e3, "Computer Science", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering", "Other")
dropdown.grid(row=2, column=1, padx=20, pady=10)

l4 = tk.Label(window, text="Phone Number:")
l4.grid(row=3, column=0, padx=10, pady=30)
e4 = tk.Entry(window, width=40)
e4.grid(row=3, column=1)


l5 = tk.Label(window, text="Select your city:")
l5.grid(row=4, column=0, sticky="w", padx=10, pady=30)

e5 = tk.StringVar()

r1 = tk.Radiobutton(window, text="Kalyan", variable=e5, value="Kalyan")
r1.grid(row=4, column=1, sticky="w", padx=10, pady=10)

r2 = tk.Radiobutton(window, text="Dombivali", variable=e5, value="Dombivali")
r2.grid(row=5, column=1, sticky="w", padx=10, pady=10)

r3 = tk.Radiobutton(window, text="Thane", variable=e5, value="Thane")
r3.grid(row=6, column=1, sticky="w", padx=10, pady=10)


b1 = tk.Button(window, text="Submit", width=10, command=submit_form)
b1.grid(row=7, column=1, sticky="w" , padx=5, pady=20)


window.mainloop()