def conteo(name_p1, name_p2, wins):
    p1_count = 0
    p2_count = 0
    for word in wins.split():
        if name_p1 == word:
            p1_count += 15
        if name_p2 == word:
            p2_count += 15
    print(p1_count, p2_count)

conteo("Bob", "Anna", "Bob, Anna, Bob")