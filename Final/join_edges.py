"""
Documentation
"""

import csv

class JoinEdges:

    def __init__(self, fields_indices, file_path_list):
        """
        """
        self.FILE_PATHS = file_path_list
        self.EDGES_FIELDNAMES_INDEX = fields_indices
        self.DATA = []

    def __call__(self):
        """
        """
        for file_path in self.FILE_PATHS:
            #print(file_path)
            with open(file_path, "r") as file_handle:
                reader = csv.DictReader(file_handle, delimiter=",")
                headers = reader.fieldnames
                headers = list(headers)
                header_list = []
                for indices in self.EDGES_FIELDNAMES_INDEX:
                    header_list.append(headers[indices])
                self.FIELDNAMES = header_list
                #print(self.FIELDNAMES)
                
                for row in reader:
                    data = []
                    for header in header_list:
                        data.append(row[header])
                    self.DATA.append(data)
    
    def save(self, filename):
        """
        """
        with open(filename, "w") as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(self.FIELDNAMES)
            csvwriter.writerows(self.DATA)



                

