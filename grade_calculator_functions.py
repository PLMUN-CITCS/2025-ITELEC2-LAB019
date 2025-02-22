def get_student_score():
    """Gets the student's score from user input."""

    score = float(input("Enter your score: "))
    return score


def calculate_grade(score):
    """Calculates the grade based on the provided score."""
    grade = ''
    
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade


# Main program flow
score = get_student_score()
grade = calculate_grade(score)
print("Your Grade is:", grade)