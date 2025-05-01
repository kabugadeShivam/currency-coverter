# currency-coverter
Currency converter - Collage Python project SE
Currency Converter Application
Currency Converter Screenshot
  
A simple desktop application built with Python and Tkinter for converting between different currencies using real-time exchange rates.

Features
Convert between multiple currencies (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR, SGD, MYR, AED)

Swap currencies with a single click

Clean and intuitive user interface

Displays the last update time for exchange rates
![Screenshot_2025-04-21_210934 1](https://github.com/user-attachments/assets/e24b947d-8179-4db8-afa4-dcd0ba6e59ee)

Requirements
Python 3.x

Tkinter (usually comes with Python)

requests library (pip install requests)

Installation
Clone this repository:

bash
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter
Install the required dependencies:

bash
pip install requests
Run the application:

bash
python currency_converter.py
Configuration
To use real-time exchange rates (instead of the hardcoded sample rates):

Get a free API key from exchangerate-api.com

Replace YOUR_API_KEY in the code with your actual API key

Uncomment the API-related code sections in the get_exchange_rates method

Usage
Enter the amount you want to convert

Select the source currency (the currency you're converting from)

Select the target currency (the currency you're converting to)

Click "Convert" to see the result



Use "Swap Currencies" to quickly switch between source and target currencies

Notes
The application currently uses hardcoded exchange rates by default

For real-time rates, you need to sign up for an API key and uncomment the relevant code

Exchange rates may not be 100% accurate without using the live API

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.
