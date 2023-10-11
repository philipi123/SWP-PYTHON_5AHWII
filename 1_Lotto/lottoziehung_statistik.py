import random

def lotto_ziehung():
    #6 zahlen zwischen 1 und 45 ziehen
    alle_zahlen = list(range(1, 46))
    gezogene_zahlen =  random.sample(alle_zahlen, 6)
    return gezogene_zahlen

def lotto_statistik(gezogene_zahlen, statistik):
    for zahl in gezogene_zahlen:
        statistik[zahl] += 1
    return statistik

def main():
    #statistik dictionary
    statistik_dict = {i: 0 for i in range(1, 46)}

    #1000 ziehungen durchführen und statistik aktualisieren
    for _ in range(1000):
        gezogene_zahlen = lotto_ziehung()
        statistik_dict = lotto_statistik(gezogene_zahlen, statistik_dict)
    
    #statistik ausgeben
    print("Statistik nach 1000 Ziehungen:")
    for nummer, haeufigkeit in statistik_dict.items():
        print(f"Zahl {nummer}: {haeufigkeit} Mal gezogen")

if __name__ == "__main__":
    main()
