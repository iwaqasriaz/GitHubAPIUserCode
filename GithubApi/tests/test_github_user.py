from unittest import mock

from src.github_api import get_user, get_user_end, get_user_plan_info, get_users, update_profile
import allure


@allure.description("Mocking get user data reponse")
@allure.severity(severity_level="NORMAL")
@mock.patch("src.github_api.requests.get")
def test_get_user(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response",
                                               **{"status_code": 200, "json.return_value": {"id": "344"}})
    allure.attach(str(mock_requests_get().status_code),
                  name="Status code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(mock_requests_get().json()), name="response", attachment_type=allure.attachment_type.TEXT)
    assert get_user() == "344"  # replace this with your user id
    assert mock_requests_get().status_code == 200


@allure.description("Mocking get user data without auth reponse")
@allure.severity(severity_level="NORMAL")
@mock.patch("src.github_api.requests.get")
def test_get_user_without_auth(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response", **{"status_code": 401, "json.return_value": {
        'message': 'Requires authentication'}})
    allure.attach(str(mock_requests_get().status_code),
                  name="Status code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(mock_requests_get().json()), name="response", attachment_type=allure.attachment_type.TEXT)
    assert get_user_end() == 401
    assert mock_requests_get().status_code == 401


@allure.description("Mocking  users list")
@allure.severity(severity_level="NORMAL")
@mock.patch("src.github_api.requests.get")
def test_get_users_list(mock_requests_get):
    reponse_json = [{"login": "octocat"}, {"login":"gippy"}]

    mock_requests_get.return_value = mock.Mock(name="Mock response",
                                               **{"status_code": 200, "json.return_value": reponse_json})
    allure.attach(str(mock_requests_get().status_code),
                  name="Status code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(mock_requests_get().json()), name="response", attachment_type=allure.attachment_type.TEXT)
    assert len(get_users()) > 0
    assert mock_requests_get().status_code == 200


@allure.description("Mocking  user plan data response")
@allure.severity(severity_level="NORMAL")
@mock.patch("src.github_api.requests.get")
def test_get_user_plan(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="Mock response",
                                               **{"status_code": 200, "json.return_value": {"plan": {"name": "pro"}}})
    allure.attach(str(mock_requests_get().status_code),
                  name="Status code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(mock_requests_get().json()), name="response", attachment_type=allure.attachment_type.TEXT)
    assert get_user_plan_info() == 'pro'
    assert mock_requests_get().status_code == 200

@allure.description("Mocking user update prorfile response")
@allure.severity(severity_level="NORMAL")
@mock.patch("src.github_api.requests.patch")
def test_update_profile(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="Mock response",
                                               **{"status_code": 200, "json.return_value": {"name": "NewName"}})
    allure.attach(str(mock_requests_get().status_code),
                  name="Status code",
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(str(mock_requests_get().json()), name="response", attachment_type=allure.attachment_type.TEXT)
    assert update_profile()['name'] == "NewName"
    assert mock_requests_get().status_code == 200