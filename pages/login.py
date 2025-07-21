# Importamos los localizadores por tipo (ID, XPATH, etc.)
from utils.config import Config
from selenium.webdriver.common.by import By

# Importamos el driver base para tipar correctamente
from selenium.webdriver.remote.webdriver import WebDriver

# Esperas explícitas para asegurar que los elementos estén presentes/interactuables
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: WebDriver):
        # Asignamos el WebDriver a un atributo de instancia
        self.driver = driver

        # Creamos un WebDriverWait reutilizable con timeout de 10 segundos
        self.wait = WebDriverWait(self.driver, 10)

        self.signButton_locator = (By.CLASS_NAME, "btn btn-primary")
        self.username_input_locator = (By.ID, "user_login")
        self.password_input_locator = (By.ID, "user_password")

    def load(self):
        self.driver.get(Config.LOGIN_URL)

    def login(self, username, password):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(self.username_input_locator)
        ).send_keys(username)
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(self.password_input_locator)
        ).send_keys(password)

    def clicSignIn(self):
        self.wait.until(EC.element_to_be_clickable(self.signButton_locator)).click()

"""

Hacer clic en un elemento
self.wait.until(EC.element_to_be_clickable(locator)).click()

Escribir texto en un input
self.wait.until(EC.visibility_of_element_located(locator)).send_keys("mi texto")

Obtener texto de un elemento
texto = self.wait.until(EC.visibility_of_element_located(locator)).text

Verificar visibilidad
es_visible = self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

Obtener atributo específico (por ejemplo, value)
valor = self.driver.find_element(*locator).get_attribute("value")

"""