import csv

#Global Variables
DATA = {}
NODES_FIELDNAMES = ["ID", "Label"]
SEASON_1_NODES_FILE_PATH = "gameofthrones-master/data/got-s1-nodes.csv"
SEASON_2_NODES_FILE_PATH = "gameofthrones-master/data/got-s2-nodes.csv"
SEASON_3_NODES_FILE_PATH = "gameofthrones-master/data/got-s3-nodes.csv"
SEASON_4_NODES_FILE_PATH = "gameofthrones-master/data/got-s4-nodes.csv"
SEASON_5_NODES_FILE_PATH = "gameofthrones-master/data/got-s5-nodes.csv"
SEASON_6_NODES_FILE_PATH = "gameofthrones-master/data/got-s6-nodes.csv"
SEASON_7_NODES_FILE_PATH = "gameofthrones-master/data/got-s7-nodes.csv"
SEASON_8_NODES_FILE_PATH = "gameofthrones-master/data/got-s8-nodes.csv"


def add_nodes_to_data(DATA, nodes_file_path):
    """
    """
    with open(nodes_file_path, "r") as file_handle:
        reader = csv.DictReader(file_handle, delimiter=",")
        headers = reader.fieldnames
        headers = list(headers)
        id_header = headers[0]
        label_header = headers[1]

        for row in reader:
            id = row[id_header]
            label = row[label_header]

            if id not in DATA:
                DATA[id] = label

def make_nodes_csv(DATA):
    """
    """
    data = [] #fieldnames = [id, label]
    for k in DATA:
        id  = k
        label = DATA[k]
        row = [id] + [label]
        data.append(row)
    return data

def save_nodes_csv(fieldnames, rows, file_name):
    """
    """
    with open(file_name, "w") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(fieldnames)
        csvwriter.writerows(rows)


if __name__=="__main__":
    add_nodes_to_data(DATA, SEASON_1_NODES_FILE_PATH)
    add_nodes_to_data(DATA, SEASON_2_NODES_FILE_PATH)
    add_nodes_to_data(DATA, SEASON_3_NODES_FILE_PATH)
    add_nodes_to_data(DATA, SEASON_4_NODES_FILE_PATH)
    add_nodes_to_data(DATA, SEASON_5_NODES_FILE_PATH)
    add_nodes_to_data(DATA, SEASON_6_NODES_FILE_PATH)
    add_nodes_to_data(DATA, SEASON_7_NODES_FILE_PATH)
    add_nodes_to_data(DATA, SEASON_8_NODES_FILE_PATH)

    csv_data = make_nodes_csv(DATA)

    save_nodes_csv(NODES_FIELDNAMES, csv_data, "S_1-8_nodes.csv")
