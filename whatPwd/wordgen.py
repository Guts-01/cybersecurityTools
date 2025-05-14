import itertools

def generate_passwords(words):
    combos = []
    for r in range(2, len(words)+1):
        for combo in itertools.permutations(words, r):
            combos.append(''.join(combo))
    return combos

def generate_usernames(words):
    usernames = set()
    # Combinações simples comuns
    for word in words:
        usernames.add(word.lower())
        usernames.add(word.lower() + "123")
        usernames.add(word.lower() + "_br")
        usernames.add(word.lower() + "2023")
        usernames.add(word.lower() + "01")
    # Combinações entre palavras
    for r in range(2, 3):  # Até 2 palavras combinadas
        for combo in itertools.permutations(words, r):
            joined = ''.join(combo).lower()
            usernames.add(joined)
            usernames.add(joined + "01")
            usernames.add(joined + "_ofc")
    return list(usernames)
