import requests
from bs4 import BeautifulSoup

def get_big_mac_price(country):
    url = f'https://www.numbeo.com/food-prices/country_result.jsp?country={country}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'data_wide_table'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 2 and cols[0].text.strip() == 'Big Mac Meal':
            return float(cols[1].text.replace('$', ''))
    return None

# 한국과 미국의 빅맥 가격 가져오기
korea_big_mac_price = get_big_mac_price('South+Korea')
usa_big_mac_price = get_big_mac_price('United+States')

if korea_big_mac_price is not None and usa_big_mac_price is not None:
    print("한국의 빅맥 가격:", korea_big_mac_price, "USD")
    print("미국의 빅맥 가격:", usa_big_mac_price, "USD")
    big_mac_index = (korea_big_mac_price / usa_big_mac_price) * 100
    print("빅맥 지수:", big_mac_index)
else:
    print("데이터를 가져올 수 없습니다.")
