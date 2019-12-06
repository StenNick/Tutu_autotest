from pages.Avia.AviaPage import SearchFlight

def test_tutu_page(browser):
    tutu_main_page = SearchFlight(browser)
    tutu_main_page.go_to_site()
    tutu_main_page.driver.implicitly_wait(10)
    tutu_main_page.check_avia_section()
    tutu_main_page.enter_data()
    # choose an air fare
    tutu_main_page.driver.implicitly_wait(10)
    tutu_main_page.choose_an_air_fare()

