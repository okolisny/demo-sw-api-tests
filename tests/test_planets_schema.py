import jsonschema
import pytest


@pytest.fixture(scope="module")
def planets_schema(planets_api):
    """Return planets JSON schema"""
    return planets_api.get_planets_schema()


@pytest.mark.skip(reason="planets schema API fails as of today")
def test_planets_schema(planets_schema, planets_api):
    """validate planets according to JSON schema"""
    status, planets = planets_api.get_planets()
    assert status == 200
    planets = planets["results"]

    for p in planets:
        assert jsonschema.validate(p, planets_schema)
