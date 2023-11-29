import uuid
class Book:
    books={}

    def __init__(self,book_name,quantity):
        self.id=uuid.uuid4()
        self.book_name=book_name
        self.quantity=quantity


    def display_books(books,q=True):
        for i,b in enumerate(books):
            if q:
                print(f'''
                    sn:{i+1}\n
                    id:{b.id}\n
                    Name:{b.book_name}\n
                    Quantity:{b.quantity}\n
            '''.center(300,"*"))
            else:
                print(f'''
                    sn:{i+1}\n
                    id:{b.id}\n
                    Name:{b.book_name}\n
            '''.center(300,"*"))



    @classmethod
    def add(cls):
        name=str(input("Enter book name:")).strip()
        quantity=int(input("Enter book quantity:"))
        book=Book(name,quantity)
        cls.books[str(book.id)]=book
        print([*cls.books.keys()])

    @classmethod
    def show(cls):
        if cls.books:
            b=[*cls.books.values()]
            cls.display_books(b)
        else:
            print("No books available")

    @classmethod
    def remove(cls):
        try:
            if cls.books:
                cls.show()
                sn=int(input("Enter book symbool no.(sn): "))
                b=[*cls.books.keys()][sn-1]
                del cls.books[b]
        except Exception as e:
            print(e)

    @classmethod
    def update(cls):
        if cls.books:
            try:
                sn=int(input("Enter book symbool no.(sn): "))
                b=[*cls.books.keys()][sn-1]
            except Exception as e:
                print(e)
            book=cls.books[b]
            name=str(input("Enter name of book: ")).strip()
            if name:
                book.book_name=name
                cls.books.update({b:book})
                print(cls.books)


    




