import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
                            "quantity": [3, 10, 0, 5]})


def is_product_available(product_name, quantity):
    product_dataframe = _PRODUCT_DF.apply(lambda x: x.astype(str).str.lower())
    product_name = product_name.lower()

    if product_name not in product_dataframe.values:
        return False

    product_df = product_dataframe.query(f'product_name == "{product_name}"')
    stock = int(product_df.get('quantity'))

    if quantity > stock:
        return False

    return True


print(is_product_available("dulce de leche", 6))
