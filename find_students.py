def find_students():
    import pandas as pd
    from tabulate import tabulate

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