from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. khai báo browser
broswer = webdriver.Chrome(executable_path='chromedriver.exe')

# 2. mở URL của post, thay đổi link này để lấy các bình luận từ post khác, chú ý thay đổi vòng lặp xem thêm bình luận
broswer.get("https://www.facebook.com/groups/ghiendalat/permalink/1434613063414279/?__tn__=-R")

# 2a. đăng nhập vào fb
'''
txtUser = broswer.find_element_by_id('email')
txtUser.send_keys('01664544354')
txtPass = broswer.find_element_by_id('pass')
txtPass.send_keys('24101999')
txtPass.send_keys(Keys.ENTER)
sleep(15)'''
# 3. Lấy link hiện comment
showcomment_link = broswer.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
showcomment_link.click()
sleep(5)

# 4. Lấy comment
showmore_link = broswer.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[3]/div[1]/div/a")
showmore_link.click()
sleep(5)

showmore_link.click()
sleep(5)
# 5. ghi các comment vào file
comment_list = broswer.find_elements_by_xpath("//div[@aria-label='Bình luận']")
sleep(10)
print(comment_list)
'''
for comment in comment_list:
    content = comment.find_element_by_class_name('_3l3x')
    print(content.text)
    '''
broswer.close()