from screenpy_selenium import Target
from selenium.webdriver.common.by import By

class HomePage():

    section_men = Target.the("section men").located_by((By.XPATH,"//a[normalize-space()='Men']"))
    section_tshirts = Target.the("section Tshirts").located_by((By.XPATH,"//a[normalize-space()='Tshirts']"))

