import json
import requests
# SZABLON_URL = 'http://api.nbp.pl/api/exchangerates/rates/c/{}/2016-04-04/?format=json'
# waluta = input('Podaj walutę: ')
# r = requests.get(SZABLON_URL.format(waluta))
# # j_s = r.text
# # j = json.loads(j_s)
# # print(r.status_code)
# r.raise_for_status()
# j = r.json()
# print(j['rates'][0]['bid'])
# requests.get('http://api.nbp.pl/api/exchangerates/rates/c/usd/2016-04-04/?format=json').json()['rates'][0]['bid']
#

#używamy antualnej ceny średniej z API NBP

def policz_koszyk(k):


    if __name__ == '__main__':


        SZABLON_URL = 'http://api.nbp.pl/api/exchangerates/rates/c/{}/2016-04-04/?format=json'

        usd = requests.get(SZABLON_URL.format('usd'))
        usd.raise_for_status()
        usd = usd.json()
        usd = (usd['rates'][0]['bid'])

        chf = requests.get(SZABLON_URL.format('chf'))
        chf.raise_for_status()
        chf = chf.json()
        chf = (chf['rates'][0]['bid'])

        eur = requests.get(SZABLON_URL.format('eur'))
        eur.raise_for_status()
        eur = eur.json()
        eur = (eur['rates'][0]['bid'])

        wartosc = k['usd']*usd + k["chf"]*chf + k["eur"]*eur
        return print((wartosc), 'zł')

k = {
            'usd': 34,
            'chf': 200,
            'eur': 555
        }
policz_koszyk(k)
        # print('Suma:', policz_koszyk(k))