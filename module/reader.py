import os
import csv
def readAllFileDirectory(directory_path):
    file_list = []

    # 디렉터리 내의 모든 파일과 폴더를 순회
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)

    return file_list

def readCsv():
    parsed_data = []

    with open('./target.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            parsed_data.append(row)

    return parsed_data