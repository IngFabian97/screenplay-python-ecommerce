from screenpy_selenium import Target
from selenium.webdriver.common.by import By

class ViewCart():

     procced_checkout_button = Target.the("procced checkout button").located_by((By.XPATH,"//a[normalize-space()='Proceed To Checkout']"))
   

