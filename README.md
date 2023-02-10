# Product Feed
A product feed is an essential medium for exporting and syncing the product catalog to external systems such as marketplaces and B2B partners. 

This program creates an XML product feed according to the [Google Merchant product data specifications](https://support.google.com/merchants/answer/7052112).

# Tasks
Generate a file: [feed.xml](./feed.xml), including the following fields: 
* ID [id]  
* Title [title] 
* Description [description]
* Link [link]
* Image link [image_link]
* Additional image link [additional_image_link]
* Availability [availability]
* Price [price]
* Brand [brand]
* Condition [condition]

Additional details:
* The field values included in the product feed must conform to Google Merchant specifications.
* Disabled products (with status `0`) must not be included in the feed. 
* All prices are in Hungarian Forints (HUF)
* Brand represents the product manufacturer
* All products are sold as new
* The base domain for product image URLs is `butopea.com`, for example: [ https://butopea.com/image/catalog/DEJEL-NS3TE[D]_1.jpg]( https://butopea.com/image/catalog/DEJEL-NS3TE[D]_1.jpg)
* Additional images must be loaded in their respective sort orders
* The product link can be constructed by appending the product ID to `https://butopea.com/p/`, for example: `https://butopea.com/p/3927`
  * It's fine if the actual links go to the not found page –– this is test data.
  
### Technologies and Dependencies Used
* Python3.11
* XML
* SQLite

### Development Steps
1. Read the data from the database where status != 0. Group by the product_id and order by the product_image.sort_order.
2. Create a Product class. 
3. Create a link to the product by appending the product.product_id to https://butopea.com/p
4. Create image link by appending the product_image.image to https://butopea.com/
5. Create additional image link. 
6. Check item availability. Item is available if quantitity > 0. 
7. Change the currency to forints.
8. Set all products conditions to new.
9. Loop through the data. 
10. Generate an XML file.
11. Close the database connection. 
   

### Project Setup
1. Clone this repository.
2. `cd` into the cloned repository.
3. Run `python3.11 product_feed.py`.
4. Have fun exploring!

### Contact
florencekotohoyoh@gmail.com

### Author
[Florence Kotohoyoh](https://github.com/Flokots)

