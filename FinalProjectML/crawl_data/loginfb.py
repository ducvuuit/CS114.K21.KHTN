from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint
# 1. khai báo biến browser
browser = webdriver.Chrome(executable_path='./chromedriver.exe')

# 2. mở thử fb
browser.get('https://www.facebook.com/beatvn.network/photos/a.1859759174341435/2670882183229126/?type=3&theater')
# 2a. điền thông tin tài khoản
txtUser = browser.find_element_by_id('email')
txtUser.send_keys('01664544354')
txtPass = browser.find_element_by_id('pass')
txtPass.send_keys('24101999')
txtPass.send_keys(Keys.ENTER)
sleep(20)


# 3. đóng trình duyệt (nếu k sẽ tốn bộ nhớ)
browser.close()