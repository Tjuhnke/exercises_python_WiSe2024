def buchstaben_zählen(text):
    text_list = list(text) 
    text_buchstaben = [i for i in text_list if i.isalpha()]
    text_buchstaben_len = len(text_buchstaben)
    return text_buchstaben_len
    
print(buchstaben_zählen("Hallo, Berlin!"))