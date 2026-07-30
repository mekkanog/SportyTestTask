from datetime import date

import requests


class MatchListApi:
    @staticmethod
    def _request_headers(user_id):
        return {
            "x-user-id": user_id,
        }

    @staticmethod
    def get_upcoming_match_id(
        base_url: str,
        user_id: str,
    ):
        # Return match ID of the first upcoming match from the matches API
        api_url = f"{base_url.rstrip('/')}/api/matches"
        response = requests.get(
            api_url,
            headers=MatchListApi._request_headers(user_id),
            timeout=10,
        )

        response.raise_for_status()
        response_data = response.json()

        if not isinstance(response_data, list):
            raise ValueError(
                "Matches API response does not contain a match list"
            )

        # The API does not return status, so UPCOMING is based on kickoffDate.
        for match in response_data:
            kickoff_date = date.fromisoformat(match["kickoffDate"])
            if kickoff_date <= date.today():
                continue

            match_id = match.get("id")
            if match_id is None:
                raise ValueError("Upcoming match does not contain an ID")
            return match_id

        raise LookupError("No upcoming match was found")

    @staticmethod
    def place_bet(
        bet_api_url: str,
        base_url: str,
        stake: int,
        selection: str,
        user_id: str,
        match_id: str | int | None = None,
    ):
        # Place a bet through the API and verify the returned stake. If match id is not specified in bet_test_data.json
        # we will get the first upcoming match_id
        expected_stake = int(stake)
        if match_id is None:
            match_id = MatchListApi.get_upcoming_match_id(base_url, user_id)

        response = requests.post(
            bet_api_url,
            headers=MatchListApi._request_headers(user_id),
            json={
                "stake": expected_stake,
                "matchId": match_id,
                "selection": selection,
            },
            timeout=10,
        )
        return response
