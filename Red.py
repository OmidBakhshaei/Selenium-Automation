import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import uniform


PATH = "C:\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# User.send_keys(Keys.CONTROL+Keys.PAGE_DOWN)

def slow_typing(element, text): 
   for character in text: 
      element.send_keys(character)
      time.sleep(uniform(0.15, 0.4))

SelectedTitle = "*"
Subreddit = "*"
PhotoLink = "*"
Username = "*"
Password = "*"

# Go to Login page
driver.get("https://www.reddit.com/login/")

time.sleep(uniform(8, 10))

# Type Username
User = driver.find_element_by_xpath("//*[@id='loginUsername']")
slow_typing(User, Username)

time.sleep(uniform(1.5, 3))

# Type Password
Pass = driver.find_element_by_xpath('//*[@id="loginPassword"]')
slow_typing(Pass, Password)

time.sleep(uniform(0.5, 1.5))

# Enter and Sign in
User.send_keys(Keys.ENTER)

time.sleep(uniform(8, 13))

# Go to the subreddit
driver.get(Subreddit)

time.sleep(uniform(5, 9))

# Add a new post
NewPost=driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[1]/input')
NewPost.click()

time.sleep(uniform(4, 6))

# Go to link tab
ToLink = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div/button[3]')
ToLink.click()

time.sleep(uniform(1.5, 3))

#Click on Title
Title = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div/textarea')
Title.click()

time.sleep(uniform(1.5, 2))

#Type the Title
slow_typing(Title,SelectedTitle)

time.sleep(uniform(1.5, 2))

#Click on url
url = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/textarea')
url.click()

time.sleep(uniform(1, 2))

#Type the link
slow_typing(url,PhotoLink)

time.sleep(uniform(1.5, 2.5))

#Click on NS
ns = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[1]/div/button[3]')
ns.click()

time.sleep(uniform(1.5, 2.5))

#Click on OC
oc = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[1]/div/button[1]/div')
oc.click()
