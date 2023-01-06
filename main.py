#Imports
import random
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import tweepy
import keys
import os
import time

#This makes the chromedriver operate without a tab.
options = Options()
options.add_argument("--headless")

#creating a driver for Chrome
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/travel/flights")

#Reaching the destination exploration page.
exploreDestinations = driver.find_element(By.XPATH,
                                          "//*[@id='yDmH0d']/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div/div/div[1]/div[3]/div/button")
exploreDestinations.click()
URL = driver.current_url

def scraping():
    """
    function gets all the destinations recommended from the current map

    :return: list of destinations
    """ 
    pass
def scraping():
    time.sleep(7)
    allDestinations = driver.find_elements(By.XPATH, "//li[@data-rank]")

    data = []
    for p in range(int(len(allDestinations))):
        data.append(allDestinations[p].text.replace("\n", " "))

    return data

def target(area):
    """
    target searches for the area of interest on Google Flights
    
    area: A string that represents the area of interest of travel

    :return:list of destinations
    """ 
    pass
def target(area):
    driver.get(URL)
    time.sleep(4)
    zoomOut = driver.find_element(By.XPATH, "//button[@aria-label='Zoom out']")
    zoomOut.click()

    if len(area) > 2:
        whereTo = driver.find_element(By.XPATH, "//input[@placeholder='Where to?']")
        time.sleep(2)
        whereTo.send_keys(area[0])  # why won't it let me input more places
        time.sleep(2)

        whereToClick = driver.find_element(By.XPATH, "//li[@aria-label='" + area + "']")
        time.sleep(1)
        whereToClick.click()

    data = scraping()
    return data

def api():
    """
    api returns the necessary authentication for the twitter bot

    :return: authentication needed
    """ 
    pass
def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

def tweet(api, message, image_path):
    """
    tweet will tweet the message and image from the twitter account
    api: authentication needed for twitter bot
    message: string that will be tweeted
    image_path: absolute path of the image that will be tweeted

    :return:
    """ 
    pass
def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)


data=[]
data = data + (target('Europe'))
data = data + (target('Asia'))
data = data + (target(""))
data = [*set(data)]
# for numberDestinations in range(len(data)):
#     print(data[numberDestinations])
# time.sleep(1)


tweeted = 'Couple of current flight deals on Google Flights! \n'
for c in range(4):
    tweeted = tweeted + data[random.randint(0, len(data))]+'\n'


if __name__ == '__main__':
    api = api()
    tweet(api, tweeted, None)
    print('tweeted')
