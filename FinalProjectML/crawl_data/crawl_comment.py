from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='./chromedriver.exe')
# Để lấy comment các bài khác thì thay link ở bên dưới
browser.get("https://www.facebook.com/beatvn.network/photos/a.1859759174341435/2670882183229126/?type=3&__xts__%5B0%5D=68.ARD05xWO78HRqM6bz1_-eGH-QQEHNLTfEnCT_8QfEWeB5XEYrCPBKqBx0ASrkzAkGZUypQ1lM68Qp-wbBd3GNfVwEeZjGBKzKbqTn4amtLuRlmPhspWeODh7ARGdEMl3atMeyEyjwjAMifoOiJx9WLqETw9Ww8XwQEfQJEyzk24qeVXSWG1DS8Tqrw7sAuwunervFqr6_evJeBp4QjdBShSyrgiOtxiHSor5R6ktU2vKFP6xg7oqpZYmClE9AdfmN7JULCfviNEk5xch_vxdEJhmzWD0Vl6E8IKd8k0ymfC5uNY6x-k9JdqEcPZUHJjRsqg-T5FLBxy6hzedtdtTbPB66kFd&__tn__=-R")

# Một số bài sẽ yêu cầu đăng nhập fb
'''
# đăng nhập vào fb
txtUser = browser.find_element_by_id('email')
txtUser.send_keys('01664544354')
txtPass = browser.find_element_by_id('pass')
txtPass.send_keys('24101999')
txtPass.send_keys(Keys.ENTER)
sleep(15)
'''

# bấm lúc khác khi hiện bảng đăng nhập 
sleep(5)
luc_khac = browser.find_element_by_xpath('//*[@id="expanding_cta_close_button"]')
luc_khac.click()


sleep(2)
# muốn click được nút thì phải kéo màn hình đến chỗ có nút đó
# kéo màn hình xuống một chút để thấy nút "1K bình luận"
browser.execute_script("window.scrollBy(0,600)")


# bấm vào nút "1K bình luận"
show_cmt_link = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a')
show_cmt_link.click()


# lặp bấm nút "xem thêm bình luận"
# try, except: nếu lệnh trong try bị lỗi thì ctrinh không dừng mà nhảy qua chạy lệnh trong except
while 1:
    sleep(3)
    try:
        more_cmt = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/div/a')        
        
        # kéo màn hình đến vị trí "xem thêm bình luận"
        browser.execute_script("arguments[0].scrollIntoView(true);", more_cmt) 
        
        more_cmt.click()
    except:
        break        


sleep(4)
cmts = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")
#fo = open('test.txt', 'w+')


f = open("A:\\git\\CS114.K21.KHTN\\FinalProjectML\\crawl_data\\text.txt",mode = 'a+',encoding = 'utf-8')


for cmt in cmts:
    # nếu cmt chỉ có hình mà không có text thì sẽ không tìm thấy '_3l3x'
    # và báo lỗi, vì vậy dùng try except để bỏ qua cmt đó
    try:
        content = cmt.find_element_by_class_name('_3l3x')
        t = content.text
        print(t)
        f.write(t)
    except:
        pass

f.close()

print(f"{len(cmts)} comments")
browser.close()
