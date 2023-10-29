import pytest
from screenpy import AnActor, ReadExactly, See, given, when, then
from screenpy_selenium import BrowseTheWeb, Click, Enter, Text, Wait
from userinterface.login_page import LoginPage
from userinterface.home_page import HomePage
from userinterface.category_products_3 import CategoryProducts3
from userinterface.view_cart import ViewCart
from userinterface.checkout import Checkout
from userinterface.payment import Payment
from userinterface.payment_done import PaymentDone


@pytest.mark.usefixture("driver")
def test_login(driver):
    actor = AnActor.named("Fabian").who_can(BrowseTheWeb.using(driver))

    given(actor).was_able_to(LoginPage().open())
    when(actor).attempts_to(
        Wait.for_the(LoginPage().username_field).to_appear(),
        Enter.the_text("ing.pruebas@hotmail.com").into_the(LoginPage().username_field),
        Enter.the_text("7890").into_the(LoginPage().password_field),
        Click.on_the(LoginPage().submit_button),
        Wait.for_the(HomePage().section_men).to_appear(),
        Click.on_the(HomePage().section_men),
        Wait.for_the(HomePage().section_tshirts).to_appear(),
        Click.on_the(HomePage().section_tshirts),
        Wait.for_the(CategoryProducts3().men_tshirt).to_appear(),
        Click.on_the(CategoryProducts3().men_tshirt),
        Wait.for_the(CategoryProducts3().view_cart).to_appear(),
        Click.on_the(CategoryProducts3().view_cart),
        Wait.for_the(ViewCart().procced_checkout_button).to_appear(),
        Click.on_the(ViewCart().procced_checkout_button),
        Wait.for_the(Checkout().place_order_button).to_appear(),
        Click.on_the(Checkout().place_order_button),
        Wait.for_the(Payment().confirmer_order_button).to_appear(),
        Enter.the_text("Fabian").into_the(Payment().name_card_input),
        Enter.the_text("1234567891").into_the(Payment().card_number_input),
        Enter.the_text("123").into_the(Payment().cvc_input),
        Enter.the_text("12").into_the(Payment().expiration_month_input),
        Enter.the_text("2026").into_the(Payment().expirtation_year_input),
        Click.on_the(Payment().confirmer_order_button),
        Wait.for_the(PaymentDone().order_confirmed_text).to_appear()
        
    )
    then(actor).should(See.the(Text.of_the(PaymentDone().order_confirmed_text), ReadExactly("Congratulations! Your order has been confirmed!")))