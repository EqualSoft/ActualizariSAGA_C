import requests
from datetime import datetime

def check_new_version():
    """
    Verifică dacă există o versiune nouă de SAGA C și afișează un mesaj dacă este disponibilă.
    """
    # Obțineți versiunea actuală a SAGA C
    current_version = "3.0.569" # Inlocuiti cu versiunea actuala instalata

    # Obțineți ultima versiune de pe site-ul SAGA
    url = "https://www.sagasoft.ro/actualizari.php?program=SAGA%20C&pagina=1"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        latest_version = html.split("Versiune: ")[1].split(" ")[0]
    else:
        print("Eroare la obținerea versiunii de pe site-ul SAGA")
        return

    # Comparați versiunile
    if latest_version != current_version:
        print(f"O nouă versiune de SAGA C este disponibilă: {latest_version}")
        print(f"Versiunea actuală instalată: {current_version}")
        print("Vă rugăm să descărcați și să instalați noua versiune de pe site-ul SAGA:")
        print("https://www.sagasoft.ro/saga-c.php")
    else:
        print("Nu există o versiune nouă de SAGA C disponibilă.")

# Setați intervalul de timp pentru verificare
interval = 60 * 60 * 24 # 24 de ore

while True:
    check_new_version()
    time.sleep(interval)
