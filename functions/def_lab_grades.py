def grade_info(grades):

    result = None

    if grades <= 2.99 and grades >= 2.00:
        result = "Fail"
    elif grades <= 3.49:
        result = "Poor"
    elif grades <= 4.49:
        result = "Good"
    elif grades <= 5.49:
        result = "Very Good"
    elif grades <= 6.00:
        result = "Excellent"

    return result


score = float(input())
print(grade_info(score))
