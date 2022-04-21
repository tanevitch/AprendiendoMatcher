import spacy
from spacy.matcher import Matcher

NLP = spacy.load("en_core_web_trf")
class SimpleMatcher:
    matcher = Matcher(NLP.vocab)
    
    def addPattern(self, pattern_name: str, expression: list):
        self.matcher.add(pattern_name, expression)

    def removePattern(self,pattern_name:str):
        self.matcher.remove(pattern_name)

    def getMatches(self, sentence: str):
        processed_sentence = NLP(sentence)

        matches = {}
        
        for match_id, start, end in self.matcher(processed_sentence):
            string_id = NLP.vocab.strings[match_id]  
            span = processed_sentence[start:end]  
            matches[string_id] = span.text if not string_id in matches.keys() else [matches[string_id]].extend(span.text)

        return matches
