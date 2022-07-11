

class Library:
    def __init__(self,booklist,libraryname):
        self.booklist=booklist
        self.libraryname=libraryname
        self.lendedbooks={}

    def DisplayBook(self):
        print("currently we have these following books: ")
        for books  in self.booklist:
            print(books,end=' ')

    def LendBook(self,bookname,user):
         if bookname not in self.lendedbooks.keys() :
            print("You can have this book")
            self.lendedbooks.update({bookname:user})
            self.booklist.remove(bookname)
         else:
            print(f"This book is using by {self.lendedbooks[bookname]}")

    def AddBook(self,bookname,user):
        print(f"This {bookname} is added by {user} to the library")
        self.booklist.append(bookname)

    def ReturnBook(self,bookname):
        print(f"{bookname} is returned ")
        del self.lendedbooks[bookname]
        self.booklist.append(bookname)

if __name__ == '__main__':
    biddaloy=Library(["golpo solpo","choto biggan","c++","Hacker's Handbook","penteserter land"],"biddaloy")
    while(True):
       print(f"\nWelcome to the {biddaloy.libraryname} Library")
       print("1.Display Book \n 2.Lend a Book \n 3.Add a Book \n 4.Return a Book")
       userchoice=int(input("Enter your choice"))
       if userchoice == 1:
           biddaloy.DisplayBook()

       elif userchoice == 2:
           print("Enter the book you want and your name ")
           book = input()
           username=input()

           biddaloy.LendBook(book,username)


       elif userchoice == 3:
           print("Which book you want to add . enter the name of the book and your name")
           book=input()
           username=input()
           biddaloy.AddBook(book,username)

       elif userchoice == 4:
           print("enter the name of the book you want to return ")
           bookname=input()
           biddaloy.ReturnBook(bookname)
       else:
        print("Enter a valid option")








