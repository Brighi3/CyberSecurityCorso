from selenium import webdriver
from selenium.webdriver.common.by import By

# Inizializza il driver del browser (per esempio, Chrome)
driver = webdriver.Chrome()

# Apri la pagina web
url = ""
driver.get(url)

# Effettua il clic sul link con l'ID "pt-login"
login_link = driver.find_element(By.ID, "pt-login")
login_link.click()

# Trova l'elemento del campo di input utilizzando l'ID
input_field = driver.find_element(By.ID, "wpName1")

# Inserisci il testo desiderato nel campo di input utilizzando il metodo send_keys
input_field.send_keys("CristianoRonaldo")

# Attendi l'input dell'utente prima di chiudere il browser
input("Premi invio per chiudere il browser...")

# Chiudi il browser
driver.quit()