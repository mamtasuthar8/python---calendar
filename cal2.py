import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Python Calendar")
root.geometry("700x650")
root.configure(bg="#1e293b")

# ---------------- CURRENT DATE ----------------
today = datetime.now()
current_day = today.day
current_month = today.month
current_year = today.year

# ---------------- FUNCTION ----------------
def show_calendar():

    month = month_entry.get()
    year = year_entry.get()

    if month == "" or year == "":
        messagebox.showerror("Error", "Please Enter Month and Year")
        return

    try:
        month = int(month)
        year = int(year)

        if month < 1 or month > 12:
            messagebox.showerror("Error", "Month must be between 1 and 12")
            return

        # Clear old calendar
        text_area.delete("1.0", tk.END)

        # Month Name
        month_name = calendar.month_name[month]

        # Heading
        heading = f"{month_name} {year}\n"
        text_area.insert(tk.END, heading.center(30))

        # Days Heading
        days = "Mo Tu We Th Fr Sa Su\n"
        text_area.insert(tk.END, days)

        # Month Calendar
        cal = calendar.monthcalendar(year, month)

        for week in cal:

            line = ""

            for day in week:

                if day == 0:
                    line += "   "

                elif (day == current_day and
                      month == current_month and
                      year == current_year):

                    # Highlight current date
                    line += f"[{day:2}]"

                else:
                    line += f"{day:2} "

            line += "\n"

            text_area.insert(tk.END, line)

    except:
        messagebox.showerror("Error", "Invalid Input")


# ---------------- HEADING ----------------
heading = tk.Label(
    root,
    text="📅 PYTHON CALENDAR",
    font=("Arial", 24, "bold"),
    bg="#2563eb",
    fg="gray",
    pady=10
)

heading.pack(fill="x")

# ---------------- INPUT FRAME ----------------
frame = tk.Frame(root, bg="#1e293b")
frame.pack(pady=20)

# Month Label
month_label = tk.Label(
    frame,
    text="Enter Month:",
    font=("Arial", 14),
    bg="#1e293b",
    fg="gray"
)

month_label.grid(row=0, column=0, padx=10)

# Month Entry
month_entry = tk.Entry(
    frame,
    font=("Arial", 14),
    width=10,
    justify="center"
)

month_entry.grid(row=0, column=1, padx=10)

# Year Label
year_label = tk.Label(
    frame,
    text="Enter Year:",
    font=("Arial", 14),
    bg="#1e293b",
    fg="gray"
)

year_label.grid(row=0, column=2, padx=10)

# Year Entry
year_entry = tk.Entry(
    frame,
    font=("Arial", 14),
    width=10,
    justify="center"
)

year_entry.grid(row=0, column=3, padx=10)

# ---------------- BUTTON ----------------
show_btn = tk.Button(
    root,
    text="Show Calendar",
    font=("Arial", 14, "bold"),
    bg="#22c55e",
    fg="gray",
    padx=20,
    pady=8,
    bd=0,
    cursor="hand2",
    command=show_calendar
)

show_btn.pack(pady=10)

# ---------------- TEXT AREA ----------------
text_area = tk.Text(
    root,
    width=35,
    height=15,
    font=("Courier New", 20, "bold"),
    bg="gray",
    fg="black",
    padx=20,
    pady=20
)

text_area.pack(pady=20)

# ---------------- FOOTER ----------------
footer = tk.Label(
    root,
    text="Created Using Python Tkinter",
    font=("Arial", 11),
    bg="#1e293b",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

# ---------------- RUN APP ----------------
root.mainloop()
