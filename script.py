###--- IMPORTS ---###
import xml.etree.ElementTree as ET
'''
[!] Warning: The xml.etree.ElementTree 
module is not secure against maliciously constructed data. 
If you need to parse untrusted or 
unauthenticated data see XML vulnerabilities.
(https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)
'''

###--- CODE ---###


def make_xml():
    '''
    Creates 'root' element with 'xml.etree.ElementTree' object,
    then creates 'product' subelement, and its attributes and elements.
    Finally, writes the element tree to a file as XML.
    '''
    xml_doc = ET.Element('root')

    product = ET.SubElement(xml_doc, 'product')

    ET.SubElement(product, 'item', id='product_id', price='9.99',
                  currency='USD').text = "Product description in detail since attributes already included."
    ET.SubElement(product, 'brand', model='testtesttest123').text = "Brand XYZ"

    tree = ET.ElementTree(xml_doc)
    ET.indent(tree, space='    ')
    tree.write('output_test.xml', encoding='UTF-8', xml_declaration=True)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    make_xml()
