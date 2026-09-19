def get_scores():
    """Ask the user how many assignments they have, then collect a
    valid score (0-100) for each one. Returns the scores as a list
    of numbers so the rest of the program can work with them."""
    scores = []

    # Keep asking until the user enters a valid whole number > 0
    while True:
        try:
            num_assignments = int(input("How many assignments do you want to enter? "))
            if num_assignments <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    # Collect one validated score per assignment
    for i in range(1, num_assignments + 1):
        while True:
            try:
                score = float(input(f"Enter the score for assignment {i} (0-100): "))
                if score < 0 or score > 100:
                    print("Score must be between 0 and 100.")
                    continue
                scores.append(score)
                break
            except ValueError:
                print("Please enter a valid number.")

    return scores


def calculate_average(scores):
    """Return the average of a list of numeric scores."""
    return sum(scores) / len(scores)


def get_letter_grade(average):
    """Convert a numeric average into a letter grade using standard
    10-point grading bands."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    """Run the grade calculator: collect scores, calculate the
    average, look up the letter grade, and display the results."""
    print("=== Grade Calculator ===")

    scores = get_scores()
    average = calculate_average(scores)
    letter_grade = get_letter_grade(average)

    print("\nResults")
    print("-------")
    print(f"Scores entered: {scores}")
    print(f"Average score: {average:.2f}")
    print(f"Letter grade: {letter_grade}")


if __name__ == "__main__":
    main()
