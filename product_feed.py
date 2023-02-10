import sqlite3
import xml.etree.ElementTree as ET
from product import Product

# TODO
# 1.  Read the data from the database where status != 0

# Connect to the database
conn = sqlite3.connect('data.sqlite')

# Create a cursor
c = conn.cursor()

# Fetch data
c.execute("""
SELECT 
product.product_id AS id, product.quantity AS quantity, product_description.name AS title, product_description.description AS description, product.image AS image, product_image.image AS alt_image, product_image.sort_order AS sort_order, product.price AS price, manufacturer.name AS brand
FROM product
INNER JOIN
manufacturer
ON 
product.manufacturer_id = manufacturer.manufacturer_id
INNER JOIN 
product_description 
ON 
product.product_id = product_description.product_id
JOIN
product_image
ON
product.product_id = product_image.product_id
WHERE product.status != '0'
GROUP BY 
    product.product_id
ORDER BY 
    product_image.sort_order
""")

items = c.fetchall()

# Loop through the data
product_feed = ET.Element('root')

for item in items:
    prod = Product(item[0], item[1], item[2], item[3],
                   item[4], item[5], item[6], item[7], item[8], )

    print(prod)

    product = ET.SubElement(product_feed, 'product')
    ET.SubElement(product, 'id').text = prod.id
    ET.SubElement(product, 'title').text = prod.title
    ET.SubElement(product, 'description').text = prod.description
    ET.SubElement(product, 'link').text = prod.link
    ET.SubElement(product, 'image_link').text = prod.image_link
    ET.SubElement(
        product, 'additional_image_link').text = prod.additional_image_link
    ET.SubElement(product, 'availability').text = prod.availability
    ET.SubElement(product, 'price').text = prod.price + \
        ' ' + prod.price_currency
    ET.SubElement(product, 'brand').text = prod.brand
    ET.SubElement(product, 'condition').text = prod.condition

# 8. Generate xml file
tree = ET.ElementTree(product_feed)
tree.write('feed.xml', encoding='UTF-8', xml_declaration=True)


# Close database connection
conn.close()
