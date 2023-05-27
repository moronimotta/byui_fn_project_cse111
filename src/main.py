import uuid
from datetime import datetime
import mysql.connector
from receipt.controller import Controller
import os

def main():
    # connect to database
    connection = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="root",
    database="grocerystore"
    )

    if connection.is_connected():
     print("Connected to MySQL database")
    
    # main menu
    main_menu()
    
    connection.close()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_empty(value):
    if value == "":
        return True
    else:
        return False

def main_menu():
    print("Welcome to the Grocery Store")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    while choice != 3:
        if choice == 1:
            input("Enter your username: ")
            input("Enter your password: ")
            # if login successful
                # diplay logged_menu()
        elif choice == 2:
            input("Enter your username: ")
            input("Enter your password: ")
            input("Enter your email: ")
            input("Enter your name: ")
            input("Enter your phone number: ")
        else:
            print("Invalid choice")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
    print("Thank you for shopping with us")

def logged_menu():
    print("1. Shop")
    print("2. View Cart")
    print("3. Finish Shopping")

    # if user is admin
    # create product
    # delete product
    # check stock
    # Warnings - (status)


    print("4. Logout")
    choice = int(input("Enter your choice: "))
    while choice != 4:
        if choice == 1:
            shop_menu()
        elif choice == 2:
            view_cart()
        elif choice == 3:
            finish_shopping()
        else:
            print("Invalid choice")
        print("1. Shop")
        print("2. View Cart")
        print("3. Finish Shopping")
        print("4. Logout")
        choice = int(input("Enter your choice: "))

def shop_menu():
    print("1. See All Products' Categories")
    print("2. See All Products")
    print("3. Search for a Product")
    print("4. Search for a Brand")
    print("5. Go back")

    choice = int(input("Enter your choice: "))
    while choice != 5:
        if choice == 1:
            # function in controller
        elif choice == 2:
            # function in controller
        elif choice == 3:
            # function in controller
        elif choice == 4:
            # function in controller
        else:
            print("Invalid choice")
        print("1. See All Products' Categories")
        print("2. See All Products")
        print("3. Search for a Product")
        print("4. Search for a Brand")
        print("5. Go back")
        choice = int(input("Enter your choice: "))
    logged_menu()

def view_cart():
    # print all items in cart and subtotal
    print("1. Remove an item")
    print("2. Go back")
    choice = int(input("Enter your choice: "))
    while choice != 2:
        if choice == 1:
            # function in controller
        else:
            print("Invalid choice")
        print("1. Remove an item")
        print("2. Go back")
        choice = int(input("Enter your choice: "))
    logged_menu()

def finish_shopping():
    print("1. Confirm")
    print("2. Go back")
    choice = int(input("Enter your choice: "))
    while choice != 2:
        if choice == 1:
            # function in controller
            # ask user if they want the receipt
                # if yes, print receipt and also save to database
                # if no, go back to main menu
        else:
            print("Invalid choice")
        print("1. Confirm")
        print("2. Go back")
        choice = int(input("Enter your choice: "))
    logged_menu()

if __name__ == "__main__":
    main()