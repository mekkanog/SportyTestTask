import pytest

from api.match_list_api import MatchListApi

# Run parametrized test to check betting functionality based on data from bet_test_data.json
@pytest.mark.api
def test_place_bet_with_stake(
    bet_api_url,
    base_url,
    user_id,
    bet_test_data,
):
    response = MatchListApi.place_bet(
        bet_api_url,
        base_url,
        bet_test_data["stake"],
        bet_test_data["team_selection"],
        user_id,
        match_id=bet_test_data.get("match_id"),
    )
    assert response.status_code in (200, 201), (
        f"Expected successful response, got {response.status_code}: "
        f"{response.text}"
    )
    response_data = response.json()
    actual_stake = response_data.get("stake")
    assert str(actual_stake) == str(bet_test_data["stake"]), (
        f"Expected stake {bet_test_data["stake"]!r}, got {actual_stake!r}"
    )
