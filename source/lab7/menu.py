from google_books_api import *
#from api_funcs import *
from display_funcs import *
# def menu():
#     credentials = get_credentials()
#     while True:
#         print("\nBOOK SEARCH MENU")
#         print("Options:")
#         print("1. Search by Title and Display Titles")
#         print("2. Display Authors")
#         print("3. Display Publishers")
#         print("4. Display Publication Dates")
#         print("5. Display Categories")
#         print("6. Display Average Ratings")
#         print("0. Exit")

#         choice = input("Enter option: ")
#         if choice == '0':
#             break

#         title_query = input("Enter book title to search: ")
#         books = search_books_by_title(credentials, title_query)

#         if choice == '1':
#             display_book_titles(books)
#         elif choice == '2':
#             display_book_authors(books)
#         elif choice == '3':
#             display_book_publishers(books)
#         elif choice == '4':
#             display_book_publication_dates(books)
#         elif choice == '5':
#             display_book_categories(books)
#         elif choice == '6':
#             display_book_average_ratings(books)
#         elif choice == '7':
#             author_query = input("Enter author name to search: ")
#             books = search_books_by_author(credentials, author_query)
#             display_books_info(books)
#         else:
#             print("Invalid option")

def menu2():
    credentials = get_credentials()
    while True:
        #using api_funcs.py
        print("\nBOOK SEARCH MENU")
        print("Options:")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Display Books by ISBN")
        print("4. Display Popular books in category")
        print("0. Exit")
        
        choice = input("Enter option: ")
        if choice == '0':
            break
        
        if choice == '1':
            #print(search_books_by_title(credentials, input("Enter book title to search: ")))
            #display_search_results(search_books_by_title(credentials, input("Enter book title to search: ")), "book")
            display_book_details(credentials, input("Enter book title to search: "))
        elif choice == '2':
            #print(search_books_by_author(credentials, input("Enter author name to search: ")))
            #display_search_results(search_books_by_author(credentials, input("Enter author name to search: ")), "book")
            display_books_by_author(credentials, input("Enter author name to search: "))
        elif choice == '3':
            #print(search_books_by_author(credentials, input("Enter author name to search: ")))
            #display_search_results(search_books_by_author(credentials, input("Enter author name to search: ")), "book")
            display_books_by_isbn(credentials, input("Enter ISBN to search: "))
        elif choice == '4':
            #print(list_new_releases(credentials, input("Enter category to search: ")))
            #display_search_results(list_new_releases(credentials, input("Enter category to search: ")), "book")
            display_new_releases(credentials, input("Enter category to search: "))
        