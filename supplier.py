class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    # Read only access to private attributes (copy same style as Product)
    @property
    def supplier_id(self) -> str:
        return self.__supplier_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def contact_email(self) -> str:
        return self.__contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id}\n"
              f"Supplier Name: {self.__name}\n"
              f"Contact Email: {self.__contact_email}")

    def __str__(self) -> str:
        # one line summary of the supplier
        return f"{self.__name} ({self.__supplier_id})"
    