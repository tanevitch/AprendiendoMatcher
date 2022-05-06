from rdflib import Graph, Literal, RDF, RDFS, URIRef, OWL, Namespace
from rdflib.namespace import FOAF , XSD

class OntologyWrapper:
    def __init__(self): 
        self.base_url = Namespace("http://www.semanticweb.org#")
        self.graph = Graph()
        self.graph.bind("sw", self.base_url)
        self.graph.parse("ontoreq.ttl", format='ttl', encoding="utf-8")

    def count_individuals_of(self, node_type: str):
        return len(list(self.graph.triples((None, RDF.type, self.base_url[node_type]))))

    def find_individual_by_label(self, label):
        for s, p, o in self.graph.triples((None, RDFS.label, Literal(label,  lang= "es"))):
            return s

    def add_individual(self, label, node_type):
        existing_node= self.find_individual_by_label(label)
        if (existing_node):
            return existing_node

        individual= self.base_url[node_type.lower()+str(self.count_individuals_of(node_type))]
        self.graph.add((individual, RDF.type, self.base_url[node_type]))
        self.graph.add((individual, RDFS.label, Literal(label, lang="es")))
        return individual 

    def add_object_property(self, node_label_origin, relationship, node_label_dest):
        self.graph.add((
            self.find_individual_by_label(node_label_origin),
            self.base_url[relationship],
            self.find_individual_by_label(node_label_dest)
        ))
    
    def add_data_property(self, node_label_origin, relationship, literal_dest_label): 
        self.graph.add((
            self.find_individual_by_label(node_label_origin),
            self.base_url[relationship],
            Literal(literal_dest_label, datatype=XSD.string)
        ))

    def persist(self):
        self.graph.serialize("output.ttl", format="ttl", encoding="utf-8")

