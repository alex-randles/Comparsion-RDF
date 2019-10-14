import rdflib
import sys


def compare_files(file_1, file_2):
    g = rdflib.graph.ConjunctiveGraph()
    # ... add some triples to g somehow ...
    g.parse(file_1, file_2, format='n3')
    query_result = g.query(
        """
             SELECT * 
             FROM NAMED <old.ttl>
             FROM <new.ttl>
             WHERE{
                 ?S ?P ?O
                 GRAPH <new.ttl> {?S1 ?P1 ?O1}
             }
           """)
    for row in query_result:
        print(row)
    return query_result


if __name__ == "__main__":
    compare_files(sys.argv[1], sys.argv[2])