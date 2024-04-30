import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

YOUR_EMAIL = YOUR_EMAIL
YOUR_USERNAME = YOUR_USERNAME
YOUR_PASSWORD = YOUR_PASSWORD


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        accept_cookies = self.driver.find_element(by=By.CSS_SELECTOR, value="#onetrust-accept-btn-handler")
        accept_cookies.click()
        start_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button")
        start_button.click()
        time.sleep(45)
        download_speed = float(self.driver.find_element(by=By.CSS_SELECTOR, value=".download-speed").text)
        upload_speed = float(self.driver.find_element(by=By.CSS_SELECTOR, value=".upload-speed").text)
        return [download_speed, upload_speed]

    def tweet_at_provider(self, internet_speeds):
        self.driver.get("https://twitter.com/home")
        time.sleep(2)
        email = self.driver.find_element(by=By.CSS_SELECTOR, value="input[autocomplete='username']")
        email.send_keys(YOUR_EMAIL, Keys.ENTER)
        time.sleep(2)
        username = self.driver.find_element(by=By.CSS_SELECTOR, value="input[inputmode='text']")
        username.send_keys(YOUR_USERNAME, Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(by=By.CSS_SELECTOR, value="input[autocomplete='current-password']")
        password.send_keys(YOUR_PASSWORD, Keys.ENTER)
        time.sleep(5)
        tweet_input = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_input.send_keys(f"Hi @Dell why is my internet speed {internet_speeds[0]} down / {internet_speeds[1]} up when I pay for 150 down / 10 up")
        time.sleep(2)
        send_tweet = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        send_tweet.click()

