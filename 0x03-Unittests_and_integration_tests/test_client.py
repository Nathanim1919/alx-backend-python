#!/usr/bin/env python3
"""Test client module
"""


from typing import Dict
import unittest
from urllib.error import HTTPError
from parameterized import parameterized, parameterized_class
from client import (GithubOrgClient)
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test client module"""

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org"""
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload
        org = GithubOrgClient(org_name)
        self.assertEqual(org.org, expected_payload)
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name)
        )

    def test_public_repos_url(self) -> None:
        """Test public repos url"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                'https://api.github.com/orgs/google/repos',
            )

    def test_public_repos(self) -> None:
        """Test public repos"""
        with patch("client.get_json") as mock_get_json:
            test_payload = {
                'repos_url': "https://api.github.com/users/google/repos",
                'repos': [
                    {
                        "id": 7697149,
                        "name": "episodes.dart",
                        "private": False,
                        "owner": {
                            "login": "google",
                            "id": 1342004,
                        },
                        "fork": False,
                        "url":
                        "https://api.github.com/repos/google/episodes.dart",
                        "created_at": "2013-01-19T00:31:37Z",
                        "updated_at": "2019-09-23T11:53:58Z",
                        "has_issues": True,
                        "forks": 22,
                        "default_branch": "master",
                    },
                    {
                        "id": 8566972,
                        "name": "kratu",
                        "private": False,
                        "owner": {
                            "login": "google",
                            "id": 1342004,
                        },
                        "fork": False,
                        "url": "https://api.github.com/repos/google/kratu",
                        "created_at": "2013-03-04T22:52:33Z",
                        "updated_at": "2019-11-15T22:22:16Z",
                        "has_issues": True,
                        "forks": 32,
                        "default_branch": "master",
                    },
                ]
            }
            mock_get_json.return_value = test_payload["repos"]
            with patch(
                    'client.GithubOrgClient._public_repos_url',
                    new_callable=PropertyMock
                    ) as mock_public_repos_url:
                mock_public_repos_url.return_value = test_payload["repos_url"]
                self.assertEqual(
                    GithubOrgClient('google').public_repos(),
                    ["episodes.dart", "kratu"],
                )
                mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Test has license"""
        client_has_license = GithubOrgClient('google').has_license(repo, key)
        self.assertEqual(client_has_license, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
