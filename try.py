import csv

with open('students.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    
    with open(students_data, 'w') as data:
    

        keys = ['MSSV','Họ và tên','Ngày sinh','Giới tính']
        csv_writer = csv.DictWriter(data, fieldnames= keys, delimiter="|")
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
