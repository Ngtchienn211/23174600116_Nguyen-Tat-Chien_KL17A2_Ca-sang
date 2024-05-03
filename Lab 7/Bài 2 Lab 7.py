student_dict = {}
grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for i in range(1, 11):
    name = input(f"Nhập tên của sinh viên {i}: ")
    while True:
        score_input = input(f"Nhập điểm thi của sinh viên {i}: ")
        if score_input.replace('.', '', 1).isdigit(): 
            score = float(score_input)
            
            if 0 <= score <= 10:
                break 
            else:
                print("Điểm thi phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
        else:
            print("Điểm thi phải là một số thực. Vui lòng nhập lại.")
    if score < 4.0:
        grade = "F"
    elif 4.0 <= score < 5.5:
        grade = "D"
    elif 5.5 <= score < 7.0:
        grade = "C"
    elif 7.0 <= score < 8.5:
        grade = "B"
    else:
        grade = "A"
    
    student_dict[name] = grade
    grade_count[grade] += 1

print("\nXếp loại học lực của sinh viên:")
for name, score in student_dict.items():
    print(f"{name}: {score}")

print("\nThống kê số lượng sinh viên ở mỗi loại học lực:")
for grade, count in grade_count.items():
    print(f"{grade}: {count}")
