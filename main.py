import csv
import pandas as pd
from tabulate import *

# Chương trình chính
def main():
    #Login
    print("-"*120)
    print("=====[HỆ THỐNG QUẢN LÝ SINH VIÊN]=====")
    while True:
        mat_khau = input("Nhập mật khẩu để vào (Gợi ý: 123): ")
        if mat_khau == "123":
            print("Đăng nhập thành công!")
            break
        else:
            print("Sai mật khẩu, vui lòng nhập lại!")

    #Menu
    while True:
        print("-"*120)
        print("=== MENU CHỨC NĂNG ===")
        print("1. Xem danh sách lớp")
        print("2. Chỉnh sửa sinh viên")
        print("3. Tìm kiếm sinh viên")
        print("4. Thoát chương trình")

        chon = input("Mời chọn chức năng (1-4): ")

        if chon == "1":
            all_students()

        elif chon == "2":
            update()
        elif chon == "3":
            find_students()
        elif chon == "4":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

def all_students():
    
    df = pd.read_csv('students_data.csv', encoding='utf-8-sig', sep='|')
    danh_sach = df.to_dict('records')
    headers = ["MSSV", "Họ và tên", "Ngày sinh", "Giới tính", "Email", "Chuyên cần", "Giữa kì", "Cuối kì",
               "GPA", "Xếp loại"]
    rows = [
        [student["MSSV"], student["Họ và tên"], student["Ngày sinh"], student["Giới tính"], student["Email"],
         student["Chuyên cần"], student["Giữa kì"], student["Cuối kì"], student["GPA"], student["Xếp loại"]] for
        student in danh_sach]
    print("-" * 120)
    # sắp xếp theo thứ tự muốn xem
    print("=======DANH SÁCH LỚP=======")
    print("Các lựa chọn:")
    print("1. Mặc định\n2. Theo điểm chuyên cần\n3. Theo điểm GPA\n4. Theo xếp loại cuối")
    choice1 = input("Lựa chọn của bạn là : ")
    if choice1 == "1":
        print("-" * 120)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        return main()
    if choice1 == "2":
        while True:
            print("-" * 120)
            print("CHỌN 1 TRONG 2:")
            print("1. ĐIỂM CHUYÊN CẦN TĂNG DẦN")
            print("2. ĐIỂM CHUYÊN CẦN GIẢM DẦN")
            opt12 = input("Bạn muốn xem danh sách học sinh theo điểm chuyên cần tăng dần hay giảm dần ? Nhập 1 hoặc 2: ")
            if opt12 == "1":
                print("--" * 30, "Bảng điểm học sinh theo điểm chuyên cần tăng dần", "--" * 30)
                df_sorted = df.sort_values(by='Chuyên cần', ascending=True)
                print(tabulate(df_sorted, headers=headers, tablefmt="grid"))
            elif opt12 == "2":
                print("--" * 30, "Bảng điểm học sinh theo điểm chuyên cần giảm dần", "--" * 30)
                df_sorted = df.sort_values(by="Chuyên cần", ascending=False)
                df = tabulate(rows, headers=headers, tablefmt="grid")
                print(tabulate(df_sorted, headers=headers, tablefmt="grid"))
            else:
                print("Nhâp 1 hoặc 2")
        return main()



    if choice1 == "3":
        while True:
            print("-" * 120)
            print("CHỌN 1 TRONG 2:")
            print("1. ĐIỂM GPA TĂNG DẦN")
            print("2. ĐIỂM GPA GIẢM DẦN")
            opt13 = input("Bạn muốn xem danh sách học sinh theo điểm GPA tăng hay giảm ? Nhập 1 hoặc 2: ")
            if opt13 == "1":
                print("--"*30,"Bảng điểm học sinh theo điểm GPA tăng dần","--"*30)
                df_sorted = df.sort_values(by='GPA', ascending=True)
                print(tabulate(df_sorted,headers=headers, tablefmt="grid"))
            elif opt13 == "2":
                print("--" * 30, "Bảng điểm học sinh theo điểm GPA giảm dần", "--" * 30)
                df_sorted = df.sort_values(by='GPA', ascending=False)
                print(tabulate(df_sorted,headers=headers, tablefmt="grid"))
            else:
                print("Nhâp 1 hoặc 2")
        return main()
    elif choice1 == "4":
        priority = {"D": 0, "D+": 1, "C": 2, "C+": 3, "B": 4, "B+": 5, "A": 6, "A+": 7}
        danh_sach = df.to_dict('records')
        while True:
            print("-" * 120)
            print("CHỌN 1 TRONG 2:")
            print("1. Xếp loại tăng dần\n2. Xếp loại giảm dần")
            opt14 = input("Lựa chọn 1 hoặc 2: ")

            if opt14 in ["1", "2"]:
                is_reverse = (opt14 == "2")
                danh_sach.sort(key=lambda x: priority.get(x["Xếp loại"], -1), reverse=is_reverse)
                rows = [[s[h] for h in headers] for s in danh_sach]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
                break
            else:
                print("Vui lòng chỉ nhập 1 hoặc 2!")
        return main()





# Tìm kiếm và hiển thị
def find_students():
    df = pd.read_csv('students_data.csv', encoding='utf-8-sig', sep='|')
    danh_sach = df.to_dict('records')
    
    print("1. Tìm kiếm theo mã sinh viên")
    print("2. Tìm kiếm theo tên sinh viên")
    print("3. Tìm kiếm theo ngày sinh sinh viên")
    print("4. Tìm kiếm theo email sinh viên")
    print("5. Tìm kiếm theo điểm sinh viên")
    print("6. Tìm kiếm theo xếp loại")
    print("7. Quay lại màn hình chính")
    while True:
        option = int(input("Hãy chọn phương án tìm kiếm (Nhập số 1 - 7): "))
        result_find = []
        if option < 1 or option > 7:
            print("Không có lựa chọn đó, hãy nhập lại")
            continue
        else:
            if option == 1:
                print("(Nhập x nếu muốn quay lại màn hình tìm kiếm)")
                find_msv = input("Hãy nhập mã sinh viên: ")
                if find_msv == 'x':
                    return find_students()
                else:
                    for msv in danh_sach:
                        if find_msv in str(msv['MSSV']):
                            result_find.append(msv)
            elif option == 2:
                print("(Nhập x nếu muốn quay lại màn hình tìm kiếm)")
                find_name = input("Hãy nhập tên sinh viên: ")
                if find_name == 'x':
                    return find_students()
                else:
                    for name in danh_sach:
                        if find_name in name['Họ và tên']:
                            result_find.append(name)
            elif option == 3:
                print("(Nhập x nếu muốn quay lại màn hình tìm kiếm)")
                find_birth = input("Hãy nhập ngày sinh sinh viên: ")
                if find_birth == 'x':
                    return find_students()
                else:
                    for birth in danh_sach:
                        if find_birth in birth['Ngày sinh']:
                            result_find.append(birth)
            elif option == 4:
                print("(Nhập x nếu muốn quay lại màn hình tìm kiếm)")
                find_email = input("Hãy nhập email sinh viên: ")
                if find_email == 'x':
                    return find_students()
                else:
                    for email in danh_sach:
                        if find_email in email['Email']:
                            result_find.append(email)
            elif option == 5:
                def find_with_scores():
                    print("1. Tìm kiếm theo điểm chuyên cần")
                    print("2. Tìm kiếm theo điểm giữa kì")
                    print("3. Tìm kiếm theo điểm cuối kì")
                    print("4. Tìm kiếm theo GPA")
                    print("5. Quay lại màn hình tìm kiếm")
                    while True:
                        option_find = int(input("Hãy nhập lựa chọn tìm kiếm (Nhập số 1 - 5): "))
                        if option_find < 1 or option_find > 5:
                            print("Không có lựa chọn đó, hãy nhập lại")
                            continue
                        elif option_find == 1:
                            print("(Nhập x nếu muốn quay lại màn hình tìm kiếm với điểm)")
                            find_chuyen_can = float(input("Hãy nhập điểm chuyên cần của sinh viên: "))
                            if find_chuyen_can == 'x':
                                return find_with_scores()
                            else:
                                for chuyen_can in danh_sach:
                                    if float(chuyen_can['Chuyên cần']) == find_chuyen_can:
                                        result_find.append(chuyen_can)
                        elif option_find == 2:
                            print("(Nhập x nếu muốn quay lại màn hình tìm kiếm với điểm)")
                            find_mid_term = float(input("Hãy nhập điểm giữa kì của sinh viên: "))
                            if find_mid_term == 'x':
                                return find_with_scores()
                            else:
                                for mid_term in danh_sach:
                                    if float(mid_term['Giữa kì']) == find_mid_term:
                                        result_find.append(mid_term)
                        elif option_find == 3:
                            print("(Nhập x nếu muốn quay lại màn hình tìm kiếm với điểm)")
                            find_final_term = float(input("Hãy nhập điểm cuối kì của sinh viên: "))
                            if find_final_term == 'x':
                                return find_with_scores()
                            else:
                                for final_term in danh_sach:
                                    if float(final_term['Cuối kì']) == find_final_term:
                                        result_find.append(final_term)
                        elif option_find == 4:
                            print("(Nhập x nếu muốn quay lại màn hình tìm kiếm với điểm)")
                            find_gpa = float(input("Hãy nhập GPA của sinh viên: "))
                            if find_gpa == 'x':
                                return find_with_scores()
                            else:
                                for gpa in danh_sach:
                                    if float(gpa['GPA']) == find_gpa:
                                        result_find.append(gpa)
                        elif option_find == 5:
                            return find_students()
                        break
                find_with_scores()
            elif option == 6:
                print("(Nhập x nếu muốn quay lại màn hình tìm kiếm)")
                find_rank = input("Hãy nhập xếp loại của sinh viên: ")
                if find_rank == 'x':
                    return find_students()
                else:
                    for rank in danh_sach:
                        if rank['Xếp loại'] == find_rank:
                            result_find.append(rank)
            elif option == 7:
                return main()
        if result_find == []:
            print("Không tìm thấy sinh viên")
            return find_students()
        else:
            headers = ["MSSV", "Họ và tên", "Ngày sinh", "Giới tính", "Email", "Chuyên cần", "Giữa kì", "Cuối kì", "GPA", "Xếp loại"]
            rows = [[student["MSSV"], student["Họ và tên"], student["Ngày sinh"], student["Giới tính"], student["Email"], student["Chuyên cần"], student["Giữa kì"], student["Cuối kì"], student["GPA"], student["Xếp loại"]] for student in result_find]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
            return find_students()
        return None
    


# Cập nhật thông tin

def update():
    print("-" * 120)
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
    print("-" * 120)
    with open("students_data.csv", 'r', encoding="utf-8-sig") as data:

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
            with open("students_data.csv", 'w', encoding="utf-8-sig") as data:
                writer = csv.DictWriter(data, fieldnames=keep[0].keys(), delimiter='|')
                writer.writeheader()
                writer.writerows(keep)
            print('Xóa thành công')
        elif opt == 'n':
            return None
    else:
        print('Không tìm thấy sinh viên!')

def changing_data(mssv):
    with open("students_data.csv", 'r', encoding="utf-8-sig") as data:

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
        print('0.MSSV', '1.Họ và tên', '2.Ngày sinh', '3.Giới tính', '4.Email', '5.Chuyên cần', '6.Giữa kì',
              '7.Cuối kì')
        opt = input('Nhập các lựa chọn (1-8): ').split()
        opt_dict = {
            '0': 'MSSV',
            '1': 'Họ và tên',
            '2': 'Ngày sinh',
            '3': 'Giới tính',
            '4': 'Email',
            '5': 'Chuyên cần',
            '6': 'Giữa kì',
            '7': 'Cuối kì'
        }
        for i in opt:
            change = input(f'{opt_dict[i]}: ')
            wan_change[opt_dict[i]] = change
        if '5' in opt or '6' in opt or '7' in opt:
            print("-" * 120)
            chcan = float(wan_change['Chuyên cần'])
            mid_term = float(wan_change['Giữa kì'])
            end_term = float(wan_change['Cuối kì'])
            avag = (chcan + mid_term * 3 + end_term * 6) / 10
            gpa = avag * 0.4
            wan_change['GPA'] = round(gpa, 1)
            wan_change['Xếp loại'] = gpa_to_letter(gpa)
        print(tabulate([wan_change.values()], headers=keep[0].keys(), tablefmt="grid"))
        wanna_change = input('Xác nhận thay đổi? y/n: ')
        if wanna_change == 'y':
            print("-" * 120)
            keep.append(wan_change)
            with open("students_data.csv", 'w', encoding="utf-8-sig") as data:
                writer = csv.DictWriter(data, fieldnames=keep[0].keys(), delimiter='|')
                writer.writeheader()
                writer.writerows(keep)
            print('Thay đổi thành công!')
        elif wanna_change == 'n':
            return None
    else:
        print('Không tìm thấy sinh viên!')

def gpa_to_letter(gpa):
    print("-" * 120)
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
    print("-" * 120)
    stuID = input('MSSV: ')
    name = input('Họ và tên: ')
    birth = input('Ngày sinh (dd/mm/yyyy): ')
    gender = input('Giới tính (Nam|Nữ): ')
    email = input('Email: ')
    chcan = float(input('Chuyên cần: '))
    mid_term = float(input('Giữa kì: '))
    end_term = float(input('Giữa kì: '))
    avag = (chcan + mid_term * 3 + end_term * 6) / 10
    gpa = avag * 0.4
    row = {
        'MSSV': stuID,
        'Họ và tên': name,
        'Ngày sinh': birth,
        'Giới tính': gender,
        'Email': email,
        'Chuyên cần': chcan,
        'Giữa kì': mid_term,
        'Cuối kì': end_term,
        'GPA': round(gpa, 1),
        'Xếp loại': gpa_to_letter(gpa)
    }
    return row

def add_info():
    keys = ['MSSV', 'Họ và tên', 'Ngày sinh', 'Giới tính', 'Email', 'Chuyên cần', 'Giữa kì', 'Cuối kì', 'GPA',
            'Xếp loại']
    info = take_info()
    print(tabulate([info.values()], headers=keys, tablefmt="grid"))
    add = input('Xác nhận thêm sinh viên? y/n: ')
    if add == 'y':
        print("-" * 120)
        with open("students_data.csv", 'a', encoding="utf-8-sig") as data:
            writer = csv.DictWriter(data, fieldnames=keys, delimiter='|')
            writer.writerow(info)
    elif add == 'n':
        return None





# Chạy
if __name__ == '__main__':
    main()