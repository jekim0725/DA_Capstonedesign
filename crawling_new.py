from selenium import webdriver
import time
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

before = 'https://news.joins.com/Search/TotalNews?page='
after = '&Keyword=%EA%B1%B4%EC%84%A4&PeriodType=DirectInput&StartSearchDate=04%2F01%2F2020%2000%3A00%3A00&EndSearchDate=04%2F01%2F2021%2000%3A00%3A00&SortType=New&SourceGroupType=Joongang%7CJtbc&ServiceCode=11&SearchCategoryType=TotalNews'  

start = time.time() 

chromedriver = "C:/Users/eonjk/chromedriver.exe" #경로 설정chromedriver_win32/chromedriver.exe"
options = webdriver.ChromeOptions() #옵션주기
options.add_argument('disable-gpu') #GPU ㄴㄴ

driver = webdriver.Chrome(chromedriver, options=options)

links = []
pageNum = 1
total = pd.DataFrame() #확인할 때마다 초기화해야하니까

while(True):
#for i in range(1, pageNum+1): #1페이지부터 입력한 페이지까지
    #url = before + str(pageNum) + after
    #url = url_format.format(str(pageNum))
    driver.get(before + str(pageNum) + after) # pageNum 접속

    time.sleep(0.1) # url 이동 대기 시간 0.1초로 설정
    
    # 뉴스 기사 객체 class name으로 가져오기
    news = driver.find_elements_by_class_name('headline.mg') 
    
    if(len(news) == 0): # 뉴스 기사가 하나도 없는 경우 멈춘다
        break
        
    #뉴스 기사가 하나라도 있으면
    for elem in news:
        link = elem.find_element_by_tag_name('a').get_attribute('href')
        links.append(link)
    print(pageNum) # 확인차 출력
    
    #if pageNum == 10:
    #    print(links)
    #    break
    
    pageNum += 1 
    
for link in links: #각 링크마다 
    try:
        r = requests.get(link)
        sp = BeautifulSoup(r.text, "html.parser", from_encoding='euc-kr') #, from_encoding ='utf-8')
        article = sp.select('div#article_body')
        article = article[0].get_text().strip().replace('\xa0', '').replace('       ', ' ')#.strip()
        article = [article]
        #articles.append(article) #글

        title = sp.select('h1#article_title')[0].text  #ext.strip('title">')
        title = [title]
        #titles.append(title)

        datetime = sp.select('div.byline')[0].text.split('입력 ')
        datetime = datetime[1].split(' ')[0]
        #dates.append(datetime)
        datetime = [datetime]
        
        sample = [datetime, title, article]
        sample = pd.DataFrame(sample).T
        total = pd.concat([total, sample])
        print(link)
    except:
        sample = [np.nan, np.nan, np.nan]
        sample =  pd.Series(sample)
        total = pd.concat([total, sample], axis=1)
        print(" 오류..")

total.rename(columns = {0: 'Date', 1: 'Title', 2 : 'Content'}, inplace=True)  
total.to_excel('건설20200401_20200401.xlsx')        
print("걸린 시간(초): ", time.time()-start)

etf = pd.read_csv('117700.csv', encoding='cp949')

etf.drop(etf.columns[[0]], axis =1, inplace=True)
etf.set_index('날짜', inplace=True)
updown = []

for i in range(1,len(etf)): 
    if (etf['종가'].iloc[i-1] > etf['종가'].iloc[i]):
        updown.append(1)
    else:
        updown.append(0)
        
updown.append(np.nan)
etf['등락'] = updown

etf.to_csv('117700.csv', encoding='cp949')




###########################################################################################
#자동차
before2 = 'https://news.joins.com/Search/totalnews?page='
after2 = '&Keyword=%EC%9E%90%EB%8F%99%EC%B0%A8&PeriodType=DirectInput&StartSearchDate=04%2F01%2F2020%2000%3A00%3A00&EndSearchDate=04%2F01%2F2021%2000%3A00%3A00&SortType=New&SourceGroupType=Joongang%7CJtbc&SearchCategoryType=TotalNews'  

start = time.time() 

chromedriver = "C:/Users/eonjk/chromedriver.exe" #경로 설정chromedriver_win32/chromedriver.exe"
options = webdriver.ChromeOptions() #옵션주기
options.add_argument('disable-gpu') #GPU ㄴㄴ

driver = webdriver.Chrome(chromedriver, options=options)

links = []
pageNum = 1
total = pd.DataFrame() #확인할 때마다 초기화해야하니까

while(True):
#for i in range(1, pageNum+1): #1페이지부터 입력한 페이지까지
    #url = before + str(pageNum) + after
    #url = url_format.format(str(pageNum))
    driver.get(before2 + str(pageNum) + after2) # pageNum 접속

    time.sleep(0.1) # url 이동 대기 시간 0.1초로 설정
    
    # 뉴스 기사 객체 class name으로 가져오기
    news = driver.find_elements_by_class_name('headline.mg') 
    
    if(len(news) == 0): # 뉴스 기사가 하나도 없는 경우 멈춘다
        break
        
    #뉴스 기사가 하나라도 있으면
    for elem in news:
        link = elem.find_element_by_tag_name('a').get_attribute('href')
        links.append(link)
    print(pageNum) # 확인차 출력
    
    #if pageNum == 10:
    #    print(links)
    #    break
    
    pageNum += 1 
    
for link in links: #각 링크마다 
    try:
        r = requests.get(link)
        sp = BeautifulSoup(r.text, "html.parser", from_encoding='euc-kr') #, from_encoding ='utf-8')
        article = sp.select('div#article_body')
        article = article[0].get_text().strip().replace('\xa0', '').replace('       ', ' ')#.strip()
        article = [article]
        #articles.append(article) #글

        title = sp.select('h1#article_title')[0].text  #ext.strip('title">')
        title = [title]
        #titles.append(title)

        datetime = sp.select('div.byline')[0].text.split('입력 ')
        datetime = datetime[1].split(' ')[0]
        #dates.append(datetime)
        datetime = [datetime]
        
        sample = [datetime, title, article]
        sample = pd.DataFrame(sample).T
        total = pd.concat([total, sample])
        print(link)
    except:
        sample = [np.nan, np.nan, np.nan]
        sample =  pd.Series(sample)
        total = pd.concat([total, sample], axis=1)
        print(" 오류..")

total.rename(columns = {0: 'Date', 1: 'Title', 2 : 'Content'}, inplace=True)  
total.to_excel('자동차20200401_20200401.xlsx')        
print("걸린 시간(초): ", time.time()-start)

etf = pd.read_csv('091180.csv', encoding='cp949')

etf.drop(etf.columns[[0]], axis =1, inplace=True)
etf.set_index('날짜', inplace=True)
updown = []

for i in range(1,len(etf)): 
    if (etf['종가'].iloc[i-1] > etf['종가'].iloc[i]):
        updown.append(1)
    else:
        updown.append(0)

updown.append(np.nan)        
etf['등락'] = updown

etf.to_csv('091180.csv', encoding='cp949')

###########################################################################################
#반도체
before3 = 'https://news.joins.com/Search/totalnews?page='
after3 = '&Keyword=%EB%B0%98%EB%8F%84%EC%B2%B4&PeriodType=DirectInput&StartSearchDate=04%2F01%2F2020%2000%3A00%3A00&EndSearchDate=04%2F01%2F2021%2000%3A00%3A00&SortType=New&SourceGroupType=Joongang%7CJtbc&SearchCategoryType=TotalNews' 

start = time.time() 

chromedriver = "C:/Users/eonjk/chromedriver.exe" #경로 설정chromedriver_win32/chromedriver.exe"
options = webdriver.ChromeOptions() #옵션주기
options.add_argument('disable-gpu') #GPU ㄴㄴ

driver = webdriver.Chrome(chromedriver, options=options)

links = []
pageNum = 1
total = pd.DataFrame() #확인할 때마다 초기화해야하니까

while(True):
#for i in range(1, pageNum+1): #1페이지부터 입력한 페이지까지
    #url = before + str(pageNum) + after
    #url = url_format.format(str(pageNum))
    driver.get(before3 + str(pageNum) + after3) # pageNum 접속

    time.sleep(0.1) # url 이동 대기 시간 0.1초로 설정
    
    # 뉴스 기사 객체 class name으로 가져오기
    news = driver.find_elements_by_class_name('headline.mg') 
    
    if(len(news) == 0): # 뉴스 기사가 하나도 없는 경우 멈춘다
        break
        
    #뉴스 기사가 하나라도 있으면
    for elem in news:
        link = elem.find_element_by_tag_name('a').get_attribute('href')
        links.append(link)
    print(pageNum) # 확인차 출력
    
    #if pageNum == 10:
    #    print(links)
    #    break
    
    pageNum += 1 
    
for link in links: #각 링크마다 
    try:
        r = requests.get(link)
        sp = BeautifulSoup(r.text, "html.parser", from_encoding='euc-kr') #, from_encoding ='utf-8')
        article = sp.select('div#article_body')
        article = article[0].get_text().strip().replace('\xa0', '').replace('       ', ' ')#.strip()
        article = [article]
        #articles.append(article) #글

        title = sp.select('h1#article_title')[0].text  #ext.strip('title">')
        title = [title]
        #titles.append(title)

        datetime = sp.select('div.byline')[0].text.split('입력 ')
        datetime = datetime[1].split(' ')[0]
        #dates.append(datetime)
        datetime = [datetime]
        
        sample = [datetime, title, article]
        sample = pd.DataFrame(sample).T
        total = pd.concat([total, sample])
        print(link)
    except:
        sample = [np.nan, np.nan, np.nan]
        sample =  pd.Series(sample)
        total = pd.concat([total, sample], axis=1)
        print(" 오류..")

total.rename(columns = {0: 'Date', 1: 'Title', 2 : 'Content'}, inplace=True)  
total.to_excel('반도체20200401_20200401.xlsx')   
print("걸린 시간(초): ", time.time()-start) 

etf = pd.read_csv('091160.csv', encoding='cp949')

etf.drop(etf.columns[[0]], axis =1, inplace=True)
etf.set_index('날짜', inplace=True)
updown = []

for i in range(1,len(etf)): 
    if (etf['종가'].iloc[i-1] > etf['종가'].iloc[i]):
        updown.append(1)
    else:
        updown.append(0)

updown.append(np.nan)        
etf['등락'] = updown

etf.to_csv('091160.csv', encoding='cp949')

###########################################################################################
#바이오

before4 = ' https://news.joins.com/Search/TotalNews?page='
after4 = '&Keyword=%EB%B0%94%EC%9D%B4%EC%98%A4&PeriodType=DirectInput&StartSearchDate=04%2F01%2F2020%2000%3A00%3A00&EndSearchDate=04%2F01%2F2021%2000%3A00%3A00&SortType=New&SourceGroupType=Joongang%7CJtbc&ServiceCode=11&SearchCategoryType=TotalNews'  

start = time.time() 

chromedriver = "C:/Users/eonjk/chromedriver.exe" #경로 설정chromedriver_win32/chromedriver.exe"
options = webdriver.ChromeOptions() #옵션주기
options.add_argument('disable-gpu') #GPU ㄴㄴ

driver = webdriver.Chrome(chromedriver, options=options)

links = []
pageNum = 1
total = pd.DataFrame() #확인할 때마다 초기화해야하니까

while(True):
#for i in range(1, pageNum+1): #1페이지부터 입력한 페이지까지
    #url = before + str(pageNum) + after
    #url = url_format.format(str(pageNum))
    driver.get(before4 + str(pageNum) + after4) # pageNum 접속

    time.sleep(0.1) # url 이동 대기 시간 0.1초로 설정
    
    # 뉴스 기사 객체 class name으로 가져오기
    news = driver.find_elements_by_class_name('headline.mg') 
    
    if(len(news) == 0): # 뉴스 기사가 하나도 없는 경우 멈춘다
        break
        
    #뉴스 기사가 하나라도 있으면
    for elem in news:
        link = elem.find_element_by_tag_name('a').get_attribute('href')
        links.append(link)
    print(pageNum) # 확인차 출력
    
    #if pageNum == 10:
    #    print(links)
    #    break
    
    pageNum += 1 
    
for link in links: #각 링크마다 
    try:
        r = requests.get(link)
        sp = BeautifulSoup(r.text, "html.parser", from_encoding='euc-kr') #, from_encoding ='utf-8')
        article = sp.select('div#article_body')
        article = article[0].get_text().strip().replace('\xa0', '').replace('       ', ' ')#.strip()
        article = [article]
        #articles.append(article) #글

        title = sp.select('h1#article_title')[0].text  #ext.strip('title">')
        title = [title]
        #titles.append(title)

        datetime = sp.select('div.byline')[0].text.split('입력 ')
        datetime = datetime[1].split(' ')[0]
        #dates.append(datetime)
        datetime = [datetime]
        
        sample = [datetime, title, article]
        sample = pd.DataFrame(sample).T
        total = pd.concat([total, sample])
        print(link)
    except:
        sample = [np.nan, np.nan, np.nan]
        sample =  pd.Series(sample)
        total = pd.concat([total, sample], axis=1)
        print(" 오류..")

total.rename(columns = {0: 'Date', 1: 'Title', 2 : 'Content'}, inplace=True)  
total.to_excel('바이오20200401_20200401.xlsx')   
print("걸린 시간(초): ", time.time()-start)

etf = pd.read_csv('244580.csv', encoding='cp949')

etf.drop(etf.columns[[0]], axis =1, inplace=True)
etf.set_index('날짜', inplace=True)
updown = []

for i in range(1,len(etf)): 
    if (etf['종가'].iloc[i-1] > etf['종가'].iloc[i]):
        updown.append(1)
    else:
        updown.append(0)

updown.append(np.nan)        
etf['등락'] = updown

etf.to_csv('244580.csv', encoding='cp949')

###########################################################################################
#IT
before5 = 'https://news.joins.com/Search/TotalNews?page='
after5 = '&Keyword=IT&PeriodType=DirectInput&StartSearchDate=04%2F01%2F2020%2000%3A00%3A00&EndSearchDate=04%2F01%2F2021%2000%3A00%3A00&SortType=New&SourceGroupType=Joongang%7CJtbc&ServiceCode=11&SearchCategoryType=TotalNews' 

start = time.time() 

chromedriver = "C:/Users/eonjk/chromedriver.exe" #경로 설정chromedriver_win32/chromedriver.exe"
options = webdriver.ChromeOptions() #옵션주기
options.add_argument('disable-gpu') #GPU ㄴㄴ

driver = webdriver.Chrome(chromedriver, options=options)

links = []
pageNum = 1
total = pd.DataFrame() #확인할 때마다 초기화해야하니까

while(True):
#for i in range(1, pageNum+1): #1페이지부터 입력한 페이지까지
    #url = before + str(pageNum) + after
    #url = url_format.format(str(pageNum))
    driver.get(before5 + str(pageNum) + after5) # pageNum 접속

    time.sleep(0.1) # url 이동 대기 시간 0.1초로 설정
    
    # 뉴스 기사 객체 class name으로 가져오기
    news = driver.find_elements_by_class_name('headline.mg') 
    
    if(len(news) == 0): # 뉴스 기사가 하나도 없는 경우 멈춘다
        break
        
    #뉴스 기사가 하나라도 있으면
    for elem in news:
        link = elem.find_element_by_tag_name('a').get_attribute('href')
        links.append(link)
    print(pageNum) # 확인차 출력
    
    #if pageNum == 10:
    #    print(links)
    #    break
    
    pageNum += 1 
    
for link in links: #각 링크마다 
    try:
        r = requests.get(link)
        sp = BeautifulSoup(r.text, "html.parser", from_encoding='euc-kr') #, from_encoding ='utf-8')
        article = sp.select('div#article_body')
        article = article[0].get_text().strip().replace('\xa0', '').replace('       ', ' ')#.strip()
        article = [article]
        #articles.append(article) #글

        title = sp.select('h1#article_title')[0].text  #ext.strip('title">')
        title = [title]
        #titles.append(title)

        datetime = sp.select('div.byline')[0].text.split('입력 ')
        datetime = datetime[1].split(' ')[0]
        #dates.append(datetime)
        datetime = [datetime]
        
        sample = [datetime, title, article]
        sample = pd.DataFrame(sample).T
        total = pd.concat([total, sample])
        print(link)
    except:
        sample = [np.nan, np.nan, np.nan]
        sample =  pd.Series(sample)
        total = pd.concat([total, sample], axis=1)
        print(" 오류..")

total.rename(columns = {0: 'Date', 1: 'Title', 2 : 'Content'}, inplace=True)  
total.to_excel('IT20200401_20200401.xlsx')   
print("걸린 시간(초): ", time.time()-start)

etf = pd.read_csv('244580.csv', encoding='cp949')

etf.drop(etf.columns[[0]], axis =1, inplace=True)
etf.set_index('날짜', inplace=True)
updown = []

for i in range(1,len(etf)): 
    if (etf['종가'].iloc[i-1] > etf['종가'].iloc[i]):
        updown.append(1)
    else:
        updown.append(0)

updown.append(np.nan)        
etf['등락'] = updown

etf.to_csv('244580.csv', encoding='cp949')