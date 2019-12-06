from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class RunTest():

    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.tutu.ru")
        driver.implicitly_wait(5)
        
        aviaTab = driver.find_element_by_class_name("tab_avia")
        trainTab = driver.find_element_by_class_name("tab_train")
        busTab = driver.find_element_by_class_name("tab_bus")
        localTrain = driver.find_element_by_class_name("tab_etrain")
        toursTab = driver.find_element_by_class_name("tab_tours")
        hotelTab = driver.find_element_by_class_name("tab_hotels")
        adventuresTab = driver.find_element_by_class_name("tab_trip")

        aviaTab.click()

        inputCityFrom = driver.find_elements_by_name("city_from")
        inputCityFrom[0].clear()
        inputCityFrom[0].send_keys("Москва (Россия)")
 
       
        inputCityTo = driver.find_elements_by_name("city_to")
        inputCityTo[0].clear()
        inputCityTo[0].send_keys("Париж (Франция)")



        inputDateFrom = driver.find_elements_by_name("date_from")
        inputDateFrom[0].clear()
        inputDateFrom[0].send_keys("28.12.2019")


        inputDateBack = driver.find_elements_by_name("date_back")
        inputDateBack[0].clear()
        inputDateBack[0].send_keys("05.01.2020")

        addAdultPassenger = driver.find_elements_by_class_name("increase")
        addAdultPassenger[0].click()

        findTickets = driver.find_elements_by_class_name("j-button-submit")
        findTickets[0].click()

        # finding page
        driver.implicitly_wait(10)
        selectBaggage = driver.find_elements_by_name("baggage")
        selectBaggage[0].click()
        time.sleep(2)
        refundTicket = driver.find_elements_by_name("refundability")
        refundTicket[0].click()
        time.sleep(2)

        buyTicket = driver.find_elements_by_class_name("rm-content_block")
        buyTicket[4].click()
        time.sleep(2)


ff = RunTest()
ff.test()
  

