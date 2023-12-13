from data_preprocessing import DataPreprocessor
from data_visualization import DataVisualizer
import warnings

# Filter out UserWarnings related to figure layout changes
warnings.filterwarnings("ignore", category=Warning)

BOOKS_FILE_PATH = '/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source/lab8/data/Books.csv'
RATINGS_FILE_PATH = '/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source/lab8/data/Ratings.csv'
USERS_FILE_PATH = '/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source/lab8/data/Users.csv'
CLEAN_DATA_FILE_PATH = '/Users/admin/Desktop/lpnu/5 сем/Specialised programming languages/source/lab8/data/clean_data.csv'

def main():
    try:
        data_preprocessor = DataPreprocessor(BOOKS_FILE_PATH, RATINGS_FILE_PATH, USERS_FILE_PATH)
        data_preprocessor.preprocess_data(CLEAN_DATA_FILE_PATH)
        
        data_visualizer = DataVisualizer(CLEAN_DATA_FILE_PATH)
        data_visualizer.visualize_data()
        
    except FileNotFoundError:
        print(f"Error: The specified CSV file does not exist.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()