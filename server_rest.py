import flask
import requests

app = flask.Flask('moja apka')


@app.route('/dodaj/<int:x>/<int:y>')
def dodaj(x, y):
    return {
        'wynik': x + y
    }

@app.route('/wycen/<waluta>/<int:kwota>')
def wycen(waluta, kwota):
    return {
        'wynik': kursy[waluta.lower()] * kwota
    }




if __name__ == '__main__':
    url = 'https://api.nbp.pl/api/exchangerates/tables/a/?format=json'
    r = requests.get(url)
    r.raise_for_status()
    j = r.json()
    kursy = {d['code'].lower(): d['mid'] for d in j[0]['rates']}
    app.run(debug=True)

# napisać serwis wyceniający kwoaty walutowe:
# /wycen/usd/1230