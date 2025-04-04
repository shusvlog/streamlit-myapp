import pandas as pd
import yfinance as yf

aapl = yf.Ticker("AAPL")

days = 20
hist = aapl.history(period=f'{days}d')
hist.reset_index()
