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

subreddits_list = []

def make_subs_list(*categories):
    # pa dast small
    for category in categories:
        for sub in category:
            if sub not in subreddits_list:
                subreddits_list.append(sub)


def pin_posts():
    driver.get("https://www.reddit.com/posts/")
    time.sleep(uniform(4, 7))
    for i in range (0, 4):
        driver.find_elements_by_css_selector('._2pFdCpgBihIaYh9DSMWBIu')[i].click()
        time.sleep(uniform(1, 2.5))
        driver.find_element_by_xpath("//*[contains(text(), 'Pin Post to Profile')]").click()
        time.sleep(uniform(2, 5))
      
def delete_posts(number):

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


def post_in_all_subs(title, image_url, subreddits_list):
    for subreddit in subreddits_list:
        if subreddit not in four_subreddits:   
            if subreddit in div4:
                div_number = "4"
            else:
                div_number = "3"
            # Go to the subreddit
            driver.get(subreddit+"submit")
            # driver.get(subreddit)
            time.sleep(uniform(6, 10))
            # Go to link tab
            link_tab = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div['+ div_number +']/div[1]/div/button[3]')
            # link_tab = wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, ('Z1w8VkpQ23E1Wdq_My3U4 ')[1])))
            # link_tab = driver.find_elements_by_class_name('Z1w8VkpQ23E1Wdq_My3U4 ')[2]
            link_tab.click()
            time.sleep(uniform(1.2, 2))
            # Click on Title
            title_form = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div['+ div_number +']/div[2]/div[1]/div/textarea')
            title_form.click()
            time.sleep(uniform(1.5, 2))
            # Check if the title needs OC
            if subreddit in subs_to_add_oc:
                title_form.send_keys(title+" (OC)")
                # slow_typing(title_form, title+" (OC)")
            elif subreddit in specific_titles:
                slow_typing(title_form, specific_titles[subreddit])
            else:
                # slow_typing(title_form,title)
                title_form.send_keys(title)
            time.sleep(uniform(1.5, 2))
            # Click on url
            url_form = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div['+ div_number +']/div[2]/div[2]/textarea')
            url_form.click()
            time.sleep(uniform(1, 2))
            # Paste the link
            url_form.send_keys(image_url)
            # slow_typing(url_form, image_url)
            time.sleep(uniform(1.2, 2.2))
            # Check if the sub has flairs
            if subreddit in flair_dictionary:
                # Add flair
                add_flair(subreddit, flair_dictionary[subreddit])
            # Post
            post = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div['+ div_number +']/div[3]/div[2]/div/div[1]/button')
            post.click()
            time.sleep(uniform(6, 12))
