import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # API key (free tier from exchangerate-api.com)
        self.API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
        self.BASE_URL = f"https://v6.exchangerate-api.com/v6/{self.API_KEY}/latest/"
        
        # Variables
        self.currencies = []
        self.exchange_rates = {}
        self.last_update = ""
        
        # Create UI
        self.create_widgets()
        
        # Load currencies
        self.load_currencies()
    
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#4a7a8c")
        header_frame.pack(fill="x")
        
        tk.Label(
            header_frame,
            text="Currency Converter",
            font=("Arial", 20, "bold"),
            bg="#4a7a8c",
            fg="white",
            padx=10,
            pady=10
        ).pack()
        
        # Main content
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill="both")
        
        # Amount input
        tk.Label(main_frame, text="Amount:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
        self.amount_entry = tk.Entry(main_frame, font=("Arial", 12), width=15)
        self.amount_entry.grid(row=0, column=1, sticky="w", pady=5)
        
        # From currency
        tk.Label(main_frame, text="From:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
        self.from_currency = ttk.Combobox(main_frame, font=("Arial", 12), width=12, state="readonly")
        self.from_currency.grid(row=1, column=1, sticky="w", pady=5)
        
        # To currency
        tk.Label(main_frame, text="To:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", pady=5)
        self.to_currency = ttk.Combobox(main_frame, font=("Arial", 12), width=12, state="readonly")
        self.to_currency.grid(row=2, column=1, sticky="w", pady=5)
        
        # Convert button
        convert_btn = tk.Button(
            main_frame,
            text="Convert",
            font=("Arial", 12, "bold"),
            bg="#4a7a8c",
            fg="white",
            command=self.convert_currency
        )
        convert_btn.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Result
        self.result_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 14, "bold"),
            fg="#4a7a8c"
        )
        self.result_label.grid(row=4, column=0, columnspan=2)
        
        # Last update
        self.update_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 8),
            fg="gray"
        )
        self.update_label.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Swap button
        swap_btn = tk.Button(
            main_frame,
            text="Swap Currencies",
            font=("Arial", 10),
            command=self.swap_currencies
        )
        swap_btn.grid(row=6, column=0, columnspan=2, pady=5)
    
    def load_currencies(self):
        """Load available currencies from API"""
        try:
            # For a real project, you would fetch this from the API
            # This is a sample list - you can add more currencies
            self.currencies = [
                "USD", "EUR", "GBP", "JPY", "AUD", "CAD", 
                "CHF", "CNY", "INR", "SGD", "MYR", "AED"
            ]
            
            self.from_currency['values'] = self.currencies
            self.to_currency['values'] = self.currencies
            
            # Set default values
            self.from_currency.set("USD")
            self.to_currency.set("EUR")
            
            # Get initial exchange rates
            self.get_exchange_rates("USD")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load currencies: {str(e)}")
    
    def get_exchange_rates(self, base_currency):
        """Fetch exchange rates from API"""
        try:
            # In a real application, you would make an API call here
            # For this example, we'll use some hardcoded rates
            
            # Sample exchange rates (these would normally come from the API)
            sample_rates = {
                "USD": 1.0,
                "EUR": 0.93,
                "GBP": 0.80,
                "JPY": 151.53,
                "AUD": 1.52,
                "CAD": 1.36,
                "CHF": 0.91,
                "CNY": 7.23,
                "INR": 83.30,
                "SGD": 1.35,
                "MYR": 4.74,
                "AED": 3.67
            }
            
            self.exchange_rates = sample_rates
            self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.update_label.config(text=f"Rates updated: {self.last_update}")
            
            # Uncomment this for real API usage:
            # response = requests.get(self.BASE_URL + base_currency)
            # data = response.json()
            # if data['result'] == 'success':
            #     self.exchange_rates = data['conversion_rates']
            #     self.last_update = data['time_last_update_utc']
            #     self.update_label.config(text=f"Rates updated: {self.last_update}")
            # else:
            #     messagebox.showerror("Error", "Failed to fetch exchange rates")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get exchange rates: {str(e)}")
    
    def convert_currency(self):
        """Convert the currency based on user input"""
        try:
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            if from_curr == to_curr:
                messagebox.showwarning("Warning", "Source and target currencies are the same!")
                return
            
            # If we don't have rates for the base currency, fetch them
            if not self.exchange_rates or self.from_currency.get() not in self.exchange_rates:
                self.get_exchange_rates(from_curr)
            
            # Convert from base currency to target currency
            if from_curr == "USD":
                converted_amount = amount * self.exchange_rates[to_curr]
            else:
                # First convert to USD, then to target currency
                amount_in_usd = amount / self.exchange_rates[from_curr]
                converted_amount = amount_in_usd * self.exchange_rates[to_curr]
            
            # Display result
            self.result_label.config(
                text=f"{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}"
            )
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def swap_currencies(self):
        """Swap the 'from' and 'to' currencies"""
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        
        self.from_currency.set(to_curr)
        self.to_currency.set(from_curr)
        
        # Clear result
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
