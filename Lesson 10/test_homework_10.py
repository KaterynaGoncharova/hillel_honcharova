import pytest
from unittest.mock import patch
import logging
from homework_10 import log_event

@patch('logging.Logger.info')
def test_log_event_success(mock_info):
    log_event("user1", "success")
    mock_info.assert_called_once_with("Login event - Username: user1, Status: success")

@patch('logging.Logger.warning')
def test_log_event_expired(mock_warning):
    log_event("user2", "expired")
    mock_warning.assert_called_once_with("Login event - Username: user2, Status: expired")

@patch('logging.Logger.error')
def test_log_event_failed(mock_error):
    log_event("user3", "failed")
    mock_error.assert_called_once_with("Login event - Username: user3, Status: failed")

@patch('logging.Logger.error')
def test_log_event_unexpected_status(mock_error):
    log_event("user4", "unknown_status")
    mock_error.assert_called_once_with("Login event - Username: user4, Status: unknown_status")
