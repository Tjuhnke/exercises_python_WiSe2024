def vokon_zählen(text):
    vokale = "aeiou"
    text_lower = text.lower()
  
    buchstaben = [i for i in text_lower if i.isalpha()]
    vokale = [i for i in buchstaben if i in vokale]
    
 #  return [len(buchstaben), len(vokale)]


    print(f"Es gibt {len(vokale)} Vokale und {len(buchstaben]-len(vokale)} Konsonanten.") 

vokon_zählen("Berlin")
vokon_zählen(" HI,&%/ BerliN!!")
