import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker_symbol = "NESN.SW"

ticker = yf.Ticker(ticker_symbol)
income_statement = ticker.financials.T
cashflow = ticker.cashflow.T



print("----- Annual Income Statement -----")
print(income_statement)

fig, ax = plt.subplots(figsize=(10, 6))

ax[0].plot(income_statement.index, income_statement['Total Revenue'], marker='o', label='Total Revenue')
ax[0].plot(income_statement.index, income_statement['Net Income'], marker='o', label='Net Income')
ax[0].plot(cashflow.index, cashflow['Free Cash Flow'], marker='o', label='Free Cash Flow')
ax[0].legend()


plt.show()