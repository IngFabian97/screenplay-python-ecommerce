from screenpy_selenium import Target
from selenium.webdriver.common.by import By

class Payment():

    name_card_input = Target.the("name on card input").located_by((By.NAME,"name_on_card"))
    card_number_input = Target.the("card number input").located_by((By.NAME,"card_number"))
    cvc_input = Target.the("CVC input").located_by((By.NAME,"cvc"))
    expiration_month_input = Target.the("expiration month input").located_by((By.NAME,"expiry_month"))
    expirtation_year_input = Target.the("expiration year input").located_by((By.NAME,"expiry_year"))
    confirmer_order_button = Target.the("pay and confirm order button").located_by((By.XPATH,"//button[@id='submit']"))
    

