import pytest

from services.planets_client import PlanetsApiClient


@pytest.fixture(scope="session")
def planets_api():
    """return panets APi object, closes connection after all tests"""
    pl_api = PlanetsApiClient()
    yield pl_api
    pl_api.close()
