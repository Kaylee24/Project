## (☞ﾟヮﾟ)☞ 개요
- 프로젝트 기간 : 2024.05.16(목) ~ 2023.05.23(목)
- 주제 : 환율 및 물가 지표를 알기 쉽게 제공하는 여행 정보 사이트
- 서비스명 : Easy Travel

## 😄 팀원 소개
- 박재현 (팀장)
   - Models.py, Serializers.py, Views.py
   - Comparison Page, Detail Page(comment) 구현
   - 로그인 관련 로직 구현
   - dummy data
   - CSS

- 김송희
   - countries.json
   - 여행지 추천 알고리즘 구현
   - Main Page, Recommendation Modal, Detail Graph Modal 구현
   - Profile Page(visited, interested), Login/SignUp Modal 구현
   - Detail Page 로딩 지연 문제 해결
   - CSS

## 🌎 서비스 소개

##### 우리는 엔화가 떨어졌다며, 이번 해외여행은 일본으로 가자고 계획합니다.

&nbsp;&nbsp; 더 이상 해외여행은 일생에 몇번 없는 특별한 순간이 아닙니다. 해외여행을 떠나면서도 이번이 마지막이라는 생각을 하지 않고, 다음에는 어디를 갈지 생각합니다.  
&nbsp;&nbsp; 이러한 시대에 이제는 환율과 해당 국가의 물가 또한 해외여행지를 결정할 때 중요한 요소가 되었습니다.  
&nbsp;&nbsp; 해외여행을 가기 전 환율과 물가를 검색해보신 적 있으신가요? 여행지가 결정되어 해당 국가의 환율과 물가만 검색한다면 간단하지만, 여행지를 결정하기 전에 다양한 국가의 환율과 물가 정보를 알아보기란 여간 번거로운 일이 아닙니다.  
&nbsp;&nbsp; 따라서 저희는 알기 쉽게 국가별 환율과 물가를 보여주고, 해외여행 계획을 더욱 손쉽게 만들어주는 서비스를 기획하였습니다.



## ❄ 서비스 화면
#### Main Page
![alt text](<Main Page.png>)

#### Comparison Page
![alt text](<Comparison Page.png>)

#### Profile Page
![alt text](<Profile Page.png>)

#### Detail Page
![alt text](<Detail Page.png>)

## ⛓ 주요 기능
- 메인 페이지 | 예산을 기반으로 한 여행지 추천, 여행지 검색 및 해당 국가 상세 페이지로 이동 기능
- 비교 페이지 | 서비스 중인 국가들의 환율, 환율 그래프, 물가 지표 제공
- 상세 페이지 | 각국 정보 및, 이용자들이 정보를 공유 할 수 있는 게시글 시스템
- 프로필 페이지 | 이용자 기본 정보, 방문 국가, 관심 국가, 작성한 게시글 등의 정보 조회 기능



## 📃 ERD



## ⚙ 여행지 추천 알고리즘
1. 이용자에게 '관심 국가', '여행 예산(숙박비, 항공비 제외)', '여행 기간'을 입력 받습니다.
   - 이용자가 form을 통해 정보를 입력하면, 이는 axios를 통해 Django 서버로 전송됩니다.
2. 이용자가 입력한 관심 국가와 동일한 지역으로 분류된 국가들에 대해 예산을 기반으로 추천 여부를 판단합니다.
   - 해당 국가의 'Area' 정보를 확인하여, 동일한 'Area' 정보를 가진 국가들을 탐색합니다.
3. 해당 국가의 물가 지표를 활용하여, 이용자가 입력한 하루 당 예산(예산/기간)을 바탕으로 여행지 추천 결과를 '비추천', '배낭 여행', '중급 여행', '럭셔리 여행' 4가지로 분류하여 제공합니다.



## 🛠 작업

### 5월 16일 (목)
- 주제 선정
- ERD 작성
- model 작성
- Main Page 기본 틀 구현

### 5월 17일 (금)
- model을 기반으로 serializer 작성
- 기본 data 제작
- Main Page 수정

### 5월 18일 (토)
- model의 image -> image1, 2, 3으로 변경
- 데이터 django -> vue3로 전송
- Detail Page 제작
- 추천 알고리즘 작성

### 5월 19일 (일)
- Profile Page 생성
- Detail Page 제작

### 5월 20일 (월)
- Navbar, LoginModal, SignUpModal, Comparison Page 기본 틀 구현
- Django의 Media file에 이미지 데이터 삽입
- SignUp 로직 구현

### 5월 21일 (화)
- (Gallery)에러 수정
- Login 로직 구현
- Comparison Page의 Card 컴포넌트 제작
- 각종 css작업 시작
- DetailComment (댓글) 구현

### 5월 22일 (수)
- 댓글의 새로고침을 해야 반영되던 버그 수정
- 댓글의 username 나오게 수정
- Profile Modal 구조 수정
- MainView 개선
- RecommendationModal(추천 알고리즘 사용 모달) 제작

### 5월 23일 (목)
- 댓글 삭제 구현
- Navbar의 Direct 메뉴 추가 (Detail Page로 가는 전체 나라 보드)
- 추가 css 작업
- dumpdata 제작
