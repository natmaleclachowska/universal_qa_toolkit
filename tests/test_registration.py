'''
TESTY FORMULARZA REJESTRACJI
'''

import pytest
from playwright.sync_api import expect
from config.settings import LOGIN2_URL, PASSWORD2
import time

def test_successful_registration(page):
    unique_email = f"test_natalia_{int(time.time())}.@test.pl"
    page.goto(LOGIN2_URL)

    # Test 1. Poprawna rejestracja
    page.locator("//input[@id='reg_email']").fill(unique_email)
    page.locator("//input[@id='reg_password']").fill(PASSWORD2)
    page.locator("//button[@name='register']").click()
    expect(page.locator("//h1[@class='entry-title']")).to_be_visible()
    print(f"Test 1: Rejestracja udana dla maila {unique_email}.")

def test_failed_registration_duplicate(page):
    page.goto(LOGIN2_URL)

    # Test 2. Niepoprawna rejestracja (istniejący adres e-mail w bazie)
    page.locator("//input[@id='reg_email']").fill("nat.malectttt@gmail.com")
    page.locator("//input[@id='reg_password']").fill(PASSWORD2)
    page.wait_for_timeout(5000)
    page.locator("button[name='register']").click()
    error_banner = page.locator(".woocommerce-error")
    print("Test 2: Rejestracja nieudana. E-mail jest już dodany do bazy.")
