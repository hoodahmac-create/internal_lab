class book_details:
    def __init__(self,book_name,author_name,number_of_pages):
        self.book_name=book_name
        self.author_name=author_name
        self.number_of_pages=number_of_pages
    def display(self):
        print("The book",self.book_name,"is written by the author",self.author_name,". It has",self.number_of_pages,"pages in it")
print("Hello! Welcome to my mini library")
book1=book_details("The DaVinci Code","Dan Brown","500")
book2=book_details("The Silent Patient","Alexandro","300")
book1.display()
book2.display()

