from pages.index import IndexPage
from pages.login import LoginPage
from utils.config import Config
import time

# Login e ir al Home

def login_and_go_to_home(driver):
    index_page = IndexPage(driver)
    index_page.load()
    index_page.clicSignIn()
    login_page = LoginPage(driver)
    login_page.login(Config.USERNAME, Config.PASSWORD)
    time.sleep(2)
    return IndexPage(driver)