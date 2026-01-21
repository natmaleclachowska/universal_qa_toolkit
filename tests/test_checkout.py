import pytest
from playwright.sync_api import expect
from config.settings import BASE2_URL, ORDER2_URL, EMAIL2

def test_complete_order_happy_path(page):
    page.goto(BASE2_URL)
    page.locator(".add_to_cart_button").first.click()
    page.wait_for_timeout(2000)
    page.goto(ORDER2_URL)

    #Test 1. Zamówienie produktu
    page.locator("//input[@id='billing_email']").fill(EMAIL2)
    page.locator("//input[@id='billing_first_name']").fill("Natalia")
    page.locator("//input[@id='billing_last_name']").fill("Kowalska")
    page.locator("//input[@id='billing_company']").fill("TestAuto")
    page.locator("//input[@id='billing_address_1']").fill("ul. Przemysłowa 1")
    page.locator("//input[@id='billing_postcode']").fill("90-123")
    page.locator("//input[@id='billing_city']").fill("Szczecin")
    page.locator("//input[@id='billing_phone']").fill("123456789")
    page.locator("//label[@for='payment_method_stripe']").click()
    page.locator("//input[@id='Field-numberInput']").fill("4242424242424242")
    page.locator("//input[@id='Field-expiryInput']").fill("0226")
    page.locator("//input[@id='Field-cvcInput']").fill("111")
    page.locator("//input[@id='wc-stripe-blik-code']").fill("111111")
    page.locator("//input[@id='terms']").check()
    page.locator("//button[@id='place_order']").click()
    expect(page.locator("//h1[@class='entry-title']")).to_contain_text("Zamówienie otrzymane")
    print("Test 1: Poprawne zamówienie produktu.")