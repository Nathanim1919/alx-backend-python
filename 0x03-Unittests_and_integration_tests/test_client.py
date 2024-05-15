#!/usr/bin/env python3
"""Test client module
"""


import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


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


if __name__ == "__main__":
    unittest.main()
