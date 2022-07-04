import csv

#Global Variables
DATA = []
EDGES_FIELDNAMES = ["Source", "Target", "Weight"]
SEASON_1_EDGES_FILE_PATH = "gameofthrones-master/data/got-s1-edges.csv"
SEASON_2_EDGES_FILE_PATH = "gameofthrones-master/data/got-s2-edges.csv"
SEASON_3_EDGES_FILE_PATH = "gameofthrones-master/data/got-s3-edges.csv"
SEASON_4_EDGES_FILE_PATH = "gameofthrones-master/data/got-s4-edges.csv"
SEASON_5_EDGES_FILE_PATH = "gameofthrones-master/data/got-s5-edges.csv"
SEASON_6_EDGES_FILE_PATH = "gameofthrones-master/data/got-s6-edges.csv"
SEASON_7_EDGES_FILE_PATH = "gameofthrones-master/data/got-s7-edges.csv"
SEASON_8_EDGES_FILE_PATH = "gameofthrones-master/data/got-s8-edges.csv"

def add_edges_to_data(DATA, edges_file_path):
    """
    """
    with open(edges_file_path, "r") as file_handle:
        reader = csv.DictReader(file_handle, delimiter=",")
        headers = reader.fieldnames
        headers = list(headers)
        source_header = headers[0]
        target_header = headers[1]
        weight_header = headers[2]

        for row in reader:
            source = row[source_header]
            target = row[target_header]
            weight = row[weight_header]
            data = [source] + [target] + [weight]
            DATA.append(data)

def save_edges_csv(fieldnames, rows, filename):
    """
    """
    with open(filename, "w") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(fieldnames)
        csvwriter.writerows(rows)


if __name__=="__main__":
    add_edges_to_data(DATA, SEASON_1_EDGES_FILE_PATH)
    add_edges_to_data(DATA, SEASON_2_EDGES_FILE_PATH)
    add_edges_to_data(DATA, SEASON_3_EDGES_FILE_PATH)
    add_edges_to_data(DATA, SEASON_4_EDGES_FILE_PATH)
    add_edges_to_data(DATA, SEASON_5_EDGES_FILE_PATH)
    add_edges_to_data(DATA, SEASON_6_EDGES_FILE_PATH)
    add_edges_to_data(DATA, SEASON_7_EDGES_FILE_PATH)
    add_edges_to_data(DATA, SEASON_8_EDGES_FILE_PATH)

    save_edges_csv(EDGES_FIELDNAMES, DATA, "S_1-8_edges.csv")