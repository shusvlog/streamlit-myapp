import pandas as pd
import yfinance as yf

aapl = yf.Ticker("AAPL")

days = 20
hist = aapl.history(period=f'{days}d')
hist.reset_index()

hist_msft = yf.Ticker("MSFT").history(period=f'{days}d')
hist_msft.head()

pd.concat([hist, hist_msft], axis=1).head()

hist.index = hist.index.strftime('%d %B %Y')
hist = hist[['Close']]
hist.columns = ['apple']
hist.head(3)

hist = hist.T
hist

hist.index.name = 'Name'
hist
