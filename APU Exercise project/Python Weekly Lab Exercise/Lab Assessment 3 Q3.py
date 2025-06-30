def get_student_answers():
    answers = []
    for i in range(1, 6):
        while True:
            answer = input(f"Enter answer for question {i} (A, B, C, or D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                answers.append(answer)
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
    return answers


def save_answers_to_file(filename, answers):
    with open(filename, 'w') as file:
        for answer in answers:
            file.write(answer + "\n")


def read_answers_from_file(filename):
    answers = []
    with open(filename, 'r') as file:
        answers = file.read().splitlines()
    return answers


def check_answers(student_answers, correct_answers):
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            print(f"Question {i + 1}: Correct")
        else:
            print(
                f"Question {i + 1}: Incorrect (Your answer: {student_answers[i]}, Correct answer: {correct_answers[i]})")


def main():
    filename = "answer.txt"

    # Correct answers
    correct_answers = ['A', 'C', 'A', 'A', 'D']

    # Get student answers and save to file
    student_answers = get_student_answers()
    save_answers_to_file(filename, student_answers)

    # Read student answers from file
    student_answers = read_answers_from_file(filename)

    # Check student answers
    check_answers(student_answers, correct_answers)


if __name__ == "__main__":
    main()