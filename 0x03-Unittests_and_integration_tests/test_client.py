#!/usr/bin/env python3
"""Test client module
"""


import unittest
from parameterized import parameterized
from client import (GithubOrgClient)
from unittest.mock import MagicMock, patch, PropertyMock


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


if __name__ == "__main__":
    unittest.main()
