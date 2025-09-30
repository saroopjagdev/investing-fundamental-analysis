import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker_symbol = "GOOGL"

ticker = yf.Ticker(ticker_symbol)
income_statement = ticker.financials.T
cashflow = ticker.cashflow.T
balance_sheet = ticker.balance_sheet.T

fig, axes = plt.subplots(2,2,figsize=(14, 10))

axes[0,0].plot(income_statement.index, income_statement['Total Revenue'], marker='o', label='Total Revenue')
axes[0,0].plot(income_statement.index, income_statement['Net Income'], marker='o', label='Net Income')
axes[0,0].plot(cashflow.index, cashflow['Free Cash Flow'], marker='o', label='Free Cash Flow')
axes[0,0].legend()

axes[0,1].plot(balance_sheet.index, income_statement['Net Income']/balance_sheet['Stockholders Equity'], marker='o', label='ROE')
axes[0,1].plot(balance_sheet.index, income_statement['Operating Income']/(balance_sheet['Stockholders Equity'] + balance_sheet['Total Debt'] - balance_sheet['Cash Cash Equivalents And Short Term Investments']), marker='o', label='ROIC')
axes[0,1].legend()

axes[1,0].plot(balance_sheet.index, balance_sheet['Total Debt'], marker='o', label='Debt')
axes[1,0].plot(balance_sheet.index, balance_sheet['Stockholders Equity'], marker='o', label='Equity')
axes[1,0].legend()
axes[1,0].set_title("Debt vs Equity")

axes[1,1].plot(balance_sheet.index, balance_sheet['Retained Earnings'], marker='o', label='Retained Earnings')
axes[1,1].legend()
axes[1,1].set_title("Retained Earnings Trend")

plt.tight_layout()
plt.show()
