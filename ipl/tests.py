import json

from rest_framework import status
from rest_framework.test import APITestCase


class MatchTestCase(APITestCase):
    def test_create_match(self):
       response = self.client.get('match/?season=2017')
       self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response(self):
        response = self.client.get('match/?season=2017')
        data = [
            {
                "winner": "Mumbai Indians",
                "count": 12
            },
            {
                "winner": "Rising Pune Supergiant",
                "count": 10
            },
            {
                "winner": "Kolkata Knight Riders",
                "count": 9
            },
            {
                "winner": "Sunrisers Hyderabad",
                "count": 8
            }
        ]
        response = response['results']
        self.assertEqual(data,response)