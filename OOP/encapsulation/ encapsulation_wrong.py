class Book:
    def __init__(self, name_book, price_book, vat_price):
        self.name_book = name_book
        self.price_book = price_book
        self.vat_price = vat_price / 100

    def get_total_price(self):
        return self.price_book + self.price_book * self.vat_price

    def to_string(self):
        return f'This book "{self.name_book}" sells for {self.get_total_price()} USD with VAT ({self.vat_price * 100}%)'


# Автор класса предоставил пример использования класса
pythonBook = Book('Python Book', 20, 18)
print(pythonBook.to_string())
# Неожиданно нагрянула новая налоговая политика
# И другой программист решил поправить налог
pythonBook.vat_price = 25
print(pythonBook.to_string())
