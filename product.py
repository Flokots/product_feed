class Product:
    """ A Product Class"""

    def __init__(self, id, quantity, title, description, image, alt_image, sort_order, price, brand):
        self.id = id
        self.quantity = quantity
        self.title = title
        self.description = description
        self.image = image
        self.alt_image = alt_image
        self.sort_order = sort_order
        self.price = price
        self.brand = brand

    # 2. Create link to product by appending the product.product_id to https://butopea.com/p/
    @property
    def link(self):
        return 'https://butopea.com/p/{}'.format(self.id)

    # 3. Create image link by appending the product_image.image to https://butopea.com/
    @property
    def image_link(self):
        return 'https://butopea.com/{}'.format(self.image)

    # 4. Create additional image link using product_image.sort_order
    @property
    def additional_image_link(self):
        return 'https://butopea.com/{}'.format(self.alt_image)

    # 5.  Check item availability. Item is available if quantity > 0. 
    @property
    def availability(self):
        if int(self.quantity) > 0:
            availability = 'in_stock'
        else:
            availability = 'out_of_stock'

        return availability

    # 6. Currency to forints
    @property
    def price_currency(self):
        return 'HUF'

    # 7. Set all products conditions to new
    @property
    def condition(self):
        return 'new'
   

    def __repr__(self):
        return "'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(self.id, self.title, self.description, self.image, self.alt_image, self.sort_order, self.quantity, self.price, self.brand, self.link, self.image_link, self.additional_image_link, self.availability, self.condition, self.price_currency)