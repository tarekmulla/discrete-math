"""test pytest"""

from unittest import mock

from app.api import generate_questions


def test_pytest():
    """test pytest framework"""
    with mock.patch("app.api.get_request") as mock_get_request:
        mock_get_request.return_value.accept.side_effect = {
            "questions": [{"question": "test1"}, {"question": "test2"}]
        }
        generate_questions("token")
        assert 1 == 1
