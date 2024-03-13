import random
import json
import os

# Zeigt die verfügbaren Spieloptionen an.
def print_options():
    print("\nStein, Papier, Schere, Echse, Spock:")  

# Ermöglicht dem Spieler, seine Wahl einzugeben.
def player_input():
    return input("Geben Sie Ihre Wahl ein: ")  

# Computer wählt zufällig eine der Optionen.
def computer_input():
    return random.choice(["Stein", "Papier", "Schere", "Echse", "Spock"])  

# Aktualisiert die Spielstatistiken nach jedem Spiel.
def update_statistics(stats, result):
    stats["Gesamtspiele"] += 1
    if result == "Sie gewinnen!":
        stats["Spieler gewinnt"] += 1
    elif result == "Computer gewinnt!":
        stats["Computer gewinnt"] += 1
    else:
        stats["Unentschieden"] += 1
    return stats

# Speichert die Spielstatistiken in einer Datei.
def save_statistics(stats):
    with open("spiel_statistik.json", "w") as file:
        json.dump(stats, file)

# Lädt die Spielstatistiken aus einer Datei.
def load_statistics():
    if os.path.exists("spiel_statistik.json"):
        with open("spiel_statistik.json", "r") as file:
            return json.load(file)
    return {"Gesamtspiele": 0, "Spieler gewinnt": 0, "Computer gewinnt": 0, "Unentschieden": 0}

# Überprüft, wer das Spiel gewonnen hat.
def check_win(player, computer):
    if player == computer:
        return "Unentschieden!"

    # Regeln, die bestimmen, welches Symbol was schlägt.
    win_conditions = {
        "Stein": ["Schere", "Echse"],
        "Papier": ["Stein", "Spock"],
        "Schere": ["Papier", "Echse"],
        "Echse": ["Spock", "Papier"],
        "Spock": ["Schere", "Stein"]
    }

    if computer in win_conditions[player]:
        return "Computer gewinnt!"
    else:
        return "Sie gewinnen!"

# Zeigt die aktuellen Spielstatistiken an.
def print_statistics(stats):
    print("\nSpielstatistiken:")
    for key, value in stats.items():
        print(f"{key}: {value}")



# Main
def main():
    stats = load_statistics()
    while True:
        print("\n1. Spielen\n2. Statistik anzeigen\n3. Beenden")
        choice = input("Wählen Sie eine Option: ")
        if choice == "1":
            print_options()
            player = player_input()
            computer = computer_input()
            result = check_win(player, computer)
            print(f"Sie: {player}, Computer: {computer}")
            print(result)
            stats = update_statistics(stats, result)
            save_statistics(stats)
        elif choice == "2":
            print_statistics(stats)
        elif choice == "3":
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie 1, 2 oder 3.")

if __name__ == "__main__":
    main()  
