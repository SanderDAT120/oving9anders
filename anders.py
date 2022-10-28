#Anders

from datetime import datetime

class Avtale:
    def __init__(self, tittel, sted, dato, varighet):
        self.tittel=tittel      #str
        self.sted=sted          #str
        self.dato=dato          #datetime.datetime
        self.varighet=varighet  #int
        
    def __str__(self): #
        return f"{self.tittel}, {self.sted}, {self.dato}, {self.varighet}"
        
def nyavtale():
   tittel=input("Tittel til avtale: ")
   sted=input("Sted: ")
   dato=input("Kode for datoen: ")
   try:
       varighet=int(input("Varighet: "))
   except ValueError:
       print("Ugyldig tidverdi!")
       
    