#!/usr/bin/env python
"""Generate MARCXML, RDFXML via CLI."""
import pymarc
import rdflib
from argparse import ArgumentParser

def generateMARCXML(MARC21input, MARCXMLoutput):
    """Write MARCXML file for given MARC21 binary file."""
    reader = pymarc.MARCReader(open(MARC21input, 'rb'))
    for record in reader:
        writer = pymarc.XMLWriter(open(MARCXMLoutput,'wb'))
        writer.write(record)
        writer.close()


def generateRDFXML(TurtleInput, RDFXMLoutput):
    """Write RDFXML file for given RDF Turtle file."""
    data = rdflib.Graph().parse(TurtleInput, format="turtle")
    data.serialize(RDFXMLoutput) #default is RDFXML


def main():
    # CLI arguments
    parser = ArgumentParser(description='simple marcxml CLI client',
                            usage='%(prog)s [options] data_filename.xml')
    parser.add_argument("-b", "--binaryMARC", dest="biMARC",
                        help="binary MARC file to be converted to XML.")
    parser.add_argument("-mx", "--MARCXML", dest="MARCXML",
                        help="MARCXML filename/file to be created.")
    parser.add_argument("-ttl", "--turtle", dest="turtleRDF",
                        help="turtle RDF file to be converted to XML.")
    parser.add_argument("-rx", "--RDFXML", dest="RDFXML",
                        help="RDFXML filename/file to be created.")

    args = parser.parse_args()

    if args.biMARC:
        if args.MARCXML:
            generateMARCXML(args.biMARC, args.MARCXML)
        else:
            MARCXML = args.biMARC.replace('.mrc', '.marc.xml')
            generateMARCXML(args.biMARC, MARCXML)

    if args.turtleRDF:
        if args.RDFXML:
            generateRDFXML(args.turtleRDF, args.RDFXML)
        else:
            RDFXML = args.turtleRDF.replace('.ttl', '.rdf')
            generateRDFXML(args.turtleRDF, RDFXML)


if __name__ == '__main__':
    main()