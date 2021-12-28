from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

def get_stock_data(ticker) :
    url = f'https://finance.yahoo.com/quote/{ticker}'
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html5lib")
    shortName = soup.find('h1', {'class' : 'D(ib) Fz(18px)'}).text
    bracket = shortName.find('(')
    shortName = shortName[: bracket]
    percent = soup.find('fin-streamer', {'class' : 'Mstart(4px) D(ib) Fz(24px)'}).text
    
    if percent[0] == '+':
        percent = float(percent[1:])
    else:
        percent = float(percent)
    
    price = soup.find('fin-streamer', {'class' : 'C($primaryColor) Fz(24px) Fw(b)'}).text
    currentPrice = soup.find('fin-streamer', {'class' : 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    return {
        "symbol": ticker,
        "shortName": shortName,
        "currentPrice": currentPrice,
        "percent": percent
        }
# WINDOW_SIZE = "1920,1080"

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
# driver.get('https://finance.yahoo.com/quote/FB')

# driver.get_screenshot_as_file("capture.png")
# content = driver.find_elements_by_class_name("Fw(b) Fz(36px) Mb(-4px) D(ib)")
# print(content)
# driver.close()
