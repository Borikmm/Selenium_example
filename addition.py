from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

def main():
    driver = webdriver.Chrome()
    driver.get("https://anceta.chtotib.ru/")

    b = driver.find_element(By.XPATH, "//select[@name='group']")

    sleep(0.005)

    select = Select(b)
    select.select_by_index(13)

    sleep(0.005)

    driver.find_element(By.XPATH, "//input[@name='submit_group']").click()

    sleep(0.005)

    el = driver.find_elements(By.XPATH, "//input")

    c = 0
    for a in range(11, len(el)):
        try:
            if c == 28: c = 0
            c += 1
            if c == 4 or c == 5: continue
            else:
                sleep(.005)
                el[a].click()
        except:
            pass

    driver.close()

while True:
    main()
