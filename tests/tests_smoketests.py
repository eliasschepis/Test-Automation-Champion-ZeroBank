# Importamos los localizadores por tipo (ID, XPATH, etc.)
from selenium.webdriver.common.by import By

# Importamos el driver base para tipar correctamente
from selenium.webdriver.remote.webdriver import WebDriver

# Esperas explícitas para asegurar que los elementos estén presentes/interactuables
from utils.config import Config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.index import IndexPage
from pages.login import LoginPage
from utils.flows import login_and_go_to_home


def test_index_url(driver):
    page = IndexPage(driver)
    page.load()

    assert "index" in driver.current_url

    page.clicSignIn()

    login_page = LoginPage(driver)
    login_page.login(Config.USERNAME, Config.PASSWORD)

def test_login_url(driver):
    page = login_and_go_to_home(driver)
    page.load()
    assert "index" in driver.current_url
