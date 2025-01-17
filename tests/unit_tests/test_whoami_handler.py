# SPDX-License-Identifier: LGPL-2.1-or-later
#
# Copyright (C) 2022 Jeny Sadadia
# Author: Jeny Sadadia <jeny.sadadia@gmail.com>

# pylint: disable=unused-argument

"""Unit test function for KernelCI API whoami handler"""

from tests.unit_tests.conftest import BEARER_TOKEN


def test_whoami_endpoint(mock_get_current_user, mock_init_sub_id, test_client):
    """
    Test Case : Test KernelCI API /whoami endpoint
    Expected Result :
        HTTP Response Code 200 OK
        JSON with '_id', 'username', 'hashed_password'
        and 'active' keys
    """
    response = test_client.get(
        "whoami",
        headers={
            "Accept": "application/json",
            "Authorization": BEARER_TOKEN
        },
    )
    assert response.status_code == 200
    assert ('_id', 'username', 'hashed_password', 'active',
            'is_admin') == tuple(response.json().keys())
