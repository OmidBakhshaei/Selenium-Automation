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
      time.sleep(uniform(0.15, 0.35))

SelectedTitle = "*"
Subreddit = "*"
PhotoLink = "*"
Username = "*"
Password = "*"
flair = "*"
IncludesFlair = ["*"]

def slow_typing(element, text): 
   for character in text: 
      element.send_keys(character)
      time.sleep(uniform(0.15, 0.4))

      
def DeletePosts(number):

    while True :
        ToLink = driver.find_elements_by_css_selector('._2pFdCpgBihIaYh9DSMWBIu')[number]
        ToLink.click()
        time.sleep(uniform(1.5, 3))
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='delete']"))).click()
        time.sleep(uniform(1.5, 3))
        DeletePost = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/section/footer/button[2]')
        DeletePost.send_keys(Keys.TAB)
        time.sleep(uniform(0.2, 0.6))
        DeletePost.send_keys(Keys.TAB)
        time.sleep(uniform(0.2, 0.6))
        DeletePost.send_keys(Keys.TAB)
        time.sleep(uniform(0.2, 0.6))
        DeletePost.send_keys(Keys.ENTER)
        time.sleep(uniform(2, 4))      
      
# Go to Reddit's Login page
driver.get("https://www.reddit.com/login/")

time.sleep(uniform(5, 8))

# Type Username
User = driver.find_element_by_xpath("//*[@id='loginUsername']")

# User.send_keys(Keys.CONTROL+Keys.PAGE_DOWN)
    
slow_typing(User, Username)

time.sleep(uniform(1.5, 3))

# Type Password
Pass = driver.find_element_by_xpath('//*[@id="loginPassword"]')
slow_typing(Pass, Password)

time.sleep(uniform(0.5, 1.5))

# Enter and Sign in
User.send_keys(Keys.ENTER)

time.sleep(uniform(2, 5))

for subreddit in subreddits:

    # Go to the subreddit
    driver.get(subreddit)

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

    time.sleep(uniform(1, 2.5))


    # Check if the sub has flairs
    if subreddit in IncludesFlair :

        # Add flair
        Addflair = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/button[4]')
        Addflair.click()

        time.sleep(uniform(2, 4))

        searchFlair = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div/div[1]/input')
        searchFlair.click()

        time.sleep(uniform(1, 2))

        slow_typing(searchFlair, flair)

        time.sleep(uniform(1, 2))

        searchFlair.send_keys(Keys.TAB)
        time.sleep(uniform(0.3, 0.6))

        selectFlair = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[2]/div/div[2]/div')
        selectFlair.send_keys(Keys.ENTER)

        time.sleep(uniform(1, 2))

        applyFlair = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[4]/div/div/div/div[3]/button[1]')
        applyFlair.click()

        time.sleep(uniform(2, 4))

    # Send the post
    save = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[2]/button')
    save.click()

    time.sleep(uniform(4, 7)) 
