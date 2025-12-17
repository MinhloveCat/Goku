import csv

with open('students.csv', 'r', encoding = 'utf-8-sig') as students_data:
    csv_reader = csv.DictReader(students_data)

    with open('students_data.csv', 'w', encoding = 'utf-8-sig') as data:
    

        keys = ['MSSV','Họ và tên','Ngày sinh','Giới tính']
        csv_writer = csv.DictWriter(data, fieldnames= keys, delimiter="|")
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)

    
    