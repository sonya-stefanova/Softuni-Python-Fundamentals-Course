class Catalogue:

    def __init__(self, name:str):
        self.name = name
        self.products = []

    def add_product(self, product_name:str):
        self.products.append(product_name) #<== пълним листа с подадените продукти

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if len(product) and product[0] == first_letter]

    def __repr__(self):
        if len(self.products):
            sorted_list = sorted(self.products)
            formatted_request = '\n'.join(sorted_list)
            return f"Items in the {self.name} catalogue: \n{formatted_request}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
