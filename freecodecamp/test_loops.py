abilities = ['fly', 'speed', 'strength', 'invisibility']

for ability in abilities:
    for letter in ability:
        if letter in 'aeiou':
            print(f'{ability} has the vowel {letter}')
            break
    else:
        print(f'{ability} does not contain a vowel')