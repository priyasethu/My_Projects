from rdflib import Graph

# Load your Turtle file into an RDF graph
g = Graph()
g.parse("patient.ttl", format="turtle")

print(f"Graph loaded. Total triples: {len(g)}")

# ── Query 1: Get all patients and their names ──────────────────────
query1 = """
PREFIX ex: <http://example.org/health#>

SELECT ?patient ?name
WHERE {
    ?patient a ex:Patient .
    ?patient ex:hasName ?name .
}
"""
query2 = """
PREFIX ex: <http://example.org/health#>

SELECT ?conditionName
WHERE {
    ex:Patient_Nguyen ex:hasCondition ?condition .
    ?condition ex:hasName ?conditionName .
}
"""


# ── Query 3: Doctor → Patient → Clinic ──────────────────────────
query3 = """
PREFIX ex: <http://example.org/health#>

SELECT ?doctorName ?patientName ?clinicName
WHERE {
    ?doctor    a              ex:Doctor ;
               ex:hasName     ?doctorName ;
               ex:manages     ?patient ;
               ex:worksAt     ?clinic .
    ?patient   ex:hasName     ?patientName .
    ?clinic    ex:hasName     ?clinicName .
}
"""




print("\n── Query 1: All patients ──")
for row in g.query(query1):
    print(f"  Patient: {row.patient}")
    print(f"  Name:    {row.name}")

print("\n── Query 2: Conditions for James Nguyen ──")
for row in g.query(query2):
    print(f"  Condition: {row.conditionName}")

print("\n── Query 3: Doctor → Patient → Clinic ──")
for row in g.query(query3):
    print(f"  Doctor:  {row.doctorName}")
    print(f"  Patient: {row.patientName}")
    print(f"  Clinic:  {row.clinicName}")