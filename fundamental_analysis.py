import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ticker_symbol = "PLTR"

ticker = yf.Ticker(ticker_symbol)
income_statement = ticker.financials.T
cashflow = ticker.cashflow.T
print(cashflow.T.index)

cashflow["FCF_calc"] = cashflow["Operating Cash Flow"] + cashflow["Capital Expenditure"]
print(cashflow[["Free Cash Flow", "FCF_calc"]])


print("----- Annual Income Statement -----")
#print(income_statement)


plt.plot(income_statement.index, income_statement['Total Revenue'], marker='o', label='Total Revenue')
plt.plot(income_statement.index, income_statement['Net Income'], marker='o', label='Net Income')

#plt.show()