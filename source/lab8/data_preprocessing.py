import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataPreprocessor:
    def __init__(self, BOOKS_FILE_PATH, RATINGS_FILE_PATH, USERS_FILE_PATH):
        self.books = pd.read_csv(BOOKS_FILE_PATH)
        self.ratings = pd.read_csv(RATINGS_FILE_PATH)
        self.users = pd.read_csv(USERS_FILE_PATH)
        self.books_ratings = None
        self.books_ratings_users = None
    
    def get_extreme_values(self):
        """Get extreme values of data"""
        for column in self.books_ratings_users.columns:
            if self.books_ratings_users[column].dtype == 'object':
                continue
            min_value = self.books_ratings_users[column].min()
            max_value = self.books_ratings_users[column].max()
            median = self.books_ratings_users[column].median()
            print(f"Column: {column}, min: {min_value}, max: {max_value}, median: {median}")
    
    def remove_year_of_publication_with_string_value(self):
        """Remove year of publication with string value"""
        temp = (self.books['Year-Of-Publication'] == 'DK Publishing Inc') | (self.books['Year-Of-Publication'] == 'Gallimard')
        self.books = self.books.drop(self.books[temp].index)
        self.books[(self.books['Year-Of-Publication'] == 'DK Publishing Inc') | (self.books['Year-Of-Publication'] == 'Gallimard')]
    
    def convert_year_of_publication_to_int(self):
        """Convert year of publication to int"""
        self.books['Year-Of-Publication'] = self.books['Year-Of-Publication'].astype(int)
    
    def remove_image_url_column(self):
        """Removing Image-URL column of all sizes"""
        self.books.drop(labels=['Image-URL-S', 'Image-URL-M', 'Image-URL-L'], axis=1, inplace=True)
        
    def get_number_of_unique_values(self):
        """Get number of unique values"""
        print("Number of Book ISBN numbers:", len(self.books['ISBN'].unique()))
        print("Number of book titles:", len(self.books['Book-Title'].unique()))
        print('Number of book authors:', len(self.books['Book-Author'].unique()))
        print('Number of Publication Years:', len(self.books['Year-Of-Publication'].unique()))
        print('Number of publisher names:', len(self.books['Publisher'].unique()))
        
    def merge_books_ratings_users(self):
        """Merge books, ratings, and users data"""
        self.merge_books_ratings()
        self.books_ratings_users = pd.merge(self.books_ratings, self.users, on='User-ID').dropna()
    
    def merge_books_ratings(self):
        """Merge books and ratings data"""
        self.books_ratings = pd.merge(self.books, self.ratings, on='ISBN', how='left').dropna()
        
    def drop_nan_values(self):
        """Drop NaN values"""
        self.books.dropna()
        self.ratings.dropna()
        self.users.dropna()
    
    def preprocess_data(self, clean_data_file_path):
        """Preprocess data"""
        try:
            self.remove_year_of_publication_with_string_value()
            self.convert_year_of_publication_to_int()
            self.remove_image_url_column()
            self.drop_nan_values()
            self.merge_books_ratings()
            self.merge_books_ratings_users()
            self.books_ratings_users.to_csv(clean_data_file_path, index=False)
            self.get_number_of_unique_values()
            self.get_extreme_values()
        except Exception as e:
            print(f"An error occurred during data preprocessing: {str(e)}")
