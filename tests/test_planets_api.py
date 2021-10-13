

def test_planets_api_1(planets_api):
    """Get all planets"""
    st, planets = planets_api.get_planets()
    assert st == 200
