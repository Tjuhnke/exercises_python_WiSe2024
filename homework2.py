def buchstabe_ändern(string, buchstabe):
i    string_lower = string.lower()
    
    for v in "aeiou":
        new_sentence = []
        
        for char in string_lower:
            if char == buchstabe: 
                new_sentence.append(v)
            else: 
                new_sentence.append(char)
                
        print("".join(new_sentence)) 
        #leere string den neuen Satz und mit join werden alle zusammen getan 
        
#buchstabe_ändern("banana","a")

buchstabe_ändern("Wie geht es Ihnen?",
                 "e")