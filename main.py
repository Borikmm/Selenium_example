from selenium import webdriver
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# C:\All2\programming\Languages\Python\Selenium_program

class main:

    MY_USER_AGENT = "your_user_agent"
    MY_PROXY = "190.107.236.173:999"

    FILE_NAME_PROFILE = "C:\\Users\\you\\AppData\\Local\\Microsoft\\Edge\\User Data"

    def __init__(self):
        service = Service("driver/msedgedriver.exe") # CREATE DRIVER FOR RUN BROWSER

        options = webdriver.EdgeOptions() # CREATE OPTIONS
        options.add_experimental_option("detach", True) # FOR CORRECTLY WORKING AND NOT DESTRIOY WINDOW
        options.add_argument(f"user-agent={self.MY_USER_AGENT}") # ADD USER_AGENT
        options.add_argument(f"user-data-dir={self.FILE_NAME_PROFILE}") #ADD USER DATA


        #options.add_argument(f"--proxy-server={self.MY_PROXY}") # ADD PROXY

        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])

        try:
            #self.browser = webdriver.Edge(options=options, service=service) # CREATE MAIN BROWSER WINDOW
            self.browser = webdriver.Edge(options=options) # CREATE MAIN BROWSER WINDOW
        except Exception as exc:
            print(exc)
            print("Браузер упал...")

    def __del__(self):
        self.__start()

    def __create_tab(self, url, name_page):
        self.browser.execute_script(f"window.open('{url}', '{name_page}')")

    def __close_page(self, name_page):
        if (type(name_page) == int):
            self.browser.switch_to.window(self.browser.window_handles[name_page])
        else:
            self.browser.switch_to.window(name_page)
        self.browser.close()

    def __change_page(self, name_page):
        self.browser.switch_to.window(name_page)

    def __start(self):
        self.__create_tab("https://vk.com/", "vk")

        #
        self.__close_page(0) # CLOSE FIRST HOLLOW PAGE

if __name__ == "__main__":
    main()