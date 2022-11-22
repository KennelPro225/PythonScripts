prix_mineur = 7
prix_majeur = 12
prix_pop = 5

print("Bonjour, Bienvenue à notre service de vente de billet de cinema!")

print("\nQuel âge avez-vous?")
age_client = int(input())
print('\nVoulez-vous du Pop Corn?\t1-OUI 0-NON')
answer = int(input())


if age_client < 18 and answer == 1:
    print("Le prix total est {}£".format(prix_mineur+prix_pop))

elif age_client < 18 and answer == 0:
    print("Le prix total est {}£".format(prix_mineur))


elif age_client >= 18 and answer == 1:
    print("Le prix total est {}£".format(prix_majeur+prix_pop))



else:
    print("Le prix total est {}£".format(prix_majeur))