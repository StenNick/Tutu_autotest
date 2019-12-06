from src.tests_folder.basePage import BasePage
from selenium.webdriver.common.by import By
import time


class AviaLocators:
    locator_aviaTab = (By.CLASS_NAME, "tab_avia")
    locator_toursTab = (By.CLASS_NAME, "tab_tours")
    locator_adventuresTab = (By.CLASS_NAME, "tab_trip")

    locator_inputCityFrom = (By.NAME, "city_from") # [0]
    locator_inputCityTo = (By.NAME, "city_to") # [0]
    locator_inputDateFrom = (By.NAME, "date_from") # [0]
    locator_inputDateBack = (By.NAME, "date_back") # [0]
    locator_addAdultPassenger = (By.CLASS_NAME, "increase") # [0]
    locator_findTickets = (By.CLASS_NAME, "j-button-submit") # [0]

    # offers page
    locator_selectBaggage = (By.NAME, "baggage")
    locator_refundTicket = (By.NAME, "refundability")
    locator_buyTicket = (By.CLASS_NAME, "rm-content_block")
 

class SearchFlight(BasePage):
    def check_avia_section(self):
        aviaTab = self.find_element(AviaLocators.locator_aviaTab)
        aviaTab.click()

    # enter data passengers
    def enter_data(self):
        # city from
        input_City_From = self.find_element(AviaLocators.locator_inputCityFrom)
        input_City_From.click()
        input_City_From.clear()
        input_City_From.send_keys("Москва (Россия)")
        
        # city to
        input_City_To = self.find_element(AviaLocators.locator_inputCityTo)
        input_City_To.click()
        input_City_To.clear()
        input_City_To.send_keys("Париж (Франция)")

        # date from
        input_Date_From = self.find_element(AviaLocators.locator_inputDateFrom)
        input_Date_From.click()
        input_Date_From.clear()
        input_Date_From.send_keys("28.12.2019")

        # date back
        input_Date_Back = self.find_element(AviaLocators.locator_inputDateBack)
        input_Date_Back.click()
        input_Date_Back.clear()
        input_Date_Back.send_keys("05.02.2020")

        # add passangers
        addAdultPassenger = self.find_element(AviaLocators.locator_addAdultPassenger)
        addAdultPassenger.click()

        # find Tickets
        findTickets = self.find_element(AviaLocators.locator_findTickets)
        findTickets.click()
        time.sleep(2)

    # choose fare
    def choose_an_air_fare(self):
        selectBaggage = self.find_elements(AviaLocators.locator_selectBaggage)
        selectBaggage[0].click()

        refundTicket = self.find_elements(AviaLocators.locator_refundTicket)
        refundTicket[0].click()

        buyTicket = self.find_elements(AviaLocators.locator_buyTicket)
        buyTicket[4].click()

