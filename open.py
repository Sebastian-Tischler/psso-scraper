from selenium import webdriver
from selenium.webdriver.common.by import By
import payload


def open_psso():
    path = "C:\Program Files (x86)\chromedriver.exe"

    # launch Chrome
    driver = webdriver.Chrome(path)

    # load PSSO
    driver.get(
        "https://psso.th-koeln.de/qisserver/rds?state=user&type=1&category=auth.login&startpage=portal.vm"
        "&breadCrumbSource=portal")

    # login
    driver.find_element(By.NAME, "asdf").send_keys(payload.username)
    driver.find_element(By.NAME, "fdsa").send_keys(payload.password)
    driver.find_element(By.NAME, "submit").click()

    # go to desired location
    driver.find_element(By.PARTIAL_LINK_TEXT, "Prüfungsverwaltung").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Notenspiegel").click()
    driver.find_element(By.PARTIAL_LINK_TEXT, "Abschluss BA Bachelor-Studiengang").click()
    driver.find_element(By.XPATH, "/html/body/div/div[6]/div[2]/form/ul/li/ul/li/a").click()

    # save in variable all the page source that was loaded
    noten = driver.page_source

    # quit and close browser
    driver.quit()

    return noten
