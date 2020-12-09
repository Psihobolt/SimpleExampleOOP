class Book:
    def __init__(self, name_book, price_book, vat_price):
        self.__name_book = name_book
        self.__price_book = price_book
        self.vat_price = vat_price

    @property
    def vat_price(self):
        return self.__vat_price

    @vat_price.setter
    def vat_price(self, value):
        self.__vat_price = value / 100

    def get_total_price(self):
        return self.__price_book + self.__price_book * self.vat_price

    def to_string(self):
        return f'This book "{self.__name_book}" sells for {self.get_total_price()} USD with VAT ({self.vat_price * 100}%)'


# Автор класса предоставил пример использования класса
pythonBook = Book('Python Book', 20, 18)
print(pythonBook.to_string())
# Неожиданно нагрянула новая налоговая политика
# И другой программист решил поправить налог
pythonBook.vat_price = 25
print(pythonBook.to_string())
