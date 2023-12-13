import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

DEFAULT_PLOT_DIR = '/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source/lab8/plots'

class DataVisualizer:
    def __init__(self, data_file_path, save_dir=DEFAULT_PLOT_DIR):
        self.data = pd.read_csv(data_file_path)
        self.save_dir = save_dir 
        
    def plot_ratings_distribution(self):
        """Plot ratings distribution"""
        sns.countplot(x='Book-Rating', data=self.data)
        plt.title('Distribution of Book Ratings')
        plt.savefig(os.path.join(self.save_dir, 'book_ratings_distribution.png'))
        plt.close()
        
    def plot_publication_year_distribution(self):
        """Plot publication year distribution"""
        yearly_ratings = self.data.groupby('Year-Of-Publication')['Book-Rating'].mean()
        plt.figure(figsize=(10, 6))
        plt.xlim(1800, 2020)
        yearly_ratings.plot()
        plt.title('Average Ratings per Year of Publication')
        plt.xlabel('Year of Publication')
        plt.ylabel('Average Rating')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'ratings_per_year_line.png'))
        plt.close()
    
    def plot_user_age_distribution(self):
        """Plot user age distribution"""
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data['Age'].dropna(), bins=50, kde=False)
        plt.title('User Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.xlim(0, 100)
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'user_age_distribution_adjusted.png'))
        plt.close()
        
    def plot_ratings_by_top_publishers(self):
        """Plot ratings by top publishers"""
        top_publishers = self.data['Publisher'].value_counts().head(10).index
        publisher_ratings = self.data[self.data['Publisher'].isin(top_publishers)].groupby('Publisher')['Book-Rating'].mean()
        plt.figure(figsize=(10, 6))
        publisher_ratings.plot(kind='bar')
        plt.title('Average Ratings of Top Publishers')
        plt.ylabel('Average Rating')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'ratings_by_top_publishers.png'))
        plt.close()
        
    def plot_books_published_each_year(self):
        """Plot books published each year"""
        books_per_year = self.data['Year-Of-Publication'].value_counts().sort_index()
        plt.figure(figsize=(10, 6))
        books_per_year.plot()
        plt.title('Number of Books Published Each Year')
        plt.xlabel('Year of Publication')
        plt.ylabel('Number of Books')
        plt.xlim(1950, 2020)
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'books_published_each_year.png'))
        plt.close()
        
    def plot_book_counts_by_authors(self):
        """Plot book counts by authors"""
        books_by_author = self.data['Book-Author'].value_counts()
        plt.figure(figsize=(10, 6))
        sns.histplot(books_by_author, bins=10000, kde=False)
        plt.title('Distribution of Book Counts by Authors')
        plt.xlabel('Number of Books')
        plt.ylabel('Count of Authors')
        plt.xlim(0, 20)
        plt.xticks(np.arange(0, 20, 1))
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'book_counts_by_authors.png'))
        plt.close()
        
    def plot_average_rating_by_age_group(self):
        """Plot average rating by age group"""
        self.data['Age Group'] = pd.cut(self.data['Age'], bins=[0, 18, 30, 50, 100], labels=['0-18', '19-30', '31-50', '51-100'])
        age_rating = self.data.groupby('Age Group')['Book-Rating'].mean()
        plt.figure(figsize=(10, 6))
        age_rating.plot(kind='bar')
        plt.title('Average Rating by Age Group')
        plt.ylabel('Average Rating')
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'average_rating_by_age_group.png'))
        plt.close()
        
    def plot_heatmap_age_year_ratings(self):
        """Plot heatmap of ratings by age and year of publication"""
        pivot_table = self.data.pivot_table(values='Book-Rating', index='Age', columns='Year-Of-Publication', aggfunc='mean')
        plt.figure(figsize=(12, 8))
        sns.heatmap(pivot_table, cmap='coolwarm', annot=True)
        plt.title('Heatmap of Ratings by Age and Year of Publication')
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'heatmap_age_year_ratings.png'))
        plt.close()
        
    def plot_lineplot_avg_ratings_over_years(self):
        """Plot line plot of average ratings over years"""
        avg_ratings_over_years = self.data.groupby('Year-Of-Publication')['Book-Rating'].mean()
        plt.figure(figsize=(12, 6))
        avg_ratings_over_years.plot()
        plt.title('Average Ratings Over Years')
        plt.xlabel('Year of Publication')
        plt.ylabel('Average Rating')
        plt.xlim(1800, 2020)
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'lineplot_avg_ratings_over_years.png'))
        plt.close()
        
    def plot_piechart_books_by_top_authors(self):
        """Plot pie chart of books by top authors"""
        top_authors = self.data['Book-Author'].value_counts().head(5)  # Taking the top 5 authors
        plt.figure(figsize=(8, 8))
        top_authors.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Distribution of Books by Top Authors')
        plt.ylabel('')  # Hide the y-label
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'piechart_books_by_top_authors.png'))
        plt.close()

    def plot_ratings_per_year_line(self):
        """Plot ratings per year line"""
        yearly_ratings = self.data.groupby('Year-Of-Publication')['Book-Rating'].mean()
        plt.figure(figsize=(10, 6))
        plt.xlim(1800, 2020)
        yearly_ratings.plot()
        plt.title('Average Ratings per Year of Publication')
        plt.xlabel('Year of Publication')
        plt.ylabel('Average Rating')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'ratings_per_year_line.png'))
        plt.close()
        
    def plot_subplots(self):
        """Create a figure and a set of subplots"""
        df = self.data  
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))

        # Subplot 1: Box Plot of Ratings by Top 5 Publishers
        top_publishers = df['Publisher'].value_counts().head(5).index
        sns.boxplot(x='Publisher', y='Book-Rating', data=df[df['Publisher'].isin(top_publishers)], ax=axs[0, 0])
        axs[0, 0].set_title('Ratings by Top 5 Publishers')
        axs[0, 0].set_xticklabels(axs[0, 0].get_xticklabels(), rotation=45)

        # Subplot 2: Scatter Plot of Book Ratings vs. Publication Year
        sns.scatterplot(x='Year-Of-Publication', y='Book-Rating', data=df, ax=axs[0, 1])
        axs[0, 1].set_xlim(1900, 2020)
        axs[0, 1].set_title('Book Ratings vs. Publication Year')

        # Subplot 3: Line Plot of Number of Books Published Each Year (Last 200 Years)
        books_per_year = df['Year-Of-Publication'].value_counts().sort_index()
        axs[1, 0].plot(books_per_year)
        axs[1, 0].set_xlim(1800, 2020)
        axs[1, 0].set_title('Number of Books Published Each Year (Last 200 Years)')
        axs[1, 0].set_xlabel('Year of Publication')
        axs[1, 0].set_ylabel('Number of Books')

        # Subplot 4: Pie Chart of Book Counts by Top 5 Authors
        top_authors = df['Book-Author'].value_counts().head(5)
        axs[1, 1].pie(top_authors, labels=top_authors.index, autopct='%1.1f%%')
        axs[1, 1].set_title('Book Counts by Top 5 Authors')

        plt.tight_layout()
        plt.savefig(os.path.join(self.save_dir, 'different_subplots.png'))
        plt.close()
        
    def visualize_data(self):
        """Visualize data"""
        self.plot_ratings_distribution()
        self.plot_publication_year_distribution()
        self.plot_user_age_distribution()
        self.plot_ratings_by_top_publishers()
        self.plot_books_published_each_year()
        self.plot_book_counts_by_authors()
        self.plot_average_rating_by_age_group()
        self.plot_heatmap_age_year_ratings()
        self.plot_lineplot_avg_ratings_over_years()
        self.plot_piechart_books_by_top_authors()
        self.plot_ratings_per_year_line()
        self.plot_subplots()
        
    