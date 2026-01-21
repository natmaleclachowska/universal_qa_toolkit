'''
TESTY EDYCJI KOSZYKA
'''

import pytest
from playwright.sync_api import expect
from config.settings import BASE2_URL, BASKET2_URL


def test_edit_cart_quantity(page):
    page.goto(BASE2_URL)

    # Test 1. Aktualizacja ilości produktów w koszyku
    page.locator(".add_to_cart_button").first.click()
    page.wait_for_timeout(2000)
    page.goto(BASKET2_URL)
    quantity_input = page.locator("//input[contains(@id, 'quantity')]")
    quantity_input.fill("2")
    page.locator("button[name='update_cart']").click()
    expect(page.locator(".woocommerce-message")).to_contain_text("Koszyk zaktualizowany")
    total_price = page.locator(".order-total strong .woocommerce-Price-amount")
    expect(total_price).to_contain_text("6 000,00 ")
    #expect(page.locator("//td[@data-title='Kwota']))
    print("Test 1: Aktualizacja ilości produktów w koszyku działa poprawnie")

def test_remove_product_from_cart(page):
    page.goto(BASE2_URL)

    # Test 2. Usunięcie produktu z koszyka
    page.locator(".add_to_cart_button").first.click()
    page.wait_for_timeout(2000)
    page.goto(BASKET2_URL)
    page.locator(".remove").first.click()
    expect(page.locator(".cart-empty")).to_be_visible()
    print("Test 2: Usuwanie produktu z koszyka działa poprawnie")



