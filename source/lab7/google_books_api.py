import google_auth_oauthlib.flow
import google.auth.transport.requests

CREDENTIALS = '/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source/lab7/credentials.json'

def get_credentials():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS,
        scopes=['https://www.googleapis.com/auth/books']
    )
    flow.run_local_server(port=0)
    return flow.credentials

def search_books_by_title(credentials, title_query):
    session = google.auth.transport.requests.AuthorizedSession(credentials)
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": title_query}
    response = session.get(url, params=params)
    return response.json().get('items', [])

def display_book_titles(books):
    print("\nBook Titles:")
    for book in books:
        title = book.get('volumeInfo', {}).get('title', 'N/A')
        print(title)

def display_book_authors(books):
    print("\nBook Authors:")
    for book in books:
        authors = ', '.join(book.get('volumeInfo', {}).get('authors', []))
        print(authors if authors else "N/A")

def display_book_publishers(books):
    print("\nPublishers:")
    for book in books:
        publisher = book.get('volumeInfo', {}).get('publisher', 'N/A')
        print(publisher)

def display_book_publication_dates(books):
    print("\nPublication Dates:")
    for book in books:
        published_date = book.get('volumeInfo', {}).get('publishedDate', 'N/A')
        print(published_date)

def display_book_categories(books):
    print("\nCategories:")
    for book in books:
        categories = ', '.join(book.get('volumeInfo', {}).get('categories', []))
        print(categories)

def display_book_average_ratings(books):
    print("\nAverage Ratings:")
    for book in books:
        average_rating = book.get('volumeInfo', {}).get('averageRating', 'N/A')
        print(average_rating)

def search_books_by_author(credentials, author_query):
    session = google.auth.transport.requests.AuthorizedSession(credentials)
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"inauthor:{author_query}"}
    response = session.get(url, params=params)
    return response.json().get('items', [])

def display_books_info(books):
    for book in books:
        volume_info = book.get('volumeInfo', {})
        print("\n-----------------------------")
        print("Title:", volume_info.get('title', 'N/A'))
        print("Authors:", ', '.join(volume_info.get('authors', [])))
        print("Publisher:", volume_info.get('publisher', 'N/A'))
        print("Published Date:", volume_info.get('publishedDate', 'N/A'))
        print("Categories:", ', '.join(volume_info.get('categories', [])))
        print("Average Rating:", volume_info.get('averageRating', 'N/A'))
        print("Description:", volume_info.get('description', 'N/A'))
        print("-----------------------------\n")
