# DA_Capstonedesign
* * *

## 주제: 섹터 별 국면을 고려한 자산 비중 조정 최적 포트폴리오
### 산업경영공학과 김장언

### 0. Introduction
#### 선정 배경 및 필요성
한국은행이 발표한 금융안정 상황 보고서에 따르면 2020년 3월 이후 약 1년 사이에 가계금융자산 내 금융투자액 중 주식비중은 2016~2019년 평균 9,8%에서 지난해 38.2%로 28.4%p 급증했다. 이처럼 주식투자에 대한 관심이 무차별적으로 커짐에 따라 ‘공포지수’로 일컬어지는 ‘코스피200 변동성지수’(VKOSPI)’는 2021년 1월에 역대 최고치를 기록했다. 이처럼 적절한 논리적 근거 없는 흥분 상태의 투자자들에게 적절한 자산 배분을 통한 리스크 관리는 필수적이다. 하지만 금융권에서는 위험 대비 수익률(Sharp Ratio), 벤츠마크 대비 수익률 등으로 성과를 평가하지만 수많은 개인 투자자들은 맹목적으로 절대 수익률을 성과로 여기며 심리적 영향을 받는다. 따라서 본 과제에서는 국내 섹터 ETF들을 사용하여 포트폴리오 최적화를 진행한다. 그리고 뉴스데이터를 활용한 텍스트마이닝 기법으로 섹터별 일정 기간 등락을 예측한 후 이를 최적화 제약조건에 반영할 것이다. 이를 통해 분산효과를 지닌 포트폴리오에 수익률 및 위험도 측면에서 얼마나 유의적인 영향이 발생하는지 확인할 것이다

#### 주요 내용
먼저 섹터에 관한 뉴스 데이터와 섹터지수의 등락의 연관성을 설명하기 위해 섹터 시장의 가격으로 섹터지수 ETF를 활용한다. 그 후 섹터별 키워드 검색을 통해 뉴스 데이터를 크롤링 한 후 형태소를 분석하여 감성사전에 실릴 후보군을 추출하고 단어들의 빈도수와 긍정 값을 계산한다. 일련의 과정을 거쳐 감성사전을 섹터별로 특화된 감성사전을 구축하고 감성분석하여 최종적으로 익일 섹터지수 변동 항목을 추가하여 기계학습 데이터로 활용한다. 기계학습을 통해 각 섹터의 등락을 예측하고 이를 제약 조건에 반영하여 포트폴리오 최적화한다. 이 때 과거의 경제상황 국면 분석을 통해 섹터 별 등락 별 움직임을 살펴보고 이를 통한 비중 제약 조건의 기준을 정의한다. 그 후 제약 조건이 주어지지 않은 기본적인 최적 포트폴리오 및 KOSPI, SECTOR 지수를 벤치마크로하여 성과 및 위험을 수치적으로 비교함으로써 본 과제의 유의성을 판단한다. 

### 1. Data crawling
#### 1) Sector ETF Price
KODEX 반도체(091160)
자동차(091180)
바이오(244580)
IT(266370)
건설(117700) => 임의로 다섯개 지정



#### 2) Relative News Data
