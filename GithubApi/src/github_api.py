import requests
import allure

headers = {'Authorization': 'token ' + "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", 'Content-Type': 'application/json'}


@allure.step("Calling get_user with authentication")
def get_user():
    r = requests.get("https://api.github.com/user", headers=headers)
    return r.json()['id']


@allure.step("Calling get_user endpoint without authentication")
def get_user_end():
    r = requests.get("https://api.github.com/user")
    return r.status_code


@allure.step("Calling get_userd endpoint")
def get_users():
    r = requests.get("https://api.github.com/users")
    # for i in r.json():
    #     print(i)
    return r.json()

@allure.step("Calling get_user_plan info endpoint")
def get_user_plan_info():
    r = requests.get("https://api.github.com/users/USERNAME")
    return r.json()['plan']['name']

@allure.step("Calling udpate profile data endpoint")
def update_profile():
    r = requests.patch("https://api.github.com/user", data={"name":"Changed Name"}, headers=headers)
    return r.json()

if __name__ == "__main__":
    print(get_users())
