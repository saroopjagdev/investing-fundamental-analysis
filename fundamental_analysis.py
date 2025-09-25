import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker_symbol = "NVDA"

ticker = yf.Ticker(ticker_symbol)
income_statement = ticker.financials.T
cashflow = ticker.cashflow.T
balance_sheet = ticker.balance_sheet.T




fig, axes = plt.subplots(1,2,figsize=(10, 6))

axes[0].plot(income_statement.index, income_statement['Total Revenue'], marker='o', label='Total Revenue')
axes[0].plot(income_statement.index, income_statement['Net Income'], marker='o', label='Net Income')
axes[0].plot(cashflow.index, cashflow['Free Cash Flow'], marker='o', label='Free Cash Flow')
axes[0].legend()

axes[1].plot(balance_sheet.index, income_statement['Net Income']/balance_sheet['Stockholders Equity'], marker='o', label='ROE')
axes[1].plot(balance_sheet.index, income_statement['Operating Income']/(balance_sheet['Stockholders Equity'] + balance_sheet['Total Debt'] - balance_sheet['Cash Cash Equivalents And Short Term Investments']), marker='o', label='ROIC')
axes[1].legend()
plt.show()