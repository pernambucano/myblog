ATTRIBUTES = {
    'owl:Thing':[('label', ['rdfs:label']),
                 ('abstract', ['dbpedia-owl:abstract']),
                 ('website', ['foaf:homepage'])],

    'DBpedia:Agent':[('title', ['dbpprop:title', 'rdfs:label']),
                     ('description', ['dc:description']),
                     ('occupation', ['dbpprop:occupation']),
                     ('profession', ['dbpprop:profession']),
                     ('partner', ['dbpedia-owl:partner', 'rdfs:label'])],

    'DBpedia:Band':[('origin', ['dbpprop:origin']),
                    ('genre', ['dbpedia-owl:genre', 'rdfs:label']),
                    ('years active', ['dbpprop:yearsActive']),
                    ('record label', ['dbpprop:label', 'rdfs:label']),
                    ('member', ['dbpedia-owl:bandMember', 'rdfs:label']),
                    ('former member', ['dbpedia-owl:formerBandMember', 'rdfs:label'])],

    'DBpedia:Person':[('birth name', ['dbpprop:birthName']),
                      ('birth date', ['dbpedia-owl:birthDate']),
                      ('birth place', ['dbpedia-owl:birthPlace', 'rdfs:label']),
                      ('death date', ['dbpedia-owl:deathDate']),
                      ('death place', ['dbpedia-owl:deathPlace', 'rdfs:label']),
                      ('spouse', ['dbpprop:spouse']),
                      ('children', ['dbpprop:children', 'rdfs:label']),
                      ('alma mater', ['dbpedia-owl:almaMater', 'rdfs:label']),
                      ('religion', ['dbpedia-owl:religion', 'rdfs:label'])],

    'DBpedia:MusicalArtist':[('genre', ['dbpedia-owl:genre', 'rdfs:label']),
                             ('instrument', ['dbpprop:instrument', 'rdfs:label'])],

    'DBpedia:Scientist':[('known for', ['dbpedia-owl:knownFor', 'rdfs:label']),
                         ('field', ['dbpedia-owl:field', 'rdfs:label']),
                         ('doctoral advisor', ['dbpprop:doctoralAdvisor', 'rdfs:label']),
                         ('nationality', ['dbpprop:nationality']),
                         ('work institutions', ['dbpprop:workInstitutions', 'rdfs:label'])],

    'DBpedia:OfficeHolder':[('party', ['dbpedia-owl:party', 'rdfs:label'])],

    'DBpedia:Colour':[('frequency', ['dbpprop:frequency']),
                      ('wave length', ['dbpprop:wavelength']),
                      ('rgb coordinate red', ['dbpedia-owl:rgbCoordinateRed']),
                      ('rgb coordinate green', ['dbpedia-owl:rgbCoordinateGreen']),
                      ('rgb coordinate blue', ['dbpedia-owl:rgbCoordinateBlue'])],

    'DBpedia:Place':[('area total', ['dbpedia-owl:areaTotal']),
                     ('percentage of area water', ['dbpedia-owl:percentageOfAreaWater']),
                     ('time zone', ['dbpprop:timeZone', 'rdfs:label'])],

    'DBpedia:PopulatedPlace':[('capital', ['dbpedia-owl:capital', 'rdfs:label']),
                              ('largest city', ['dbpedia-owl:largestCity', 'rdfs:label']),
                              ('official language', ['dbpedia-owl:officialLanguage', 'rdfs:label']),
                              ('demonym', ['dbpedia-owl:demonym']),
                              ('government type', ['dbpprop:governmentType', 'rdfs:label']),
                              ('leader', ['dbpedia-owl:leader', 'rdfs:label']),
                              ('legislature', ['dbpprop:legislature', 'rdfs:label']),
                              ('population total', ['dbpedia-owl:populationTotal']),
                              ('population density', ['dbpedia-owl:populationDensity'])],

    'DBpedia:Country':[('gdp ppp total', ['dbpprop:gdpPpp']),
                       ('gdp ppp per capita', ['dbpprop:gdpPppPerCapita']),
                       ('gdp nominal total', ['dbpprop:gdpNominal']),
                       ('gdp nominal per capita', ['dbpprop:gdpNominalPerCapita']),
                       ('currency', ['dbpedia-owl:currency', 'rdfs:label']),
                       ('date format', ['dbpprop:dateFormat']),
                       ('drives on the', ['dbpprop:drivesOn'])],

    'DBpedia:City':[('country', ['dbpedia-owl:country', 'rdfs:label']),
                    ('leader name', ['dbpedia-owl:leaderName', 'rdfs:label']),
                    ('population demonym', ['dbpprop:populationDemonym']),
                    ('nickname', ['dbpprop:nickname'])],

    'DBpedia:University':[('campus', ['dbpedia-owl:campus', 'rdfs:label']),
                          ('motto', ['dbpprop:motto']),
                          ('country', ['dbpprop:country']),
                          ('state', ['dbpedia-owl:state', 'rdfs:label']),
                          ('city', ['dbpedia-owl:city', 'rdfs:label']),
                          ('faculty size', ['dbpedia-owl:facultySize']),
                          ('number of students', ['dbpedia-owl:numberOfStudents']),
                          ('official school colour', ['dbpedia-owl:officialSchoolColour']),
                          ('president', ['dbpedia-owl:president', 'rdfs:label'])],

    'DBpedia:Work':[('genre', ['dbpedia-owl:genre', 'rdfs:label'])],

    'DBpedia:Book':[('author', ['dbpedia-owl:author', 'rdfs:label']),
                    ('country', ['dbpprop:country']),
                    ('illustrator', ['dbpprop:illustrator']),
                    ('publisher', ['dbpedia-owl:publisher', 'rdfs:label'])],

    'DBpedia:Film':[('creator', ['dbpprop:creator', 'rdfs:label']),
                    ('writer', ['dbpedia-owl:writer', 'rdfs:label']),
                    ('language', ['dbpedia-owl:language', 'rdfs:label']),
                    ('country', ['dbpedia-owl:country', 'rdfs:label']),
                    ('author', ['dbpedia-owl:author', 'rdfs:label']),
                    ('starring', ['dbpedia-owl:starring', 'rdfs:label']),
                    ('cinematography', ['dbpedia-owl:cinematography', 'rdfs:label']),
                    ('director', ['dbpedia-owl:director', 'rdfs:label']),
                    ('distributor', ['dbpedia-owl:distributor', 'rdfs:label']),
                    ('editing', ['dbpedia-owl:editing', 'rdfs:label']),
                    ('producer', ['dbpedia-owl:producer', 'rdfs:label'])],

    'DBpedia:TelevisionShow':[('composer', ['dbpedia-owl:composer', 'rdfs:label']),
                              ('country', ['dbpprop:country']),
                              ('creator', ['dbpedia-owl:creator', 'rdfs:label']),
                              ('language', ['dbpprop:language', 'rdfs:label']),
                              ('num episodes', ['dbpprop:numEpisodes']),
                              ('num seasons', ['dbpedia-owl:numberOfSeasons']),
                              ('open theme', ['dbpprop:opentheme']),
                              ('starring', ['dbpedia-owl:starring', 'rdfs:label'])]

}
