import csv
from tabulate import *

def update():
    print("1. Cập nhật thông tin sinh viên")
    print("2. Thêm sinh viên")
    print("3. Xóa sinh viên")
    option = int(input("Nhập số trước mỗi lựa chọn: "))
    if option == 1:
        mssv = input('Nhập MSSV: ')
        changing_data(mssv)
    elif option == 2:
        add_info()
    elif option == 3:
        mssv = input('Nhập MSSV: ')
        rmStu(mssv)

def rmStu(mssv):
    with open("students_data.csv", 'r',encoding="utf-8-sig") as data:

        keep = []
        found = False
        reader = csv.DictReader(data, delimiter='|')
        for row in reader:
            if row['MSSV'] != mssv:
                keep.append(row)
            else:
                wan_rm = row
                found = True
    
    if found == True:
                
        print(tabulate([wan_rm.values()], headers=keep[0].keys(), tablefmt="grid"))
        opt = input('Bạn thực sự có muốn xóa thông tin không? y/n: ')      
        if opt == 'y':
            with open("students_data.csv", 'w',encoding="utf-8-sig") as data:
                writer = csv.DictWriter(data,fieldnames=keep[0].keys(),delimiter='|')
                writer.writeheader()
                writer.writerows(keep)
            print('Xóa thành công')
        elif opt == 'n':
            return None
    else:
        print('Không tìm thấy sinh viên!')        
    
def changing_data(mssv):
    with open("students_data.csv", 'r',encoding="utf-8-sig") as data:

        keep = []
        found = False
        reader = csv.DictReader(data, delimiter='|')
        for row in reader:
            if row['MSSV'] != mssv:
                keep.append(row)
            else:
                wan_change = row
                found = True
    if found == True:
        print(tabulate([wan_change.values()], headers=keep[0].keys(), tablefmt="grid"))
        print('Chọn trường muốn thay đổi')
        print('0.MSSV', '1.Họ và tên','2.Ngày sinh','3.Giới tính', '4.Email', '5.Chuyên cần', '6.Giữa kì', '7.Cuối kì')
        opt = input('Nhập các lựa chọn (1-8): ').split()
        opt_dict = {
            '0':'MSSV',
            '1':'Họ và tên',
            '2':'Ngày sinh',
            '3':'Giới tính',
            '4':'Email',
            '5':'Chuyên cần',
            '6':'Giữa kì',
            '7':'Cuối kì'
        }
        for i in opt:
            change = input(f'{opt_dict[i]}: ')
            wan_change[opt_dict[i]] = change
        if '5' in opt or '6' in opt or '7' in opt:
            chcan = float(wan_change['Chuyên cần'])
            mid_term = float(wan_change['Giữa kì'])
            end_term = float(wan_change['Cuối kì'])
            avag = (chcan + mid_term*3 + end_term*6)/10
            gpa = avag * 0.4
            wan_change['GPA'] = round(gpa,1)
            wan_change['Xếp loại'] = gpa_to_letter(gpa)
        print(tabulate([wan_change.values()], headers=keep[0].keys(), tablefmt="grid"))
        wanna_change = input('Xác nhận thay đổi? y/n: ')
        if wanna_change == 'y':
            keep.append(wan_change)
            with open("students_data.csv", 'w',encoding="utf-8-sig") as data:
                writer = csv.DictWriter(data,fieldnames=keep[0].keys(),delimiter='|')
                writer.writeheader()
                writer.writerows(keep)
            print('Thay đổi thành công!')
        elif wanna_change == 'n':
            return None
    else:
        print('Không tìm thấy sinh viên!')
    

def gpa_to_letter(gpa):
    if gpa >= 3.7:
        return "A"
    elif gpa >= 3.3:
        return "B+"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.7:
        return "B-"
    elif gpa >= 2.3:
        return "C+"
    elif gpa >= 2.0:
        return "C"
    elif gpa >= 1.7:
        return "C-"
    elif gpa >= 1.3:
        return "D+"
    elif gpa >= 1.0:
        return "D"
    else:
        return "F"

def take_info():
    stuID = input('MSSV: ')
    name = input('Họ và tên: ')
    birth = input('Ngày sinh (dd/mm/yyyy): ')
    gender = input('Giới tính (Nam|Nữ): ')
    email = input('Email: ')
    chcan = float(input('Chuyên cần: '))
    mid_term = float(input('Giữa kì: '))
    end_term = float(input('Giữa kì: '))
    avag = (chcan + mid_term*3 + end_term*6)/10
    gpa = avag * 0.4
    row ={
        'MSSV': stuID,
        'Họ và tên':name,
        'Ngày sinh':birth,
        'Giới tính':gender,
        'Email':email,
        'Chuyên cần': chcan,
        'Giữa kì': mid_term,
        'Cuối kì': end_term,
        'GPA': round(gpa,1),
        'Xếp loại': gpa_to_letter(gpa)
    }
    return row

def add_info():
    keys = ['MSSV', 'Họ và tên','Ngày sinh','Giới tính', 'Email', 'Chuyên cần', 'Giữa kì', 'Cuối kì','GPA','Xếp loại']
    info = take_info()
    print(tabulate([info.values()], headers=keys, tablefmt="grid"))
    add = input('Xác nhận thêm sinh viên? y/n: ')
    if add == 'y':
        with open("students_data.csv", 'a',encoding="utf-8-sig") as data:
            writer = csv.DictWriter(data, fieldnames=keys, delimiter='|')
            writer.writerow(info)
    elif add == 'n':
        return None

def main():
    update()

if __name__ == '__main__':
    main()