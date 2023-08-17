from flask import Flask, render_template
import redis
import json

# Créer un objet d'application Flask nommé "application_suivie"
application_suivi_performance = Flask(__name__, static_folder='templates/images')

# Se connecter à Redis
r = redis.Redis(host='localhost', port=6379, db=2)

@application_suivi_performance.route('/')
def index():
    # Récupérer les données de revenus annuels
    revenus_annuels = r.hgetall('annual_income')
    dates = []
    revenus = []
    for annee, montant in revenus_annuels.items():
        dates.append(annee.decode())
        revenus.append(float(montant.decode()))
    #faire un sort par date(année)
    dates, revenus = zip(*sorted(zip(dates, revenus)))
    dates_json = json.dumps(dates)
    revenus_json = json.dumps(revenus)
    return render_template('index.html', dates_json=dates_json, revenus_json=revenus_json)

if __name__ == '__main__':
    application_suivi_performance.run()
