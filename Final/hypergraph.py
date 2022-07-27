import csv

#Global Variables
CLUSTER_IDS = {}
CLUSTER_NODES_COUNT = {}
CLASS_EDGES_DATA = []
CLASS_NODES_DATA = []
MODULARITY_SERIES_PATH = "data/modularity data/series/"
MODULARITY_BOOKS_PATH = "data/modularity data/books/"
HYPERGRAPH_SERIES_PATH = "data/hypergraph data/series/"
HYPERGRAPH_BOOKS_PATH = "data/hypergraph data/books/"

# UTILITY FUNCTIONS

def refresh():
    """
    """
    global CLUSTER_IDS, CLUSTER_NODES_COUNT, CLASS_EDGES_DATA, CLASS_NODES_DATA
    CLUSTER_IDS = {}
    CLUSTER_NODES_COUNT = {}
    CLASS_EDGES_DATA = []
    CLASS_NODES_DATA = []

def assign_id_clusters(dict, cluster_nodes_file):
    """
    """
    with open(cluster_nodes_file, "r") as file_handle:
        reader = csv.DictReader(file_handle, delimiter=",")
        headers = reader.fieldnames
        headers = list(headers)
        id_header = headers[0]
        modularity_class = headers[-1]

        for row in reader:
            id = row[id_header]
            cluster = row[modularity_class]

            if id not in dict:
                dict[id] = cluster

def convert_edges_to_hypergraph_edges(cluster_edges_filename, cluster_ids, class_edges_data, save_filename):
    """
    """
    with open(cluster_edges_filename, "r") as file_handle:
        reader = csv.DictReader(file_handle, delimiter=",")
        headers = reader.fieldnames
        headers = list(headers)
        # reference fieldnames = [Source, Target, Type, Id, Label, timeset, Weight, Season]
        source_header = headers[0]
        target_header = headers[1]
        type_header = headers[2]
        id_header = headers[3]
        label_header = headers[4]
        timeset_header = headers[5]
        weight_header = headers[6]
        season_header = headers[7]

        for row in reader:
            source = row[source_header]
            target = row[target_header]
            type_ = row[type_header]
            id = row[id_header]
            label = row[label_header]
            timeset = row[timeset_header]
            weight = row[weight_header]
            season = row[season_header]
            
            # new data = [c_source, c_target, type, id, label, timeset, weight]
            cluster_source = cluster_ids[source]
            cluster_target = cluster_ids[target]

            data = [cluster_source] + [cluster_target] + [type_] + [id] + [label] + [timeset] + [weight] + [season]
            class_edges_data.append(data)

        with open (save_filename, "w") as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(headers)
            csvwriter.writerows(class_edges_data)

def convert_nodes_to_hypergraph_nodes(cluster_nodes_filename, cluster_nodes_count, class_nodes_data, save_filename):
    """
    """
    with open(cluster_nodes_filename, "r") as file_handle:
        reader = csv.DictReader(file_handle, delimiter=",")
        headers = reader.fieldnames
        headers = list(headers)
        modulatiry_class = headers[-1]

        for row in reader:
            cluster_no = row[modulatiry_class]
            if cluster_no not in cluster_nodes_count:
                cluster_nodes_count[cluster_no] = 1
            else:
                cluster_nodes_count[cluster_no] += 1

    # hypergraph nodes fieldnames = [id, label, size]
    for k in cluster_nodes_count:
        size = cluster_nodes_count[k]
        id = k
        label = ""
        data = [id] + [label] + [size]
        class_nodes_data.append(data)
    
    hypergraph_nodes_fieldnames = ["Id", "Label", "Size"]

    with open(save_filename, "w") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(hypergraph_nodes_fieldnames)
        csvwriter.writerows(class_nodes_data)

if __name__=="__main__":

    """
    SERIES
    """

    # Season - 1
    filename_nodes = "got_s1_abs_nodes.csv"
    filename_edges = "got_s1_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_SERIES_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_SERIES_PATH + filename_edges
    hypergraph_nodes_filename = "got_s1_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_s1_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Season - 2
    filename_nodes = "got_s2_abs_nodes.csv"
    filename_edges = "got_s2_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_SERIES_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_SERIES_PATH + filename_edges
    hypergraph_nodes_filename = "got_s2_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_s2_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Season - 3
    filename_nodes = "got_s3_abs_nodes.csv"
    filename_edges = "got_s3_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_SERIES_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_SERIES_PATH + filename_edges
    hypergraph_nodes_filename = "got_s3_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_s3_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Season - 4
    filename_nodes = "got_s4_abs_nodes.csv"
    filename_edges = "got_s4_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_SERIES_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_SERIES_PATH + filename_edges
    hypergraph_nodes_filename = "got_s4_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_s4_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()
    
    # Season - 5
    filename_nodes = "got_s5_abs_nodes.csv"
    filename_edges = "got_s5_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_SERIES_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_SERIES_PATH + filename_edges
    hypergraph_nodes_filename = "got_s5_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_s5_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Season - 6
    filename_nodes = "got_s6_abs_nodes.csv"
    filename_edges = "got_s6_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_SERIES_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_SERIES_PATH + filename_edges
    hypergraph_nodes_filename = "got_s6_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_s6_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Season - 7
    filename_nodes = "got_s7_abs_nodes.csv"
    filename_edges = "got_s7_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_SERIES_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_SERIES_PATH + filename_edges
    hypergraph_nodes_filename = "got_s7_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_s7_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Season - 8
    filename_nodes = "got_s8_abs_nodes.csv"
    filename_edges = "got_s8_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_SERIES_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_SERIES_PATH + filename_edges
    hypergraph_nodes_filename = "got_s8_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_s8_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_SERIES_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    """
    BOOKS
    """

    # Book - 1
    filename_nodes = "got_b1_abs_nodes.csv"
    filename_edges = "got_b1_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_edges
    hypergraph_nodes_filename = "got_b1_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_b1_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Book - 2
    filename_nodes = "got_b2_abs_nodes.csv"
    filename_edges = "got_b2_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_edges
    hypergraph_nodes_filename = "got_b2_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_b2_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Book - 3
    filename_nodes = "got_b3_abs_nodes.csv"
    filename_edges = "got_b3_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_edges
    hypergraph_nodes_filename = "got_b3_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_b3_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Book - 4
    filename_nodes = "got_b4_abs_nodes.csv"
    filename_edges = "got_b4_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_edges
    hypergraph_nodes_filename = "got_b4_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_b4_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()

    # Book - 5
    filename_nodes = "got_b5_abs_nodes.csv"
    filename_edges = "got_b5_abs_edges.csv"
    CLUSTERED_NODES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_nodes
    CLUSTERED_EDGES_FILE_PATH = MODULARITY_BOOKS_PATH + filename_edges
    hypergraph_nodes_filename = "got_b5_abs_hypergraph_nodes.csv"
    hypergraph_edges_filename = "got_b5_abs_hypergraph_edges.csv"
    hypergraph_nodes_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_nodes_filename
    hypergraph_edges_filepath = HYPERGRAPH_BOOKS_PATH + hypergraph_edges_filename
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, hypergraph_edges_filepath)
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, hypergraph_nodes_filepath)
    refresh()
