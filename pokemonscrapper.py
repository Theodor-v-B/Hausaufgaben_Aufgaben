import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule # Now this import should work
import time
# Funktion zum Überprüfen des Bestands


URL_Liste = [
["https://www.cardsparadise.com/PPokemon-Scarlet-Violet-SV-85-Prismatic-Evolucion-1-Case-mit-allen-8-verschiedenen-Mini-TIN-Englisch",
    "#buttons-container",
    ""],

["https://www.karten-piraten.com/product/pokemon-prismatic-evolutions-mini-tin-display/",
    ".single_add_to_cart_button button",
    ""],

["https://www.cardbuddys.de/home/produkte/vorbestellungen/15655/vorbestellung-scarlet-and-violet-prismatic-evolutions-mini-tin-display-8-tins-en",
    "#AddToCartForm_AddToCartForm_productQuantity",
    ""],

["https://games-island.eu/Pokemon-TCG-Scarlet-Violet-85-Prismatic-Evolutions-Mini-Tin-Display-8-Tins-Englisch",
    "#quantity-grp",
    ""],

["https://stunning-cards.de/products/prismatic-evolutions-mini-tin-display-en",
    "#ProductSubmitButton-template--23151292678473__main",
    "In den Warenkorb legen"],

["https://www.nomeko-store.de/products/pokemon-sammelkartenspiel-8er-mini-tin-display-prismatische-entwicklungen-englisch-release-7-02-2025",
    "#ProductSubmitButton-template--22566784893256__main" ,
    "In den Warenkorb legen"],

["https://www.play-maniac.de/products/pok-mon-prismatic-evolutions-mini-tin-display-8-englisch",
    "#quantity",
    ""]
]

def URL_Check(Eine_URL):
    #Eine_URL = [URL, id_oder_cls, Elementtext]
    try:
        response = requests.get(Eine_URL[0])
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Beispiel: Verfügbarkeit in einem div mit der Klasse 'availability' überprüfen
        stock_info = soup.select(Eine_URL[1])
        #if len(stock_info) > 0: print(stock_info[0].text)
        if len(stock_info) == 0:        #Button nicht da (muss aber da sein)
            return False
        elif Eine_URL[2] == "":         #Button ist da, und Inhalt egal (muss nur da sein)
            return True
        elif stock_info[0].text.find(Eine_URL[2]) == -1: #Button ist da, aber falscher Text
            return False
        else:                           #Button hat richtigen Text
            return True
        
    except requests.exceptions.ConnectTimeout:
        print("Wir wurden blockiert von " + Eine_URL[0])

    except Exception as error:
        print(error.with_traceback)

    finally:
        return False


# for (i,Eine_URL) in enumerate(URL_Liste):
#     if i > 0:
#         print(Eine_URL[0])
#         print(URL_Check(Eine_URL))
print(URL_Check(URL_Liste[0]))

# Funktion zum Senden von E-Mails
def Email_senden(subject, body, to_email):
    try:
        from_email = "techstarter@web.de"
        password = "Techstarter2025"
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.web.de', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("E-Mail versendet")
    except:
        print("E-mail konnte nicht gesendet werden!")

# Funktion für den Job, der alle 30 Minuten prüft
def job(Eine_URL):
    if URL_Check(Eine_URL):
        Email_senden("Produkt wieder vorrätig", Eine_URL[0], "nvh22@web.de")
    else:
        print("Produkt nicht auf", Eine_URL[0])

# Alle 30 Minuten ausführen

for Eine_URL in URL_Liste:
    schedule.every(5).minutes.do(job(Eine_URL))

while True:
    schedule.run_pending()  #Alle Jobs ausführen, die im Scheduler sind, aber nicht gestartet
    time.sleep(10)
