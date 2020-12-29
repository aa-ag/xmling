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

    df = pd.DataFrame(df_rows, columns=df_columns)

    # display dataframe
    print(df)

    '''
      id   price currency                        description   brand brand description
    0  1    9.99        ¥        Lorem ipsum dolor sit amet.  modelx           Brand X
    1  2   99.99        ¥      Consectetuer adipiscing elit.  modely           Brand Y
    2  3  999.99        ¥  Aenean commodo ligula eget dolor.  modelz           Brand Z
    '''

    # save dataframe to CSV
    df.to_csv('xml.csv', index=False)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    make_xml()
    convert_to_dataframe()
