# 판다스 라이브러리 로드
import pandas as pd

# CSV 읽기
df = pd.read_csv('./day04/도서정보.csv', encoding='utf-8')

print(df)