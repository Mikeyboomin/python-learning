def word_length_finder(sentence):
    if not isinstance(sentence, str):
        return "Argument must be a string."
    elif not sentence:
        return "Argument must not be empty."
    else:
        result = ''
        words = sentence.split()
        for word in words:
            if word == words[-1]:
                result += f"{word}:{len(word)}"
            else:
                result += f"{word}:{len(word)}" + " "
        return result


print(word_length_finder("I love coding"))