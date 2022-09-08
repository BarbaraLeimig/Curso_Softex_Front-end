class ClubedoLivro:

    def __init__(self, name: str, age: int, books: int):
        self.__name = name  # __ = atributo private
        self.__age = age  # __ = atributo private
        self.__books = books  # __ = atibuto private. books = número de livros lidos ao ano

    # incluindo os métodos acessores
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_books(self):
        return self.__books

    # incluindo os métodos modificadores
    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

    def set_books(self, new_book):  # incluindo método construtor
        if new_book > 0:
            self.__books += new_book


#  criando objeto para cada atributo
followup_new_book = ClubedoLivro('Ana Martins', 27, 5)  # acompanhamento do registro no sistema de novos livros lidos

#  teste dos métodos acessores
print(f'Nome: {followup_new_book.get_name()}')
print(f'Idade: {followup_new_book.get_age()}')
print(f'Número de livros lidos este ano: {followup_new_book.get_books()}')

# teste dos métodos modificadores
followup_new_book.set_name('Ana Martins')
followup_new_book.set_age(28)
followup_new_book.set_books(2)
print()
print(f'Nome: {followup_new_book.get_name()}')
print(f'Idade: {followup_new_book.get_age()}')
print(f'Número de livros lidos este ano: {followup_new_book.get_books()}')
