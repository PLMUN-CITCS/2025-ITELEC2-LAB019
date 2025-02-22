def get_student_score():
    """Gets the student's score from user input."""

    score = float(input("Enter your score: "))
    return score


def calculate_grade(score):
    """Calculates the grade based on the provided score."""

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# Main program flow
score = get_student_score()
grade = calculate_grade(score)
print("Your Grade is:", grade)