def get_name_age():
    return "John", 25
name, age = get_name_age()
print(name)
print(age)

# 리스트
numbers, even_numbers, odd_numbers = [1,2,3,4,5], [], []
for i in numbers:
    if i % 2:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)
print(f"짝수: {even_numbers}, 홀수: {odd_numbers}")


# 딕셔너리
student_grades = {"a":85, "b":92, "c":78, "d":95}
for name in student_grades:
    if student_grades[name] >= 90:
        print(name)