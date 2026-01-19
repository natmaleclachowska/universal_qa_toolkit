'''
TESTY EDYCJI KOSZYKA
'''
from operator import contains

import pytest
from playwright.sync_api import expect
from config.settings import BASE2_URL

def test_edit_cart_quantity(page):
    page.goto(BASE2_URL)

    # Test 1. Aktualizacja ilości produktów w koszyku
    page.locator(".add_to_cart_button").first.click()
    page.wait_for_timeout(2000)
    page.goto("https://fakestore.testelka.pl/koszyk/")
    quantity_input = page.locator("//input[contains(@id, 'quantity')]")
    quantity_input.fill("2")
    page.locator("button[name='update_cart']").click()
    expect(page.locator(".woocommerce-message")).to_contain_text("Koszyk zaktualizowany")
    total_price = page.locator(".order-total .amount")
    expect(total_price).to_contain_text("6 000,00 zł")
    print("Test 1: Aktualizacja ilości produktów w koszyku działa poprawnie")



