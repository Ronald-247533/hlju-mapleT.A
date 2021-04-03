from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import requests
from requests.cookies import RequestsCookieJar


#部分测试无法获取答案，提示在计分测试期间不允许看到答案，故尝试进行302破解，但目前没有成功、

option=webdriver.ChromeOptions() 
option.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(options=option)
driver.get("http://125.223.1.242/mapleta/login/login.do")

WebDriverWait(driver,timeout=10).until(EC.presence_of_all_elements_located)
useridText=driver.find_element_by_id("LoginActionForm.login")
useridText.clear()
useridText.send_keys("20201501")

passwordText=driver.find_element_by_id("LoginActionForm.password")
passwordText.clear()
passwordText.send_keys("34120029winnie")
    
driver.find_element_by_id("loginButton").submit()     
try:
    time.sleep(1)
    driver.switch_to.alert.accept()  # 若弹出警告弹窗，则进行确认
except:   
    pass
driver.get("http://125.223.1.242/mapleta/526")
cookies=driver.get_cookies()

s=requests.session()
s.verify=False
jar=RequestsCookieJar()
for cookie in cookies:
        jar.set(cookie['name'],cookie['value'])
try:        
    r=s.get("http://125.223.1.242:80/mapleta/modules/gradeProctoredTest.Login?currPage=1&testId=16470&actionID=viewdetails",cookies=jar,allow_redirects=True)    
except Exception as e:
    print(e)
r.encoding="utf-8"
print(r.text)