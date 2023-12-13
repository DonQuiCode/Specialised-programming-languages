from prettytable import PrettyTable
from api_funcs import *

# def display_data(data, field_names, entity_name):
#     if not data:
#         print(f"No {entity_name} data to display")
#         return None

#     table = PrettyTable()
#     table.field_names = field_names
#     for idx, item in enumerate(data, start=1):
#         # Assuming the title is stored under item['volumeInfo']['title']
#         title = item.get('volumeInfo', {}).get('title', 'N/A')
#         table.add_row([idx, title])
#     print(f"{entity_name.capitalize()} data:")
#     print(table)



# def display_data(data, field_names, entity_name):
#     if not data:
#         print(f"No {entity_name} data to display")
#         return None

#     table = PrettyTable()
#     table.field_names = field_names
#     for idx, item in enumerate(data, start=1):
#         row = [idx]
#         for field in field_names[1:]:  # Skip the first field (#), as it's the index
#             if field.lower() in ['title', 'author(s)', 'published date']:
#                 value = item.get('volumeInfo', {}).get(field.capitalize(), 'N/A')
#             elif field.lower() == 'isbn':
#                 isbn = ', '.join([identifier.get('identifier') for identifier in item.get('volumeInfo', {}).get('industryIdentifiers', []) if identifier.get('type') in ['ISBN_10', 'ISBN_13']])
#                 value = isbn or 'N/A'
#             else:
#                 value = item.get(field, 'N/A')
#             row.append(value)
#         table.add_row(row)

#     print(f"{entity_name.capitalize()} data:")
#     print(table)

def display_data(data, field_names, entity_name):
    if not data:
        print(f"No {entity_name} data to display")
        return None

    table = PrettyTable()
    table.field_names = field_names

    for idx, item in enumerate(data, start=1):
        book_info = item.get('volumeInfo', {})
        row = [idx]

        for field in field_names[1:]:  # Skip the index column
            if field == "Title":
                title = book_info.get('title', 'N/A')
                row.append(title)
            elif field == "Author(s)":
                authors = ', '.join(book_info.get('authors', ['Unknown']))
                row.append(authors)
            elif field == "Published Date":
                published_date = book_info.get('publishedDate', 'N/A')
                row.append(published_date)
            elif field == "ISBN":
                isbn = ', '.join([identifier.get('identifier') for identifier in book_info.get('industryIdentifiers', []) if identifier.get('type') in ['ISBN_10', 'ISBN_13']])
                row.append(isbn or 'N/A')
            else:
                row.append('N/A')

        table.add_row(row)

    print(f"{entity_name.capitalize()} data:")
    print(table)

# def display_book_details(credentials, title_query):
#     books = search_books_by_title(credentials, title_query)
#     field_names = ["#", "Title"]
#     display_data(books, field_names, "book")
def display_book_details(credentials, title_query):
    books = search_books_by_title(credentials, title_query)
    field_names = ["#", "Title", "Author(s)", "Page Count", "Categories", "Language"]
    display_data(books, field_names, "book")

def display_books_by_author(credentials, author_query):
    books = search_books_by_author(credentials, author_query)
    field_names = ["#", "Title", "Author(s)", "Published Date", "ISBN"]
    display_data(books, field_names, "books by author")

def display_books_by_isbn(credentials, isbn_query):
    books = search_books_by_isbn(credentials, isbn_query)
    field_names = ["#", "Title", "Author(s)", "Published Date"]
    display_data(books, field_names, "books by ISBN")

def display_new_releases(credentials, category="fiction", max_results=10):
    books = list_new_releases(credentials, category, max_results)
    field_names = ["#", "Title", "Author(s)", "Published Date"]
    display_data(books, field_names, "new releases")

def display_popular_books_in_category(credentials, category, max_results=10):
    books = get_popular_books_in_category(credentials, category, max_results)
    field_names = ["#", "Title", "Author(s)", "Published Date"]
    display_data(books, field_names, "popular books in category")
