from screenpy_selenium import Target
from selenium.webdriver.common.by import By

class PaymentDone():

    order_confirmed_text = Target.the("order confirmed text").located_by((By.XPATH,"//p[normalize-space()='Congratulations! Your order has been confirmed!']"))
    
    
