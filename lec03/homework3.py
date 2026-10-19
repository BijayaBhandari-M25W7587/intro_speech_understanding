def words2characters(words):
    words=['hello', 1.234, True] 
    chars = []
    for word in words:
        for c in str(word):
            chars.append(c)
    return chars
    

