import requests
import matplotlib.pyplot as plt
from datetime import datetime

# API 키 설정
api_key = 'YOUR_API_KEY'

# 요청할 통화 설정
base_currency = 'KRW'  # 한국 원을 기준으로 설정
currencies = ['USD', 'EUR', 'JPY', 'GBP', 'CNY']  # 비교할 다른 통화들을 추가하세요
# currencies = ['TRY', 'RUB', 'DKK', 'NOK', 'EZP']  # 비교할 다른 통화들을 추가하세요

# 서브플롯 생성
fig, axes = plt.subplots(nrows=len(currencies), ncols=1, figsize=(12, 8), sharex=True)

# 각 통화에 대한 환율 데이터 가져오고 그래프 표시
for currency, ax in zip(currencies, axes):
    url = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={currency}&to_symbol={base_currency}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    dates = []
    prices = []

    for date, info in data['Time Series FX (Daily)'].items():
        dates.append(datetime.strptime(date, '%Y-%m-%d'))
        prices.append(float(info['4. close']))

    ax.plot(dates, prices, label=f'{base_currency}/{currency}')
    ax.set_title(f'Exchange Rate ({base_currency}/{currency}) Over Time')
    ax.grid(True)

plt.xlabel('Date')
plt.ylabel('Price')
plt.tight_layout()
plt.show()
