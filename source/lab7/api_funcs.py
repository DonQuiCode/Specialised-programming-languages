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

# This function might need adjustments based on API capabilities
def list_categories(credentials):
    session = google.auth.transport.requests.AuthorizedSession(credentials)
    url = "https://www.googleapis.com/books/v1/categories"
    response = session.get(url)
    return response.json().get('items', [])

def search_books_by_author(credentials, author_query):
    session = google.auth.transport.requests.AuthorizedSession(credentials)
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"inauthor:{author_query}"}
    response = session.get(url, params=params)
    return response.json().get('items', [])

def search_books_by_isbn(credentials, isbn_query):
    session = google.auth.transport.requests.AuthorizedSession(credentials)
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"isbn:{isbn_query}"}
    response = session.get(url, params=params)
    return response.json().get('items', [])

def list_new_releases(credentials, category="fiction", max_results=10):
    session = google.auth.transport.requests.AuthorizedSession(credentials)
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"subject:{category}", "orderBy": "newest", "maxResults": max_results}
    response = session.get(url, params=params)
    return response.json().get('items', [])

def get_popular_books_in_category(credentials, category, max_results=10):
    session = google.auth.transport.requests.AuthorizedSession(credentials)
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": f"subject:{category}", "orderBy": "relevance", "maxResults": max_results}
    response = session.get(url, params=params)
    return response.json().get('items', [])


