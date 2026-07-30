from locators.match_list_locators import MatchListLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MatchListPage:
    ODDS_MAPPING = {
        "HOME": 0,
        "DRAW": 1,
        "AWAY": 2,
    }

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Find first upcoming match card
    def find_upcoming_match(self):
        match_cards = self.wait.until(
            EC.presence_of_all_elements_located(
                MatchListLocators.match_cards
            )
        )
        for match_card in match_cards:
            badges = match_card.find_elements(*MatchListLocators.badge)
            if any(
                badge.text.strip().upper() == "UPCOMING"
                for badge in badges
            ):
                return match_card

        raise NoSuchElementException(
            'No badge with the text "UPCOMING" was found'
        )

    # Selecting odds based on data from bet_test_data.json
    def select_odds(self, match_card, selection: str = "HOME") -> None:
        odds_buttons = match_card.find_elements(
            *MatchListLocators.odds_buttons
        )
        odds_index = self.ODDS_MAPPING[selection]
        odds_button = odds_buttons[odds_index]
        odds_button.click()

    # Enter value of stake in input. Data are taking from bet_test_data.json
    def fill_stake(self, stake) -> None:
        stake_input = self.wait.until(
            EC.element_to_be_clickable(MatchListLocators.stake_input)
        )
        stake_input.clear()
        stake_input.send_keys(str(stake))

    # Waiting when button "Place bet" will be available and click on it
    def place_button_click(self) -> None:
        self.wait.until(
            EC.element_to_be_clickable(MatchListLocators.place_bet_button)
        ).click()
