from rdflib import Graph
g = Graph()
g.parse("ontologies/patient.ttl", format="turtle")
print(f"Total triples:{len}")