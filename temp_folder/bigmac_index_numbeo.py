import pandas as pd

# Numbeo에서 제공하는 빅맥 가격 데이터셋을 사용하여 한국과 미국의 빅맥 가격 비교
url = "https://www.numbeo.com/food-prices/country_result.jsp?country=United+States"
df_usa = pd.read_html(url)[2]  # 데이터프레임으로 변환

url = "https://www.numbeo.com/food-prices/country_result.jsp?country=South+Korea"
df_korea = pd.read_html(url)[2]  # 데이터프레임으로 변환

print(df_korea)


# 미국과 한국의 빅맥 가격 비교
# usa_big_mac_price = df_usa.loc[df_usa['Item'] == 'Big Mac Meal']['Average']
# korea_big_mac_price = df_korea.loc[df_korea['Item'] == 'Big Mac Meal']['Average']

# print("미국의 빅맥 가격:", usa_big_mac_price.values[0], "USD")
# print("한국의 빅맥 가격:", korea_big_mac_price.values[0], "USD")

# # 빅맥 지수 계산
# big_mac_index = (korea_big_mac_price / usa_big_mac_price) * 100
# print("빅맥 지수:", big_mac_index.values[0])
