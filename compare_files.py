import rdflib
import sys


def compare_files(file_1, file_2):
    g = rdflib.graph.ConjunctiveGraph()
    # ... add some triples to g somehow ...
    g.parse(file_2, file_1, format='n3')
    query_result = g.query(
        """
            SELECT DISTINCT ?S
                WHERE { GRAPH <old.ttl>
                {?S ?P ?O }
                FILTER NOT EXISTS
                { GRAPH <new.ttl>
                {?S ?P ?O}
                }}
           """)
    for row in query_result:
        print(row)
    return query_result


if __name__ == "__main__":
    compare_files(sys.argv[1], sys.argv[2])