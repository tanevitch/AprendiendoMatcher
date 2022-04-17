import spacy
from spacy.matcher import Matcher

# Modelo de precisión en inglés
nlp = spacy.load("en_core_web_trf")

class AprendiendoMatcher:
    matcher = Matcher(nlp.vocab)
    
    def __init__(self, expresion):
        self.matcher.add("patron", expresion)
        
    def setMatcher(self, expresion) -> None:
        '''
        Por cuestiones de simplicidad, este matcher va a trabajar con un solo patrón a la vez. Por esta razón, cada vez que se setea uno nuevo se borra el anterior
        '''
        self.matcher.remove("patron")
        self.matcher.add("patron", expresion)
          
    def procesarOracionLenguajeNatural(self, oracion_lenguaje_natural) -> list[str]:
        '''
        Procesa la oración con NLP, porque el matcher espera eso como parámetro. Luego, la procesa con el matcher y retorna una lista de strings que son las palabras que matchearon con el patrón seteado
        '''
        oracion_procesada = nlp(oracion_lenguaje_natural)
        matches= self.matcher(
            oracion_procesada, as_spans=True
        )
        return list(map(lambda each: str(each), matches))
