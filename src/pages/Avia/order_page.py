from src.tests_folder.basePage import BasePage
from selenium.webdriver.common.by import By
import time


class AviaLocators:
    # Choose type of trip
    # personal or working
    locator_personal_trip = (By.CLASS_NAME, "dist__button__2cQyl")
    locator_working_trip = (By.CLASS_NAME, "dist__button__2cQyl")
    # passengers
    locator_count_passengers = (By.CLASS_NAME, "j-passenger_item")
    locator_first_name = (By.NAME, "first_name")
    locator_last_name = (By.NAME, "last_name")
    locator_gender = (By.CLASS_NAME, "j-gender_group") # надо придумать как выбрать доч эл
    locator_date_birthday = (By.NAME, "birthday")
    locator_document_number = (By.NAME, "document_number")
    locator_document_expiration_date = (By.NAME, "document_expiration_date")
    locator_delete_passenger = (By.CLASS_NAME, "j-delete_passenger")
    locator_add_passenger = (By.CLASS_NAME, "j-add_more")
    # Customer
    locator_Customer_last_name = (By.ID, "id_input_user_sname")
    locator_Customer_first_name = (By.ID, "id_input_user_name")
    locator_Customer_number_phone = (By.ID, "id_input_user_phone")
    locator_Customer_email_phone = (By.ID, "id_input_user_email")
    # submit order
    locator_button_submit = (By.CLASS_NAME, "j-button-submit")


class CheckoutOrder(BasePage):
    def selectType(self, typeTrip):
        any_type_trip = self.find_elements(AviaLocators.locator_personal_trip)
        any_type_trip[typeTrip].click()

    def fill_order(self, indexPassenger, FirstName, LastName, genderIndex, numberDocument):
        count_passengers = self.find_elements(AviaLocators.locator_count_passengers)
        if str(len(count_passengers)) > 1:
            first_name = self.find_elements(AviaLocators.locator_first_name)
            first_name[indexPassenger].clear()
            first_name[indexPassenger].send_keys(FirstName)

            last_name = self.find_elements(AviaLocators.locator_last_name)
            last_name[indexPassenger].clear()
            last_name[indexPassenger].send_keys(LastName)

            # male or female
            select_gender = self.find_elements(AviaLocators.locator_gender)
            select_gender[genderIndex].click()

            # input number passport
            number_document = self.find_elements(AviaLocators.locator_document_number)
            number_document[indexPassenger].clear()
            number_document[indexPassenger].send_key(numberDocument)


