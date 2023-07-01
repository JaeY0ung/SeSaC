import csv
import data_generator

class DataPrinter(data_generator.DataGenerator): # 상속
    def exprt_to_console(self, count):
        data = self.generate_data(count)
        for id, name, type, address in data:
            print(f"ID:{id}\nName:{name}\nType:{type}\nAddress:{address}\n")
    
    def exprt_to_csv(self, count, filename):
        data = self.generate_data(count)
        headers = ['ID', 'Name', 'Type', 'Address']
        with open(filename, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerow(headers)
            wr.writerows(data)