
def calculate_average(total):
    return total / 5


# Grading scale
def find_puntos(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'



puntos = []
for i in range(1, 6):
    puntos = int(input('Enter puntos {0}: '.format(i)))
    print('That\'s a(n): ' + find_puntos(puntos))
    puntos.append(puntos)

# sum of all subject marks
total = sum(puntos)
avg_marks = calculate_average(total)
final_grade = find_puntos(avg_marks)

print('Average grade is: ' + str(avg_marks))
print("That's a(n): " + str(final_grade))