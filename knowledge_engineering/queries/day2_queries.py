from rdflib import Graph

g = Graph()
g.parse("ontologies/patient.ttl", format="turtle")
print(f"Total triples: {len(g)}")

# Query 1: All patients with name and DOB
query1 = """
PREFIX ex: <http://example.org/health#>

SELECT ?patient ?name ?dob
WHERE {
    ?patient a           ex:Patient ;
             ex:hasName  ?name ;
             ex:hasBirthDate ?dob .
}
"""
print("\n── Query 1: All patients ──")
for row in g.query(query1):
    print(f"  Patient: {row.patient}")
    print(f"  Name:    {row.name}")
    print(f"  DOB:     {row.dob}")

# Query 2: Patients born before 1980
query2 = """
PREFIX ex:  <http://example.org/health#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?patient ?name ?dob
WHERE {
    ?patient a               ex:Patient ;
             ex:hasName      ?name ;
             ex:hasBirthDate ?dob .
    FILTER (?dob < "1980-01-01"^^xsd:date)
}
"""
print("\n── Query 2: Patients born before 1980 ──")
for row in g.query(query2):
    print(f"  Patient: {row.patient}")
    print(f"  Name:    {row.name}")
    print(f"  DOB:     {row.dob}")

# Query 3: All patients and last visit (OPTIONAL)
query3 = """
PREFIX ex: <http://example.org/health#>

SELECT ?patient ?name ?lastVisit
WHERE {
    ?patient a ex:Patient ;
             ex:hasName ?name .
    OPTIONAL { ?patient ex:lastVisit ?lastVisit . }
}
"""
print("\n── Query 3: Patients and last visit date ──")
for row in g.query(query3):
    print(f"  Name:       {row.name}")
    print(f"  Last Visit: {row.lastVisit if row.lastVisit else 'N/A'}")

# Query 4: All patients and their conditions
query4 = """
PREFIX ex: <http://example.org/health#>

SELECT ?patient ?name ?conditionName
WHERE {
    ?patient  a               ex:Patient ;
              ex:hasName      ?name ;
              ex:hasCondition ?condition .
    ?condition ex:hasName     ?conditionName .
}
"""
print("\n── Query 4: Patients and conditions ──")
for row in g.query(query4):
    print(f"  Name:      {row.name}")
    print(f"  Condition: {row.conditionName}")