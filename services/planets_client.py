import json

from services.base_swapi import BaseSwApiClient


class PlanetsApiClient(BaseSwApiClient):
    """Client class for /planets API"""

    PLANETS_URL = "/planets/"
    PLANETS_ID_URL = "/planets/{id}"
    PLANETS_SCHEMA_URL = "/planets/schema/"

    def get_planets(self):
        """Get all planets"""
        res = self.client.get(self.BASE_URL + self.PLANETS_URL)
        return res.status_code, json.loads(res.content)

    def get_planets_by_id(self, planet_id):
        """
        Get planet by ID
        :param planet_id: ID of planet
        """
        url = self.PLANETS_ID_URL.format(id=planet_id)
        res = self.client.get(self.BASE_URL + url)
        return res.status_code, json.loads(res.content)

    def get_planets_schema(self):
        """Get planets API JSON schema"""
        res = self.client.get(self.BASE_URL + self.PLANETS_SCHEMA_URL)
        return json.loads(res.content)
