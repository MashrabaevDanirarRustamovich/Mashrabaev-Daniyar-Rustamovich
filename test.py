import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()

    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver

    driver.quit()


def test_show__my_pets(driver):
    driver.find_element(By.ID, 'email').send_keys('mashrabaev89@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Daniyar')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

def test_show_my_pets2(driver):
    driver.find_element(By.ID, 'email').send_keys('mashrabaev89@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('Daniyar')
    driver.implicitly_wait(10)
    visible_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    driver.find_element(*visible_button).click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'