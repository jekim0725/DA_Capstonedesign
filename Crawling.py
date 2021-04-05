import selenium
from selenium import webdriver
import pandas as pd

codes = ['091160', '091180' ,'244580','266370','117700'] 
def get_Data(code):
    url = 'https://finance.naver.com/item/sise_day.nhn?code={}&page=1'.format(code)
    driver = webdriver.Chrome(executable_path='C:/Users/eonjk/chromedriver_win32/chromedriver')
    driver.get(url)
    driver.implicitly_wait(2)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    pgrr = soup.find('td', class_='pgRR')
    last_page = str(pgrr.a['href']).split('=')[-1]

    data = pd.DataFrame()
    
    for page in range(1, int(last_page) + 1):
        sise_url = 'https://finance.naver.com/item/sise_day.nhn?code={}'.format(code)
        url = '{}&page={}'.format(sise_url, page)
        driver.get(url)
        driver.implicitly_wait(2)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        a = soup.find('table', class_='type2')
        table = str(a)
        table_df_list = pd.read_html(table)
        table_df = table_df_list[0]
        table_df.dropna(inplace=True)

        data = data.append(table_df)
        name = str(code) + '1.csv'
        data.to_csv(name, mode='w', encoding='euc-kr')
    
    return data
