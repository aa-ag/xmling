###--- IMPORTS ---###
import xml.etree.ElementTree as ET
'''
[!] Warning: The xml.etree.ElementTree
module is not secure against maliciously constructed data.
If you need to parse untrusted or
unauthenticated data see XML vulnerabilities.
(https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)
'''
# import pandas as pd


###--- CODE ---###


def make_xml():
    '''
    Creates 'root' element with 'xml.etree.ElementTree' object,
    then creates 'product' subelement, and its attributes and elements.
    Finally, writes the element tree to a file as XML.
    '''
    xml_doc = ET.Element('root')

    # 1st product
    product = ET.SubElement(xml_doc, 'product')

    ET.SubElement(product, 'item', id='1', price='9.99',
                  currency='¥').text = "Lorem ipsum dolor sit amet."
    ET.SubElement(product, 'brand', model='modelx').text = "Brand X"

    # 2nd product
    product = ET.SubElement(xml_doc, 'product')

    ET.SubElement(product, 'item', id='2', price='99.99',
                  currency='¥').text = "Consectetuer adipiscing elit."
    ET.SubElement(product, 'brand', model='modely').text = "Brand Y"

    # 3rd product
    product = ET.SubElement(xml_doc, 'product')

    ET.SubElement(product, 'item', id='3', price='999.99',
                  currency='¥').text = "Aenean commodo ligula eget dolor."
    ET.SubElement(product, 'brand', model='modelz').text = "Brand Z"

    tree = ET.ElementTree(xml_doc)
    ET.indent(tree, space='    ')
    tree.write('output_test.xml', encoding='UTF-8', xml_declaration=True)


# def make_dataframe(output_test):
#     attributes = output_test.attrib

#     for xml in output_test.iter('product'):
#         doct_dict = attributes.copy()
#         doct_dict.update(xml.attrib)
#         doct_dict['data'] = xml.text

#         yield doct_dict


# etree = ET.parse('output_test.xml')
# df = pd.DataFrame(list(make_dataframe(etree.getroot())))

# print(df)

###--- DRIVER CODE ---###
if __name__ == "__main__":
    make_xml()
