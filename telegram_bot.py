from selenium import webdriver
from time import sleep
import payload


def send(result):
    if result != []:
        for x in result:
            # write text message
            message = x.replace(" ", "%20")
            url = f"https://api.telegram.org/bot{payload.API_KEY}/sendMessage?chat_id={payload.chat_id}&text={message}"
            path = "C:\Program Files (x86)\chromedriver.exe"
            # launch Chrome
            driver = webdriver.Chrome(path)
            driver.get(url)

            # quit and close browser
            driver.quit()
            sleep(1)
