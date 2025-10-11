
    
#funkcija za učitavanje teksta iz datoteke
def ucitaj_tekst(filepath):
    try:
        #Ovdje ide logika za čitanje datoteke
        with open(filepath,'r',encoding='utf-8') as file:
            sadrzaj = file.read()
        return sadrzaj
    except FileNotFoundError:
        print(f'Datoteka{filepath}nije pronađena.')
        return None


#Funkcija za pročiščavanje teksta
def ocisti_tekst(tekst):
    tekst = tekst.lower()
    interpunkcija = ['.',',','!','?',';',':','"',"'",'(',')','[',']','{','}','-','_','/','\\']
    for znak in interpunkcija:
        tekst = tekst.replace(znak,'')

    lista_rijeci = tekst.split()
    return lista_rijeci
def broji_rijeci(lista_rijeci):
    brojac_rijeci = {}
    for rijec in lista_rijeci:
        if rijec in brojac_rijeci:
            brojac_rijeci[rijec] += 1
        else:
            brojac_rijeci[rijec] = 1
    return brojac_rijeci

if __name__ == "__main__":
    filepath = "tekst.txt"
    print(f"Učitavam tekst iz datoteke: {filepath}")
    ucitani_tekst = ucitaj_tekst(filepath)
    if ucitani_tekst:
        print("Učitani tekst je:")
        print(ucitani_tekst)
    else:
        print("Greška pri učitavanju datoteke")
    ucitani_tekst = ocisti_tekst(ucitani_tekst)
    if ucitani_tekst:
        print("Očišćeni tekst je:")
        print(ucitani_tekst)
        brojac_rijeci = broji_rijeci(ucitani_tekst)
        print("Broj riječi u tekstu:")
        print(brojac_rijeci)
    else:
        print("Greška pri očiščavanju teksta.")

STOP_WORDS = ['i', 'u', 'na', 'je', 'se', 'su', 's', 'za', 'o', 'a', 'pa', 'te', 'li', 'da']
def ukloni_stop_words(lista_rijeci, brojac_rijeci):
    
    novi_rjecnik = {}
    stop_words_lista = {}
    for rijec in lista_rijeci:
        if rijec in STOP_WORDS:
            stop_words_lista[rijec] 
        else:
            novi_rjecnik[rijec] 
        

def sortiraj_i_ispisi(rjecnik_frekvencija):
    novi_rjecnik = sorted(rjecnik_frekvencija.items(), key=lambda x: x[1], reverse=True)
    print("Riječi sortirane po frekvenciji:")
    for rijec, frekvencija in novi_rjecnik[:15]:
        print('Top 15 najčešćih riječi'f"{rijec}: {frekvencija}")
def main():
    filepath = "tekst.txt"
    novi_rjecnik = {}
    stop_words_lista = {}
    print("Učitavam tekst iz datoteke: {filepath}")

    
if __name__ == "__main__":
    filepath = "tekst.txt"
    print("Ovo je lista stop riječi:{stop_words_lista}")
    print("Ovo je novi rječnik bez stop riječi:{novi_rjecnik}")