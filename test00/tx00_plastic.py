# import requests
# import json

# def get_trash_bag_stores(city_name, district_name):
#     # 1. 공공데이터포털에서 발급받은 본인의 인코딩 인증키를 입력
#     service_key = "여기에_발급받은_인증키를_넣으세요"

#     # 2. 요청주소 (전국 종량제 봉투 판매소 표준 데이터 API 주소 예시)
    
#     # 3. 요청 파라미터 설정
#     params = {
#         'serviceKey': service_key,
#         'pageNo': '1',
#         'numOfRows': '100',   # 한 번에 가져올 데이터 수
#         'type': 'json',       # 결과 형식 (json이 파이썬에서 다루기 쉬움)
#         'q': f"{city_name} {district_name}" # 검색어 (예: 서울특별시 강남구)
#     }

#     try:
#         # 4. API호출
#         response = response.get(url, params=params)

#         # 5. 응답 상태 확인 (200은 성공)
#         if response.status_code == 200:
#             data = response.json()

#             # 실제 데이터가 담긴 리스트 추출 (API 명세서에 따라 구조가 다를 수 있음)
#             items = data.get('response', {}).get('body', {}).get('items', [])
            
#             if not items:
#                 print(f"{district_name} 지역에 대한 데이터가 없습니다.")
#                 return

#             print(f"--- {district_name} 종량제 봉투 판매소 목록 ---")
#             for item in items:
#                 name = item.get('msstoreNm')     # 판매소 명칭
#                 address = item.get('rdmadr')     # 도로명 주소
#                 tel = item.get('phoneNumber')    # 전화번호
                
#                 print(f"점포명: {name} | 주소: {address} | 연락처: {tel}")
                
#         else:
#             print(f"Error 발생: {response.status_code}")

#     except Exception as e:
#         print(f"연결 오류: {e}")

# # 실행 예시 (본인의 지역으로 바꿔보세요)
# get_trash_bag_stores("서울특별시", "강남구")