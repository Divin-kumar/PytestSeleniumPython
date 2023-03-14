from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver=driver

    def rent_tab(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"rentheading\"]")

    def click_rent_tab(self):
        self.rent_tab().click()

    def click_owner_properties(self):
        self.driver.find_element(By.XPATH,"//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[2]/div/div/div["
                                          "1]/ul/li[1]/a").click()

    def switch_tab(self):
        child_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(child_window_handle)

    def click_top_localities(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div").click()

    def click_pune_mumbai_it_corridor(self):
        self.driver.find_element(By.XPATH,
                                 "//*[@id=\"body\"]/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[1]/label").click()

    def click_done(self):
        self.driver.find_element(By.XPATH, "//*[@id=\"body\"]/div[1]/div/div[2]/div[1]/div/div[2]/div[2]").click()

    def select_property(self):
        self.driver.find_element(By.XPATH,"//*[@id=\"cardid65923719\"]/div/div[1]/div[2]/h2").click()

    def enter_your_name(self):
        self.driver.find_element(By.ID,"userName").send_keys('Divin Kumar S')

    def enter_your_email(self):
        self.driver.find_element(By.ID,"userEmail").send_keys("divinkumr67@gmail.com")

    def enter_you_number(self):
        self.driver.find_element(By.ID,"userMobile").send_keys("9688825747")

    def select_location_bar(self):
        self.driver.find_element(By.XPATH,"/html/body/header/section[1]/div/div[1]/div[2]/a").click()

    def select_location(self):
        self.driver.find_element(By.XPATH,"/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()

    def click_search(self):
        self.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[4]").click()

    def click_top_agents(self):
        self.driver.find_element(By.LINK_TEXT,"Top Agents").click()

    def click_rent_bar(self):
        self.driver.find_element(By.XPATH,"//*[@id=\"tabRENT\"]").click()

    def click_find_an_agent(self):
        self.driver.find_element(By.XPATH,"//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[2]/div/div/div[4]/ul/li[3]/a").click()
