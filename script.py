###--- IMPORTS ---###
import xml.etree.ElementTree as ET
'''
[!] Warning: The xml.etree.ElementTree
module is not secure against maliciously constructed data.
If you need to parse untrusted or
unauthenticated data see XML vulnerabilities.
(https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)
'''
import pandas as pd


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


def convert_to_dataframe():
    xtree = ET.parse("output_test.xml")
    xroot = xtree.getroot()

    df_columns = ["id", "price", "currency",
                  "description", "brand", "brand description"]
    df_rows = list()

    for node in xroot:
        product_id = node.find("item").attrib.get('id')
        product_price = node.find("item").attrib.get('price')
        product_currency = node.find("item").attrib.get('currency')
        product_description = node.find("item").text
        product_brand = node.find("brand").attrib.get('model')
        product_brand_description = node.find("brand").text

        df_rows.append({"id": product_id, "price": product_price, "currency": product_currency,
                        "description": product_description, "brand": product_brand, "brand description": product_brand_description})

    print(df_rows)

    '''
    [{'id': '1', 'price': '9.99', 'currency': '¥', 'description': 'Lorem ipsum dolor sit amet.', 'brand': 'modelx', 'brand description': 'Brand X'}, 
    {'id': '2', 'price': '99.99', 'currency': '¥', 'description': 'Consectetuer adipiscing elit.', 'brand': 'modely', 'brand description': 'Brand Y'}, 
    {'id': '3', 'price': '999.99', 'currency': '¥', 'description': 'Aenean commodo ligula eget dolor.', 'brand': 'modelz', 'brand description': 'Brand Z'}]
    '''


###--- DRIVER CODE ---###
if __name__ == "__main__":
    make_xml()
    convert_to_dataframe()
