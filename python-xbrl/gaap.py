from parser import XBRLParser, GAAP, GAAPSerializer

xbrl_parser = XBRLParser(precision=0)

# Parse an incoming XBRL file
xbrl = xbrl_parser.parse(file("sam-20140329.xml"))

# Parse just the GAAP data from the xbrl object
gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20140329")

# Serialize the GAAP data
serialized = GAAPSerializer(gaap_obj)

# Print out the serialized GAAP data
print serialized.data