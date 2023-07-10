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

# Puoi eseguire ulteriori azioni dopo il clic, come compilare campi di input o attendere il caricamento di una nuova pagina

# Attendi l'input dell'utente prima di chiudere il browser
input("Premi invio per chiudere il browser...")

# Chiudi il browser
driver.quit()