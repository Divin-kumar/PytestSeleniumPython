from selenium.webdriver.common.by import By


class FindAnAgent:
    def __init__(self,driver):
        self.driver=driver

    def click_rent_tab(self):
        self.driver.find_element(By.ID,"rentDrop").click()

    def click_ask_a_question(self):
        self.driver.find_element(By.LINK_TEXT,"Ask a Question").click()

    def click_set_a_property_alert(self):
        self.driver.find_element(By.XPATH,"//*[@id=\"staticSwiperSliderRent\"]/div[4]/ul/li[4]/a").click()

    def click_rent_radio_button(self):
        self.driver.find_element(By.ID,"listTypeR").click()

    def select_property_type(self):
        self.driver.find_element(By.ID,"textPropertyRent").click()

    def click_hostel(self):
        self.driver.find_element(By.ID,"propertyTypeRent_10053").click()

    def select_budget_list(self):
        self.driver.find_element(By.ID,"budgetRentDDList").click()

    def click_10k_to_15k(self):
        self.driver.find_element(By.ID,"budgetRent_11852-11853").click()

    def select_bed_room(self):
        self.driver.find_element(By.ID,"textBedRoom").click()

    def click_two(self):
        self.driver.find_element(By.ID,"bedrooms_11701").click()

    def select_floor_preference(self):
        self.driver.find_element(By.ID,"floorPref").click()

    def click_10th_floor_and_above(self):
        self.driver.find_element(By.XPATH,"//*[@id=\"floorPreferences\"]/div[2]/div[1]/div[1]/ul/li[3]").click()

    def enter_city(self):
        self.driver.find_element(By.ID,"keyword").send_keys("Erode")

    def confirm_city(self):
        self.driver.find_element(By.XPATH,"//*[@id=\"keyword_suggest\"]/div[2]/span").click()

    def enter_locality(self):
        self.driver.find_element(By.ID,"keywordLoc").send_keys("Perundurai, Erode")

    def confirm_locality(self):
        self.driver.find_element(By.XPATH,"//*[@id=\"keyword_suggest_Loc\"]/div[2]").click()

    def get_alert(self):
        self.driver.find_element(By.ID,"alertFrequency_1203433").click()

    def accept_t_and_c(self):
        self.driver.find_element(By.ID,"tnc").click()

    def post_req(self):
        self.driver.find_element(By.ID,"postReqLoginSubmit").click()

    def login_option(self):
        return self.driver.find_element(By.XPATH,"//*[@id=\"firstLoginDiv\"]/div[1]").text()

    def click_s(self):
        self.driver.find_element(By.XPATH,"/html/body/div/div/div[5]/div[1]/div[3]/form/div[1]/div[1]/div[1]").click()
