def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A+"
    elif 80 <= average < 90:
        return "A"
    elif 70 <= average < 80:
        return "B"
    elif 60 <= average < 70:
        return "C"
    elif 50 <= average < 60:
        return "D"
    else:
        return "F"

# Input marks for 5 subjects
subject_marks = []
for i in range(5):
    mark = float(input("Enter marks for subject {}: ".format(i+1)))
    subject_marks.append(mark)

# Calculate and display the grade
grade = calculate_grade(subject_marks)
print("The grade is:", grade)
