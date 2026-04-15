def vowel_counter(word):
    if not isinstance(word, str):
        return "Input must be a string."
    elif not word:
        return "Input cannot be empty"
    else:
        count_vowel = 0
        count_consonant = 0
        for letter in word:
            if letter.lower() in 'aeiou':
                count_vowel += 1
            else:
                count_consonant += 1
        return f"vowel: {count_vowel}, consonant: {count_consonant}"        
    

print(vowel_counter("Michael"))