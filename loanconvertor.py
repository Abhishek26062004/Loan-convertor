from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry, Frame
import tkinter.font as tkFont
import math

class LoanCalculator():
    def _init_(self):
        window = Tk()
        window.title("Loan Calculator App")
        window.geometry("500x700")
        window.configure(bg="#d4e0e6")
        window.resizable(width=False, height=False)

        # Custom font
        custom_font = tkFont.Font(family="Helvetica", size=14, weight="bold")

        self.loan_amount = StringVar()
        self.interest_rate = StringVar()
        self.loan_term = IntVar()
        self.monthly_payment = StringVar()
        self.total_payment = StringVar()

        # Create frames for 3D effect
        top_frame = Frame(window, bg="#d4e0e6", bd=5, relief="raised")
        top_frame.pack(pady=20, padx=20, fill="both")

        middle_frame = Frame(window, bg="#d4e0e6", bd=5, relief="raised")
        middle_frame.pack(pady=20, padx=20, fill="both")

        bottom_frame = Frame(window, bg="#d4e0e6", bd=5, relief="raised")
        bottom_frame.pack(pady=20, padx=20, fill="both")

        # Loan Amount label
        loan_amount_label = Label(top_frame, text="Loan Amount", bg="#1e90ff", fg="white", font=custom_font, relief="solid", padx=10, pady=5, bd=3)
        loan_amount_label.grid(column=0, row=0, padx=15, pady=5)

        # Loan Amount entry
        loan_amount_entry = Entry(top_frame, textvariable=self.loan_amount, width=18, relief="sunken", bd=3, font=custom_font)
        loan_amount_entry.grid(column=1, row=0, padx=15, pady=5)

        # Interest Rate label
        interest_rate_label = Label(top_frame, text="Interest Rate (%)", bg="#1e90ff", fg="white", font=custom_font, relief="solid", padx=10, pady=5, bd=3)
        interest_rate_label.grid(column=0, row=1, padx=15, pady=5)

        # Interest Rate entry
        interest_rate_entry = Entry(top_frame, textvariable=self.interest_rate, width=18, relief="sunken", bd=3, font=custom_font)
        interest_rate_entry.grid(column=1, row=1, padx=15, pady=5)

        # Loan Term label
        loan_term_label = Label(top_frame, text="Loan Term (Years)", bg="#1e90ff", fg="white", font=custom_font, relief="solid", padx=10, pady=5, bd=3)
        loan_term_label.grid(column=0, row=2, padx=15, pady=5)

        # Loan Term entry
        loan_term_entry = Entry(top_frame, textvariable=self.loan_term, width=18, relief="sunken", bd=3, font=custom_font)
        loan_term_entry.grid(column=1, row=2, padx=15, pady=5)

        # Monthly Payment label
        monthly_payment_lbl = Label(bottom_frame, text="Monthly Payment $", bg="#3cb371", fg="white", font=custom_font, relief="solid", padx=10, pady=5, bd=3)
        monthly_payment_lbl.grid(column=0, row=0, padx=15, pady=5)

        # Monthly Payment entry
        monthly_payment_entry = Entry(bottom_frame, textvariable=self.monthly_payment, width=18, relief="sunken", bd=3, font=custom_font)
        monthly_payment_entry.grid(column=1, row=0, padx=15, pady=5)

        # Total Payment label
        total_payment_lbl = Label(bottom_frame, text="Total Payment $", bg="#3cb371", fg="white", font=custom_font, relief="solid", padx=10, pady=5, bd=3)
        total_payment_lbl.grid(column=0, row=1, padx=15, pady=5)

        # Total Payment entry
        total_payment_entry = Entry(bottom_frame, textvariable=self.total_payment, width=18, relief="sunken", bd=3, font=custom_font)
        total_payment_entry.grid(column=1, row=1, padx=15, pady=5)

        # Calculate button
        calculate_btn = Button(bottom_frame, text="Calculate", bg="#32cd32", fg="white", command=self.calculate, relief="raised", padx=10, pady=5, bd=3, font=custom_font)
        calculate_btn.grid(column=0, row=2, padx=15, pady=15, columnspan=2)

        # Clear button
        clear_btn = Button(bottom_frame, text="Clear", bg="#ff4500", fg="white", command=self.clear, relief="raised", padx=10, pady=5, bd=3, font=custom_font)
        clear_btn.grid(column=1, row=2, padx=15, pady=15, columnspan=2)

        window.mainloop()

    def calculate(self):
        try:
            principal = float(self.loan_amount.get())
            annual_rate = float(self.interest_rate.get()) / 100
            monthly_rate = annual_rate / 12
            term_years = int(self.loan_term.get())
            term_months = term_years * 12

            # Calculate monthly payment using the formula:
            # M = P[r(1+r)^n] / [(1+r)^n – 1]
            if monthly_rate != 0:
                monthly_payment = principal * (monthly_rate * math.pow(1 + monthly_rate, term_months)) / (math.pow(1 + monthly_rate, term_months) - 1)
            else:
                monthly_payment = principal / term_months

            total_payment = monthly_payment * term_months

            self.monthly_payment.set(f"{monthly_payment:.2f}")
            self.total_payment.set(f"{total_payment:.2f}")
        except ValueError:
            self.monthly_payment.set("Invalid input")
            self.total_payment.set("Invalid input")

    def clear(self):
        self.loan_amount.set("")
        self.interest_rate.set("")
        self.loan_term.set(0)
        self.monthly_payment.set("")
        self.total_payment.set("")

LoanCalculator()