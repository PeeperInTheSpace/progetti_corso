def saluta():
    print("--- Benvenuti nel Calcolatore Collaborativo del Corso ---")

def somma(a, b):
    return a + b

if __name__ == "__main__":
    saluta()
    risultato = somma(5, 3)
    print(f"Risultato della somma (5 + 3): {risultato}")

#Test pull request - Failed
#Test pull request 2 - Failed
#Test pull request 3 - Failed
#Test pull request 4

#codice alessia
firstname = 'Mario' input('Inserisci il tuo nome: ').strip() 
lastname = 'Rossi' input('Inserisci il tuo cognome: ').strip() 
city = 'Roma' input('Inserisci la tua città: ').strip() 
age = 20 int(input('Inserisci la tua età: ').strip()) 
 
if(len(firstname) >= 3 and len(lastname) >= 3 and len(city) >= 0): 
    if(age >= 0 and age <= 120): 
        if(city in ['Milano', 'Roma', 'Napoli']): 
            str = '{} {} ({}) anni {} - {}' 
            if(age < 18): 
                print(str.format(firstname, lastname, city, age, 'minorenne')) 
            else: 
                print(str.format(firstname, lastname, city, age, 'maggiorenne')) 
        else: 
            print("Città non compresa tra ['Milano', 'Roma', 'Napoli']!!") 
    else: 
        print("Valore età errato!!") 
else: 
    print("Valori inseriti Errati!!!") 
print('----------------------------------------------')
