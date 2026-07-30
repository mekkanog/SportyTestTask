import pytest

from actions.match_list_actions import MatchListPageActions

@pytest.mark.ui
def test_place_bet_on_upcoming_match(driver, app_url, bet_test_data):
    stake = bet_test_data["stake"]
    team_selection = bet_test_data["team_selection"]

    driver.get(app_url)
    match_list_actions = MatchListPageActions(driver)
    match_list_actions.make_bet_upcoming_match(team_selection, stake)
    match_list_actions.verify_placed_bet(stake)
