#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

print("Que voulez-vous?")
print("Pour la liste des cryptos disponible tapez: Liste des cryptos. Pour le prix d'une crypto tapez son nom (choisissez dans la liste!). ")

choix = input("Entrez votre choix: ")

print("Vous avez choisi:", choix)



import requests
requete = requests.get("https://www.cryptocompare.com/api/data/coinlist/")
page=requete.json()
page=page["Data"]

if(choix == 'Liste des cryptos'):
	for n in page:
		print(n)
elif (choix == 'quit'):
	print ('exit')

else :
	requete = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+choix+"&tsyms=BTC,USD,EUR")
	valeurs= requete.json()
	print(valeurs)