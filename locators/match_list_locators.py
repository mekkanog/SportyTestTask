from selenium.webdriver.common.by import By


class MatchListLocators:
    # Main page
    date_filter = (By.ID, "date-filter-toggle")
    odds_filter = (By.ID, "odds-filter-toggle")
    match_cards = (By.CSS_SELECTOR, ".matchCard")
    badge = (By.CSS_SELECTOR, ".badge")
    odds_buttons = (By.CSS_SELECTOR, ".oddsButton")

    # Bet Slip
    stake_input = (By.ID, "bet-slip-stake-input")
    place_bet_button = (By.ID, "bet-slip-place-bet")

    # Success stake modal
    success_modal_stake = (By.ID, "modal-success-stake")
