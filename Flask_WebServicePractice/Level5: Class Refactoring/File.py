import csv

class File:
    def read(self, file_path):
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            rdr = csv.reader(f)
            for row in rdr:
                clean_row = [element.strip() for element in row]
                data.append(clean_row)
        return data