from SPARQLWrapper import SPARQLWrapper, JSON
from collections import OrderedDict
from .dbpedia_attributes import ATTRIBUTES
SPARQL_ENDPOINT_URL = 'http://dbpedia.org/sparql'
LANGUAGE_PREDICATES = ['rdfs:label', 'dbpedia-owl:abstract']

class DBpediaSPARQLEndpoint(object):

    def query_attributes(self, uri, classes):
        attributes = []

        for class_name in classes:
            if class_name in ATTRIBUTES.keys():
                for attribute in ATTRIBUTES[class_name]:
                    attributes.append(attribute)

        sparql_query = self.generate_sparql_query(uri, attributes)
        query_results = self.execute_sparql_query(sparql_query)

        attribute_values = OrderedDict()

        for result in query_results['results']['bindings']:
            for attribute in attributes:
                attribute_name = attribute[0]
                variable_name = attribute_name.replace(' ', '')

                if variable_name in result.keys():
                    attribute_value = result[variable_name]['value']

                    if attribute_name in attribute_values.keys():
                        if attribute_value not in attribute_values[attribute_name]:
                            attribute_values[attribute_name].append(attribute_value)
                    else:
                        attribute_values[attribute_name] = [attribute_value]

        return attribute_values

    def generate_sparql_query(self, uri, attributes):
        variables = []
        query_pattern = ''
        temp_variable_number = 1

        for attribute in attributes:
            variable = '?' + attribute[0].replace(' ', '')
            variables.append(variable)

            subject = '<' + uri + '>'

            query_pattern += 'OPTIONAL { '

            for predicate in attribute[1][:-1]:
                temp_variable = '?x' + str(temp_variable_number)
                query_pattern += subject + ' ' + predicate + ' ' + temp_variable + ' .\n'
                subject = temp_variable
                temp_variable_number += 1

            predicate = attribute[1][-1]
            query_pattern += subject + ' ' + predicate + ' ' + variable + ' . \n'

            if predicate in LANGUAGE_PREDICATES:
                query_pattern += 'FILTER(langMatches(lang(' + variable + '), "EN"))'

            query_pattern += '}\n'

        result_clause = 'SELECT'

        for variable in variables:
            result_clause += ' ' + variable

        sparql_query = result_clause + '\nWHERE\n{\n'
        sparql_query += query_pattern
        sparql_query += '}'

        return sparql_query

    def execute_sparql_query(self, sparql_query):
        sparql_endpoint = SPARQLWrapper(SPARQL_ENDPOINT_URL)
        sparql_endpoint.setQuery(sparql_query)
        sparql_endpoint.setReturnFormat(JSON)

        results = sparql_endpoint.query().convert()

        return results
