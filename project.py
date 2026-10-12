import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tcs_project.csv")
#print(df.columns)

df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
df = df.sort_values("date")

# Question No1. Daily return
df["Daily_Return"] = df["close"].pct_change()*100

# Question no.2 Moving Average
df["MA20"] = df["close"].rolling(20).mean().fillna(0)
df["MA50"] = df["close"].rolling(50).mean().fillna(0)
# question no.3 Max and min price
max_price = df["high"].max()
min_price = df["low"].min()
highest_close = df["close"].max()
lowest_close = df["close"].min()
latest_close = df["close"].iloc[-1]
avg_return = df["Daily_Return"].mean()
ma20 = df["MA20"].iloc[-1]
ma50 = df["MA50"].iloc[-1]

#Question no.4 Trend Analysis
df["Trend"] = df.apply(lambda row: "UPWARD" if row["MA20"] > row["MA50"] else "DOWNWARD",axis=1)

plt.show()
df.to_csv("tcs_share_analysis.csv", index=False)
