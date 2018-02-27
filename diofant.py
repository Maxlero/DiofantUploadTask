import time
from selenium import webdriver


# that script will stuck in case sending the right answer or already solved problem
def main():
    # set your info here
    login = ''
    password = ''

    url2 = 'http://www.diofant.ru/problem/3372/'  # task url

    chromedriver_path = '/home/maxlero/PycharmProjects/Library/chromedriver'  # path to chromedriver

    multiplier = 0  # starting values
    start_value = 36  # starting values

    # init browser
    browser = webdriver.Chrome(executable_path=chromedriver_path)

    # login process
    url1 = 'http://www.diofant.ru/accounts/login/'
    browser.get(url1)
    browser.execute_script("document.getElementById('username').value = '" + login + "';")
    browser.execute_script("document.getElementsByName('password')[0].value = '" + password + "';")
    browser.execute_script("document.getElementById('login_form').submit();")

    # opening task url
    browser.get(url2)

    print("Start sending answers:")
    for x in range(0, 4050):
        browser.execute_script(
            "document.getElementById('r_answer_input').value = '" + str(start_value * multiplier) + "';")
        time.sleep(31)
        print("Sleep for 31s..")
        browser.execute_script("javascript:on_submit_click();")
        print(str(start_value * multiplier) + " sent")
        multiplier += 1

    time.sleep(60)
    print("If you see this, that means we didn't send the right answer")


if __name__ == "__main__":
    main()
