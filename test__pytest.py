import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



@pytest.mark.skip
def test1():
    assert True

@pytest.mark.skip
def testChrome():
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')
    driver.maximize_window()
    assert 'https://www.python.org/' == driver.current_url
    assert 'Welcome to Python.org' == driver.title

def test_tp1():
    driver = webdriver.Chrome()
    driver.get('https://phptravels.com/')
    driver.maximize_window()
    driver.get_screenshot_as_file('phptravels.png')
    menu_pricing = driver.find_element(By.XPATH, "//header/div[1]/div/nav/a[2]")
    menu_pricing.click()
    assert 'https://phptravels.com/pricing' == driver.current_url
    assert 'Phptravels Plans & Pricing | One Time Payment' == driver.title
    menu_pricing = driver.find_element(By.XPATH, "//header/div[1]/div/nav/a[2]")
    assert menu_pricing.text == 'Pricing'
    menu_pricing.screenshot('pricing.png')

def test_tp2():
    driver = webdriver.Chrome()
    driver.get('https://phptravels.com/pricing')
    driver.maximize_window()
    texte_titre = driver.find_element(By.XPATH, "//h1")
    texte_explicatif = driver.find_element(By.XPATH, "//h1/../p")
    assert "Plans and Prices" == texte_titre.text
    assert "Flexible pricing" in texte_explicatif.text #solution du feignant
    assert texte_explicatif.is_displayed()
    assert texte_explicatif.location['y'] > texte_titre.location['y']

def test_tp3():
    driver = webdriver.Chrome()
    driver.get('https://phptravels.com/')
    menu_login = driver.find_element(By.XPATH, "//header/div[1]/div/div[2]/a[2]")
    menu_login.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    assert 'https://app.phptravels.com/login' == driver.current_url
    driver.switch_to.window(windows[0])
    menu_get_started = driver.find_element(By.XPATH, "//header/div[1]/div/div[2]/a[3]")
    menu_get_started.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    assert 'https://app.phptravels.com/signup' == driver.current_url
