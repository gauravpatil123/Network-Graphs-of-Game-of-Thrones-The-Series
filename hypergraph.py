import csv

#Global Variables
CLUSTER_IDS = {}
CLUSTER_NODES_COUNT = {}
CLASS_EDGES_DATA = []
CLASS_NODES_DATA = []
CLUSTERED_NODES_FILE_PATH = "Nodes_Mod_1.csv"
CLUSTERED_EDGES_FILE_PATH = "Edges_Mod_1.csv"

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
        # reference fieldnames = [Source, Target, Type, Id, Label, timeset, Weight]
        source_header = headers[0]
        target_header = headers[1]
        type_header = headers[2]
        id_header = headers[3]
        label_header = headers[4]
        timeset_header = headers[5]
        weight_header = headers[6]

        for row in reader:
            source = row[source_header]
            target = row[target_header]
            type_ = row[type_header]
            id = row[id_header]
            label = row[label_header]
            timeset = row[timeset_header]
            weight = row[weight_header]
            
            # new data = [c_source, c_target, type, id, label, timeset, weight]
            cluster_source = cluster_ids[source]
            cluster_target = cluster_ids[target]

            data = [cluster_source] + [cluster_target] + [type_] + [id] + [label] + [timeset] + [weight]
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
    assign_id_clusters(CLUSTER_IDS, CLUSTERED_NODES_FILE_PATH)
    convert_edges_to_hypergraph_edges(CLUSTERED_EDGES_FILE_PATH, CLUSTER_IDS, CLASS_EDGES_DATA, "hypergraph_edges.csv")
    convert_nodes_to_hypergraph_nodes(CLUSTERED_NODES_FILE_PATH, CLUSTER_NODES_COUNT, CLASS_NODES_DATA, "hypergraph_nodes.csv")
    



