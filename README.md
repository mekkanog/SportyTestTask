# SportyTestTask

Test automation project for the Sporty QA assignment. It validates the core
bet-placement flow of the football betting application through both its web UI
and API.

The project uses:

- `pytest` as the test runner;
- `requests` for API tests;
- `Selenium WebDriver` for browser UI tests;
- JSON files for parametrized test data;
- the Page Object pattern to separate locators, page interactions, and test
  scenarios.

## Project structure

```text
.
├── actions/        # Reusable high-level UI actions and assertions
├── api/            # API client for matches and bet placement
├── data/           # Parametrized test data
├── locators/       # Selenium element locators
├── manualPart/     # Manual test cases, bug reports, and QA recommendations
├── pages/          # Page Object classes and low-level UI interactions
├── tests/
│   ├── api/        # API scenarios
│   ├── ui/         # Browser UI scenarios
│   └── conftest.py # Shared fixtures and environment configuration
├── pytest.ini      # pytest paths and marker definitions
└── requirements.txt
```

## Installation

### Prerequisites

- Python 3.10 or newer;
- Google Chrome for the default UI test run. Firefox and Edge are also
  supported by the WebDriver fixture;

Clone the repository, open its directory, and create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Selenium Manager resolves the required browser driver automatically. Make sure
the selected browser is installed and available on the machine.

## Running the tests

Run the complete test suite:

```bash
pytest
```

Run only API tests:

```bash
pytest -m api
```

Run only UI tests:

```bash
pytest -m ui
```


The tests target the assignment environment and its predefined test user by
default. These values can be overridden with environment variables:

```bash
BASE_URL="https://example.test/" \
BET_API_URL="https://example.test/api/place-bet" \
USER_ID="test-user-id" \
```

> **Note:** Successful scenarios place real bets for the configured test user
> and reduce that user's balance. Use a dedicated test account with sufficient
> funds.

## Test data

Bet stakes, selections, and optional match IDs are defined in
[`data/bet_test_data.json`](data/bet_test_data.json). Each entry is used as a
separate parametrized test case by both the API and UI suites.

Supported selections are `HOME`, `DRAW`, and `AWAY`. If `match_id` is omitted,
the API helper selects the first upcoming match returned by the matches API.

## Manual testing materials

The [`manualPart`](manualPart) directory contains the manual QA deliverables
that complement the automated suite:

- [`testplan.md`](manualPart/testplan.md) — risk-based manual test cases for
  successful betting, stake validation, retrying a failed bet, boundary values,
  duplicate submissions, and date filtering;
- [`testExecution.md`](manualPart/testExecution.md) — defects discovered during
  test execution, including reproduction steps, expected and actual results,
  severity, business impact, and links to supporting screenshots;
- [`StrategyRecommendations.md`](manualPart/StrategyRecommendations.md) — the
  proposed balance between automated and manual coverage, identified backend
  risks, CI test-suite recommendations, and improvements for test isolation;
- `BugScreenshots/` — evidence attached to the bug reports:
  - `multiplestake.png` — multiple bets submitted by repeated clicks;
  - `BalanceChange.png` — balance not refreshed after placing a bet;
  - `SuccessModal.png` — missing selection details in the success modal.

Together, these files document coverage beyond the current automated happy-path
checks and highlight the highest-risk areas for future automation.
