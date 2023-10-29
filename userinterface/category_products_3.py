from screenpy_selenium import Target
from selenium.webdriver.common.by import By

class CategoryProducts3():

    men_tshirt = Target.the("men Tshirt").located_by((By.XPATH,"//body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/div[2]/div[1]/div[1]/div[1]/a[1]"))
    view_cart = Target.the("view cart").located_by((By.XPATH,"//u[normalize-space()='View Cart']"))

