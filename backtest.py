import pyupbit
import numpy as np

#시초가, 고가, 저가, 종가, 거래량
df = pyupbit.get_ohlcv("KRW-BTC") 
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0005
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

#누적 수익률(누적곱)
df['hpr'] = df['ror'].cumprod()
#Draw Down
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#최대 Draw Down(MDD)
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")