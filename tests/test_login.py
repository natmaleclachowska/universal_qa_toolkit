'''
TESTY FORMULARZA LOGOWANIA
'''

import pytest
from playwright.sync_api import expect
from config.settings import LOGIN2_URL, EMAIL2, PASSWORD2


def test_successful_login(page):
    page.goto(LOGIN2_URL)

    # Test 1. Poprawne zalogowanie
    page.locator("//input[@id='username']").fill(EMAIL2)
    page.locator("//input[@id='password']").fill(PASSWORD2)
    page.locator("//button[@name='login']").click()
    expect(page.locator("//h1[@class='entry-title']")).to_be_visible()
    print("Test 1: Poprawne zalogowanie się.")

def test_failed_login_invalid_email(page):
    page.goto(LOGIN2_URL)

    #Test 2. Niepoprawne logowanie (błędny adres e-mail)
    page.locator("//input[@id='username']").fill("nat.malecttttt@gmail.com")
    page.locator("//input[@id='password']").fill(PASSWORD2)
    page.locator("//button[@name='login']").click()
    expect(page.locator("//ul[@role='alert']")).to_be_visible()
    print("Test 2: Logowanie nie jest możliwe (błędny adres e-mail).")

def test_failed_login_invalid_password(page):
    page.goto(LOGIN2_URL)

    # Test 2. Niepoprawne logowanie (błędne hasło)
    page.locator("//input[@id='username']").fill(EMAIL2)
    page.locator("//input[@id='password']").fill("TajneHaslo1234!")
    page.locator("//button[@name='login']").click()
    expect(page.locator("//ul[@role='alert']")).to_be_visible()
    print("Test 2: Logowanie nie jest możliwe (błędne hasło).")
