def kviz():
    bodovi = 0

    
    print("1. Koji je glavni grad Francuske?")
    odgovor1 = input("a) Madrid\nb) Pariz\nc) Berlin\nd) Rim\nOdgovor: ")
    if odgovor1.lower() == 'b':
        bodovi += 1

    
    print("\n2. Koji je najduži rijeka na svijetu?")
    odgovor2 = input("a) Nil\nb) Amazon\nc) Mississippi\nd) Yangtze\nOdgovor: ")
    if odgovor2.lower() == 'b':
        bodovi += 1

    
    print("\n3. Koje godine je počeo Drugi svjetski rat?")
    odgovor3 = input("a) 1914\nb) 1939\nc) 1941\nd) 1945\nOdgovor: ")
    if odgovor3.lower() == 'b':
        bodovi += 1

    
    print("\n4. Koji je najbrži kopneni sisavac?")
    odgovor4 = input("a) Gepard\nb) Lav\nc) Antilopa\nd) Konj\nOdgovor: ")
    if odgovor4.lower() == 'a':
        bodovi += 1

    
    print("\n5. Koji je najbliži planet Suncu?")
    odgovor5 = input("a) Zemlja\nb) Mars\nc) Merkur\nd) Venera\nOdgovor: ")
    if odgovor5.lower() == 'c':
        bodovi += 1

    
    print(f"\nOsvojili ste {bodovi} od 5 bodova.")

    input("Pritisnite Enter za izlaz...")

kviz()
