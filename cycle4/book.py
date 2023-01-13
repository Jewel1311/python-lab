class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("\n*********************\nBook Details\n*********************")
        print("Publisher Name : ",self.name)


class Book(Publisher):
    def __init__(self, title, author, name):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title : ",self.title)
        print("Author : ",self.author)


class Python(Book):
    def __init__(self, name, title, author, prize, pages):
        super().__init__(title, author, name)
        self.prize = prize
        self.pages = pages

    def display(self):
        super().display()
        print("Prize : ",self.prize)
        print("No of pages : ",self.pages)

name = input("Enter the publisher : ")
title = input("Enter the title : ")
author = input("Author name : ")
prize = int(input("Enter prize : "))
page = int(input("Enter no.of pages : "))

ob = Python(name, title, author, prize, page)
ob.display()
