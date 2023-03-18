from db.db import songs_dict

print("\nHey, welcome to Find Song Lyrics!")

chosen = 0

while chosen != -1:
    try:
        chosen = int(input(
            "\nChoose a song:\n1.    Yellow by Coldplay.\n2.    Memories by Maroon 5.\n3.    As it was by Harry Styles.\n4.    Do I wanna know? by Artic Monkeys.\n5.    Dueles by Jesse & Joy.\n6.    Unstoppable by Sia.\n7.    Photograph by Ed Sheeran.\n8.    No me doy por vencido by Luis Fonsi.\n9.    Por las noches by Peso Pluma.\n10.   Eyes open by Taylow Swift.\n[-1 to exit]\n\nElection: "))
        if chosen >= 1 and chosen <= 10:
            print("\n" + songs_dict[chosen])

    except ValueError:
        print("That's not an option! Try again: ")

print("Thanks for try me, see on!")
