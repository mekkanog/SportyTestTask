# On this file are described actions for match_list page,

from pages.match_list_page import MatchListPage
from locators.match_list_locators import MatchListLocators
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from decimal import Decimal

class MatchListPageActions:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.match_list_page = MatchListPage(driver, timeout)
        self.wait = WebDriverWait(driver, timeout)

    # Make bet for upcoming match in current state it will search first upcoming match and will make a bet
    # which is specified in bet_test_data.json file
    def make_bet_upcoming_match(self, match_result, stake):
        match_card = self.match_list_page.find_upcoming_match()
        self.match_list_page.select_odds(match_card, match_result)
        self.match_list_page.fill_stake(stake)
        self.match_list_page.place_button_click()

    # Check that placed bet are reflected in success modal. There is also should be result of match which we select but
    # because of the bug right now we are not able to see result in modal window
    def verify_placed_bet(self, stake) -> None:
        expected_stake = str(stake)
        stake_element = self.wait.until(
            EC.visibility_of_element_located(
                MatchListLocators.success_modal_stake
            )
        )

        if expected_stake not in stake_element.text:
            raise AssertionError(
                f"Success modal stake {stake_element.text!r} does not "
                f"contain {expected_stake!r}"
            )
