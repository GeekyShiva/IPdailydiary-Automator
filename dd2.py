#Notes for the readed
# enter Enrollment Number and Nucleus password
# Check tag value for your system at line 39,49,57,61
# Install selenium and run this code
# Enjoy !! and follow @pandastichuman on Twitter.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time
usernameStr = 'Enrollment Number'
passwordStr = 'Nucleus Password'

browser = webdriver.Chrome()
browser.get(('https://nucleus.niituniversity.in/'))

# fill in username and hit the next button

username = browser.find_element_by_id('SchSel_txtUserName')
username.send_keys(usernameStr)

#nextButton = browser.find_element_by_id('')
#nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 15).until(
    EC.presence_of_element_located((By.NAME, "SchSel$txtPassword")))

password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('SchSel_btnLogin')
signInButton.click()

time.sleep(5)

daily_diary = browser.find_element_by_id('ctl000_ContentPlaceHolder1_btnDDiary')
daily_diary.click()

time.sleep(3)
select = Select(browser.find_element_by_name('ctl00$ContentPlaceHolder1$Timeinhr'))

# select by visible text
select.select_by_visible_text('10')

time.sleep(3)
select = Select(browser.find_element_by_name('ctl000$ContentPlaceHolder1$Timeouthr'))

# select by visible text
select.select_by_visible_text('20')

time.sleep(3)
diaryStr =  ' I am a bot created by author: particle_panda and I fill this diary on behalf of him: (UPDATE) I had a productive day, completed all programing tasks assigned.'

diary = browser.find_element_by_name('ctl000$ContentPlaceHolder1$txtDesc')
diary.send_keys(diaryStr)

time.sleep(5)
SubmitButton = browser.find_element_by_name('ctl000$ContentPlaceHolder1$btnSubmit')
SubmitButton.click()

time.sleep(5)

browser.close()
#browser.find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click()

# select by value
#select.select_by_value('1')