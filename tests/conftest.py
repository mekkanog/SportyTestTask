"""Shared pytest fixtures for the Sporty UI test suite."""

from __future__ import annotations

import json
import os
from pathlib import Path


import pytest
from selenium import webdriver


DEFAULT_BASE_URL = "https://qae-assignment-tau.vercel.app/"
DEFAULT_BET_API_URL = f"{DEFAULT_BASE_URL}api/place-bet"
DEFAULT_USER_ID = "candidate-rTOjxcoVTL"
BET_TEST_DATA_FILE = (
    Path(__file__).resolve().parents[1] / "data" / "bet_test_data.json"
)


def load_bet_test_cases():
    with BET_TEST_DATA_FILE.open(encoding="utf-8") as file:
        test_cases = json.load(file)
    return [
        pytest.param(test_data, id=test_name)
        for test_name, test_data in test_cases.items()
    ]


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", DEFAULT_BASE_URL)


@pytest.fixture(scope="session")
def user_id():
    return os.getenv("USER_ID", DEFAULT_USER_ID)


@pytest.fixture(scope="session")
def app_url(base_url, user_id):
    return f"{base_url.rstrip('/')}/?user-id={user_id}"


@pytest.fixture(scope="session")
def bet_api_url():
    return os.getenv("BET_API_URL", DEFAULT_BET_API_URL)


@pytest.fixture(scope="session", params=load_bet_test_cases())
def bet_test_data(request):
    return request.param


@pytest.fixture()
def driver(request):
    browser = getattr(request, "param", "chrome")
    print("inside driver:", browser)

    if browser == "chrome":
        web_driver = webdriver.Chrome()
    elif browser == "firefox":
        web_driver = webdriver.Firefox()
    elif browser == "edge":
        web_driver = webdriver.Edge()
    else:
        pytest.fail(f"Unsupported browser: {browser}")

    print("Setting up WebDriver...")
    yield web_driver
    print("Closing WebDriver...")
    web_driver.quit()
