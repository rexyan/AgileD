import os
import pytest


@pytest.fixture(scope='session', autouse=True)
def checkout_test_env():
    before_service_env = os.environ.get('MODE', "")
    os.environ["SERVICE_TAGS"] = "DEV"
    yield
    os.environ["SERVICE_TAGS"] = before_service_env
