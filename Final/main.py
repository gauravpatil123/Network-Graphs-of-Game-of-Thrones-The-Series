"""
Documentation
"""

import csv
from join_edges import JoinEdges as JE

# GLOBAL VARIABLES
SERIES_S01_EDGES_FILE_PATH = "data/networkofthrones/series/got-s1-edges.csv"
SERIES_S02_EDGES_FILE_PATH = "data/networkofthrones/series/got-s2-edges.csv"
SERIES_S03_EDGES_FILE_PATH = "data/networkofthrones/series/got-s3-edges.csv"
SERIES_S04_EDGES_FILE_PATH = "data/networkofthrones/series/got-s4-edges.csv"
SERIES_S05_EDGES_FILE_PATH = "data/networkofthrones/series/got-s5-edges.csv"
SERIES_S06_EDGES_FILE_PATH = "data/networkofthrones/series/got-s6-edges.csv"
SERIES_S07_EDGES_FILE_PATH = "data/networkofthrones/series/got-s7-edges.csv"
SERIES_S08_EDGES_FILE_PATH = "data/networkofthrones/series/got-s8-edges.csv"
SERIES_EDGES_FILE_PATH_LIST = [SERIES_S01_EDGES_FILE_PATH, SERIES_S02_EDGES_FILE_PATH, SERIES_S03_EDGES_FILE_PATH, SERIES_S04_EDGES_FILE_PATH, SERIES_S05_EDGES_FILE_PATH, SERIES_S06_EDGES_FILE_PATH, SERIES_S07_EDGES_FILE_PATH, SERIES_S08_EDGES_FILE_PATH]
SERIES_FIELD_INDICES = [0, 1, 2, 3]
SAVE_DATA_PATH_SERIES = "data/constructed/series/"

BOOKS_B01_EDGES_FILE_PATH = "data/networkofthrones/books/asoiaf-book1-edges.csv"
BOOKS_B02_EDGES_FILE_PATH = "data/networkofthrones/books/asoiaf-book2-edges.csv"
BOOKS_B03_EDGES_FILE_PATH = "data/networkofthrones/books/asoiaf-book3-edges.csv"
BOOKS_B04_EDGES_FILE_PATH = "data/networkofthrones/books/asoiaf-book4-edges.csv"
BOOKS_B05_EDGES_FILE_PATH = "data/networkofthrones/books/asoiaf-book5-edges.csv"
BOOKS_EDGES_FILE_PATH_LIST = [BOOKS_B01_EDGES_FILE_PATH, BOOKS_B02_EDGES_FILE_PATH, BOOKS_B03_EDGES_FILE_PATH, BOOKS_B04_EDGES_FILE_PATH, BOOKS_B05_EDGES_FILE_PATH]
BOOKS_FIELD_INDICES = [0, 1, 3 , 4]
SAVE_DATA_PATH_BOOKS = "data/constructed/books/"

# UTILITY FUNCTIONS
def cumulative_list(end_number, list):
    """
    """
    out_list = []
    for i in range(end_number):
        out_list.append(list[i])
    return out_list

if __name__=="__main__":
    
    """
    SERIES
    """

    # SEASON 1 CUMULATIVE EDGES DATA
    season_1_cumulative_file_path_list = cumulative_list(1, SERIES_EDGES_FILE_PATH_LIST)
    season_1_cumulative_edges = JE(SERIES_FIELD_INDICES, season_1_cumulative_file_path_list)
    season_1_cumulative_edges()
    filename = "got_s1_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_SERIES + filename
    season_1_cumulative_edges.save(filepath)
    
    # SEASON 2 CUMULATIVE EDGES DATA
    season_2_cumulative_file_path_list = cumulative_list(2, SERIES_EDGES_FILE_PATH_LIST)
    season_2_cumulative_edges = JE(SERIES_FIELD_INDICES, season_2_cumulative_file_path_list)
    season_2_cumulative_edges()
    filename = "got_s2_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_SERIES + filename
    season_2_cumulative_edges.save(filepath)
    
    # SEASON 3 CUMULATIVE EDGES DATA
    season_3_cumulative_file_path_list = cumulative_list(3, SERIES_EDGES_FILE_PATH_LIST)
    season_3_cumulative_edges = JE(SERIES_FIELD_INDICES, season_3_cumulative_file_path_list)
    season_3_cumulative_edges()
    filename = "got_s3_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_SERIES + filename
    season_3_cumulative_edges.save(filepath)
    
    # SEASON 4 CUMULATIVE EDGES DATA
    season_4_cumulative_file_path_list = cumulative_list(4, SERIES_EDGES_FILE_PATH_LIST)
    season_4_cumulative_edges = JE(SERIES_FIELD_INDICES, season_4_cumulative_file_path_list)
    season_4_cumulative_edges()
    filename = "got_s4_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_SERIES + filename
    season_4_cumulative_edges.save(filepath)
    
    # SEASON 5 CUMULATIVE EDGES DATA
    season_5_cumulative_file_path_list = cumulative_list(5, SERIES_EDGES_FILE_PATH_LIST)
    season_5_cumulative_edges = JE(SERIES_FIELD_INDICES, season_5_cumulative_file_path_list)
    season_5_cumulative_edges()
    filename = "got_s5_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_SERIES + filename
    season_5_cumulative_edges.save(filepath)
    
    # SEASON 6 CUMULATIVE EDGES DATA
    season_6_cumulative_file_path_list = cumulative_list(6, SERIES_EDGES_FILE_PATH_LIST)
    season_6_cumulative_edges = JE(SERIES_FIELD_INDICES, season_6_cumulative_file_path_list)
    season_6_cumulative_edges()
    filename = "got_s6_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_SERIES + filename
    season_6_cumulative_edges.save(filepath)
    
    # SEASON 7 CUMULATIVE EDGES DATA
    season_7_cumulative_file_path_list = cumulative_list(7, SERIES_EDGES_FILE_PATH_LIST)
    season_7_cumulative_edges = JE(SERIES_FIELD_INDICES, season_7_cumulative_file_path_list)
    season_7_cumulative_edges()
    filename = "got_s7_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_SERIES + filename
    season_7_cumulative_edges.save(filepath)
    
    # SEASON 8 CUMULATIVE EDGES DATA
    season_8_cumulative_file_path_list = cumulative_list(8, SERIES_EDGES_FILE_PATH_LIST)
    season_8_cumulative_edges = JE(SERIES_FIELD_INDICES, season_8_cumulative_file_path_list)
    season_8_cumulative_edges()
    filename = "got_s8_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_SERIES + filename
    season_8_cumulative_edges.save(filepath)

    """
    BOOKS
    """

    # BOOK 1 CUMULATIVE EDGES DATA
    book_1_cumulative_file_path_list = cumulative_list(1, BOOKS_EDGES_FILE_PATH_LIST)
    book_1_cumulative_edges = JE(BOOKS_FIELD_INDICES, book_1_cumulative_file_path_list)
    book_1_cumulative_edges()
    filename = "got_b1_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_BOOKS + filename
    book_1_cumulative_edges.save(filepath)

    # BOOK 2 CUMULATIVE EDGES DATA
    book_2_cumulative_file_path_list = cumulative_list(2, BOOKS_EDGES_FILE_PATH_LIST)
    book_2_cumulative_edges = JE(BOOKS_FIELD_INDICES, book_2_cumulative_file_path_list)
    book_2_cumulative_edges()
    filename = "got_b2_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_BOOKS + filename
    book_2_cumulative_edges.save(filepath)

    # BOOK 3 CUMULATIVE EDGES DATA
    book_3_cumulative_file_path_list = cumulative_list(3, BOOKS_EDGES_FILE_PATH_LIST)
    book_3_cumulative_edges = JE(BOOKS_FIELD_INDICES, book_3_cumulative_file_path_list)
    book_3_cumulative_edges()
    filename = "got_b3_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_BOOKS + filename
    book_3_cumulative_edges.save(filepath)

    # BOOK 4 CUMULATIVE EDGES DATA
    book_4_cumulative_file_path_list = cumulative_list(4, BOOKS_EDGES_FILE_PATH_LIST)
    book_4_cumulative_edges = JE(BOOKS_FIELD_INDICES, book_4_cumulative_file_path_list)
    book_4_cumulative_edges()
    filename = "got_b4_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_BOOKS + filename
    book_4_cumulative_edges.save(filepath)

    # BOOK 5 CUMULATIVE EDGES DATA
    book_5_cumulative_file_path_list = cumulative_list(5, BOOKS_EDGES_FILE_PATH_LIST)
    book_5_cumulative_edges = JE(BOOKS_FIELD_INDICES, book_5_cumulative_file_path_list)
    book_5_cumulative_edges()
    filename = "got_b5_sigma_edges.csv"
    filepath = SAVE_DATA_PATH_BOOKS + filename
    book_5_cumulative_edges.save(filepath)



    