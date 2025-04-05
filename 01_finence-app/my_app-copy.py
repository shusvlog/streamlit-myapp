import pandas as pd
import yfinance as yf
import altair as alt

def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = '企業名'
        df = pd.concat([df, hist])
    return df

days = 20
tickers = {
    'apple': 'AAPL',
    'meta': 'META',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'amazon': 'AMZN'
}

df = get_data(days, tickers)
df

companies = ['apple', 'meta']
data = df.loc[companies]
data.sort_index()

data = data.T.reset_index()
data = pd.melt(data, id_vars=['Date']).rename(
    columns = {'value': '株価(USD$)'}
)
data
