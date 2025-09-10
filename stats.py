def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_text = text.lower()
    count = {char: lower_text.count(char) for char in set(lower_text)}
    return count

def character_count_sorted(characters):
    return sorted([{k: v} for k, v in characters.items()], key=lambda d: list(d.values())[0], reverse=True)