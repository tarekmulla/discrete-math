'''test pytest'''
from app import api  # type: ignore
from unittest import mock


def test_pytest():
    '''test pytest framework'''
    with mock.patch("app.api.get_request") as mock_get_request:
        mock_get_request.return_value.accept.side_effect = {
            "questions": [
                {"question": "test1"},
                {"question": "test2"}
            ]
        }
        api.generate_questions('token')
        assert 1 == 1
