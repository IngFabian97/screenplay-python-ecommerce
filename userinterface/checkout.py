from screenpy_selenium import Target
from selenium.webdriver.common.by import By

class Checkout():

    place_order_button = Target.the("place order button").located_by((By.XPATH,"//a[normalize-space()='Place Order']"))

