import data_printer

count_input = int(input("몇 개의 데이터를 생성하시겠습니까?: "))
storeName_file = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/mission6 refactoring/src/storeNames.txt'
city_file = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/mission6 refactoring/src/koreaCities.txt'
si_file = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/mission6 refactoring/src/korea_sis.txt'
gu_file = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/mission6 refactoring/src/korea_gus.txt'
export_csv_file = '/Users/jeongjaeyeong/Project/SeSac/Python_DataGenerator/mission6 refactoring/src/data2.csv'

while True:
    print_or_csv = input("print or csv?: ").lower()
    exporter = data_printer.DataPrinter(storeName_file, si_file, gu_file)
    if print_or_csv == 'print':
        exporter.exprt_to_console(count_input)
        break
    elif print_or_csv == 'csv':
        exporter.exprt_to_csv(count_input, export_csv_file)
        break
    print("잘못 입력하셨습니다. 다시 입력해 주세요.")

if __name__ == "__main__":
    print("직접 실행")
    print(__name__)
else:
    print("임포트되어 사용됨")
    print(__name__)