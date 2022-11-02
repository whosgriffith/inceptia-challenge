import pandas as pd

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
                            "quantity": [3, 10, 0, 5]})


# Nota: No logre entender muy bien la idea del ejercicio, el loop esta por fuera de la funcion, siempre que se llame
# a la funcion con los mismo valores se va a repetir el resultado, pero para resolver el ejercicio decidi dar
# una excepcion en caso de que no haya stock o no exista ese producto

class ProductNotFoundError(Exception):
    """Raised when the product doesn't exist"""
    pass


class NoStockFoundError(Exception):
    """Raised when the product exist but doesn't have any stock"""
    pass


def is_product_available(product_name, quantity):
    product_dataframe = _PRODUCT_DF.apply(lambda x: x.astype(str).str.lower())
    product_name = product_name.lower()

    if product_name not in product_dataframe.values:
        raise ProductNotFoundError

    product_df = product_dataframe.query(f'product_name == "{product_name}"')
    stock = int(product_df.get('quantity'))

    if stock == 0:
        raise NoStockFoundError

    if quantity > stock:
        return False

    return True


print(is_product_available("Chocolate", 6))
