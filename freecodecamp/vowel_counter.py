def vowel_counter(word):
    if not isinstance(word, str):
        return "Argument must be a string."
    elif not word:
        return "Argument must not be empty."
    else:
        count_vowel = 0
        count_consonant = 0
        for letter in word:
            if letter.lower() not in 'aeiou':
                count_consonant += 1
            else:
                count_vowel += 1
        return f"vowels: {count_vowel}, consonants: {count_consonant}"
    

print(vowel_counter('Python'))