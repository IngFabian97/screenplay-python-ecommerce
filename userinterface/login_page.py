from screenpy_selenium import Open, Target
from selenium.webdriver.common.by import By

class LoginPage():
    url = "https://automationexercise.com/login"

    username_field = Target.the("username field").located_by((By.NAME, "email"))
    password_field = Target.the("password field").located_by((By.NAME, "password"))
    submit_button = Target.the("submit button").located_by((By.XPATH, "//button[normalize-space()='Login']"))

    def open(self):
        return Open(self.url)
