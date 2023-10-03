import tkinter as tk

class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking App")
        
        # Initialize balance
        self.balance = 1000
        
        # Create balance label
        self.balance_label = tk.Label(root, text="Balance: #1000")
        self.balance_label.pack()
        
        # Create entry for deposit/withdraw amount
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()
        
        # Create deposit and withdraw buttons
        deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        
        deposit_button.pack()
        withdraw_button.pack()

    def update_balance_label(self):
        self.balance_label.config(text="Balance: #" + str(self.balance))

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            self.balance += amount
            self.update_balance_label()
        except ValueError:
            # Handle invalid input
            print("Invalid input!")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if self.balance >= amount:
                self.balance -= amount
                self.update_balance_label()
            else:
                # Handle insufficient balance
                print("Insufficient balance!")
        except ValueError:
            # Handle invalid input
            print("Invalid input!")

# Create the main application window
root = tk.Tk()
app = BankApp(root)

# Run the Tkinter main loop
root.mainloop()
