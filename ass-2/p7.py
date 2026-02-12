'''
7. Menu Driven Program: Student Result
System
Operations:
   Enter Marks
   Calculate Percentage
   Assign Grade
'''
# Functions
def enter_marks():
    marks = []
    subjects = int(input("Enter number of subjects: "))
    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    return marks

def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return percentage

def assign_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Menu-driven program
marks = []

while True:
    print("\nStudent Result System Menu:")
    print("1. Enter Marks")
    print("2. Calculate Percentage")
    print("3. Assign Grade")
    print("4. Exit")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        marks = enter_marks()
        print("Marks entered successfully.")
    elif choice == '2':
        if marks:
            percentage = calculate_percentage(marks)
            print("Percentage:", percentage)
        else:
            print("Please enter marks first.")
    elif choice == '3':
        if marks:
            percentage = calculate_percentage(marks)
            grade = assign_grade(percentage)
            print("Grade:", grade)
        else:
            print("Please enter marks first.")
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
