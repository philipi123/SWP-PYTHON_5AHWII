import unittest
import random
from collections import Counter

# definiere die möglichen farben und werte für ein kartenspiel
farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

# erstelle ein komplettes deck aus allen kombinationen von farben und symbolen
karten = [(farbe, symbol) for farbe in farben for symbol in symbole]

# eine funktion, die fünf zufällige karten aus dem deck zieht
def ziehe_karten():
    return random.sample(karten, 5) 

# prüft, ob die hand ein royal flush ist, also zehn, bube, dame, könig und ass in derselben farbe
def ist_royal_flush(hand):
    farben = [karte[0] for karte in hand]
    symbole = set(karte[1] for karte in hand)
    return farben.count(farben[0]) == 5 and symbole == {'10', 'Bube', 'Dame', 'König', 'Ass'}

# prüft, ob die hand ein straight flush ist, also fünf aufeinanderfolgende karten in derselben farbe
def ist_straight_flush(hand):
    farbe = hand[0][0]  # betrachte die farbe der ersten karte
    symbole = set(karte[1] for karte in hand)
    if farben.count(farbe) == 5:
        symbole_werte = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Bube': 11, 'Dame': 12, 'König': 13, 'Ass': 14}
        symbole_wertliste = [symbole_werte[s] for s in symbole]
        symbole_wertliste.sort()
        return symbole_wertliste[-1] - symbole_wertliste[0] == 4
    return False

# prüft, ob die hand vier karten desselben wertes hat
def ist_four_of_a_kind(hand):
    symbole = [karte[1] for karte in hand]
    counts = Counter(symbole)
    return 4 in counts.values()

# prüft, ob die hand einen drilling und ein paar hat, also ein full house
def ist_full_house(hand):
    symbole = [karte[1] for karte in hand]
    counts = Counter(symbole)
    return 3 in counts.values() and 2 in counts.values()

# prüft, ob alle karten die gleiche farbe haben, also ein flush
def ist_flush(hand):
    farben = [karte[0] for karte in hand]
    return farben.count(farben[0]) == 5

# prüft, ob die hand fünf aufeinanderfolgende werte hat, also ein straight
def ist_straight(hand):
    symbole_werte = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Bube': 11, 'Dame': 12, 'König': 13, 'Ass': 14}
    symbole = set(karte[1] for karte in hand)
    symbole_wertliste = [symbole_werte[s] for s in symbole]
    symbole_wertliste.sort()
    return symbole_wertliste[-1] - symbole_wertliste[0] == 4 and len(symbole) == 5

# prüft, ob die hand drei karten desselben wertes hat, also ein drilling
def ist_three_of_a_kind(hand):
    symbole = [karte[1] for karte in hand]
    counts = Counter(symbole)
    return 3 in counts.values()

# prüft, ob die hand zwei verschiedene paare hat
def ist_two_pair(hand):
    symbole = [karte[1] for karte in hand]
    counts = Counter(symbole)
    return list(counts.values()).count(2) == 2

# prüft, ob die hand ein paar hat
def ist_one_pair(hand):
    symbole = [karte[1] for karte in hand]
    counts = Counter(symbole)
    return 2 in counts.values()

# prüft, ob keine der anderen hände zutrifft und die höchste karte zählt
def ist_high_card(hand):
    return len(set(karte[1] for karte in hand)) == 5

# die hauptfunktion des programms, die die simulation durchführt
def main():
    anzahl_simulationen = 100000
    ergebnisse = {
        'Royal Flush': 0, 'Straight Flush': 0, 'Four of a Kind': 0, 'Full House': 0,
        'Flush': 0, 'Straight': 0, 'Three of a Kind': 0, 'Two Pair': 0,
        'One Pair': 0, 'High Card': 0
    }

    # führe die simulation mehrere male aus
    for _ in range(anzahl_simulationen):
        hand = ziehe_karten()
        # überprüfe für jede hand, welche kombination vorliegt und aktualisiere die zählung
        if ist_royal_flush(hand):
            ergebnisse['Royal Flush'] += 1
        elif ist_straight_flush(hand):
            ergebnisse['Straight Flush'] += 1
        elif ist_four_of_a_kind(hand):
            ergebnisse['Four of a Kind'] += 1
        elif ist_full_house(hand):
            ergebnisse['Full House'] += 1
        elif ist_flush(hand):
            ergebnisse['Flush'] += 1
        elif ist_straight(hand):
            ergebnisse['Straight'] += 1
        elif ist_three_of_a_kind(hand):
            ergebnisse['Three of a Kind'] += 1
        elif ist_two_pair(hand):
            ergebnisse['Two Pair'] += 1
        elif ist_one_pair(hand):
            ergebnisse['One Pair'] += 1
        else:
            ergebnisse['High Card'] += 1

    # gebe die ergebnisse und deren prozentuale anteile aus
    for kombination, anzahl in ergebnisse.items():
        prozentualer_anteil = (anzahl / anzahl_simulationen) * 100
        print(f'{kombination}: {anzahl} ({prozentualer_anteil:.2f}%)')

    # gebe die tatsächlichen wahrscheinlichkeiten aus und vergleiche sie mit den simulationsergebnissen
    tatsächliche_wahrscheinlichkeiten = {
        'Royal Flush': 0.000154, 'Straight Flush': 0.00139, 'Four of a Kind': 0.0240,
        'Full House': 0.1441, 'Flush': 0.197, 'Straight': 0.3925, 'Three of a Kind': 2.1128,
        'Two Pair': 4.7539, 'One Pair': 42.2569, 'High Card': 50.1177
    }

    for kombination, wahrscheinlichkeit in tatsächliche_wahrscheinlichkeiten.items():
        print(f'Wahrscheinlichkeit {kombination}: {wahrscheinlichkeit * 100:.5f}%')

# wenn das programm gestartet wird, führe die main-funktion aus
if __name__ == '__main__':
    #main()
    unittest.main()


class TestPokerHands(unittest.TestCase):

    def setUp(self):
        self.hand_royal_flush = [('Herz', '10'), ('Herz', 'Bube'), ('Herz', 'Dame'), ('Herz', 'König'), ('Herz', 'Ass')]
#Royal Flush testen
#     
    def test_royal_flush(self):
        self.assertTrue(ist_royal_flush(self.hand_royal_flush))

    def test_straight_flush(self):
        # Hand erstellen die Straight FLush ist
     #self.assertTrue(ist_straight_flush(hand_straight_flush))
        
        pass #platzhalter


   


