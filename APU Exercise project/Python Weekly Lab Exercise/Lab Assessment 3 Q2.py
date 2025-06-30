import random

def write_responses_to_file(filename):
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later.",
        "I’m not sure.",
        "I can’t tell you right now.",
        "I’ll tell you after my nap.",
        "No way!",
        "I don’t think so.",
        "Without a doubt, no.",
        "Absolutely not!"
    ]

    with open(filename, 'w') as file:
        for response in responses:
            file.write(response + "\n")


def read_responses_from_file(filename):
    responses = []
    with open(filename, 'r') as file:
        responses = file.readlines()
    return [response.strip() for response in responses]


def get_random_response(responses):
    return random.choice(responses)


def main():
    filename = "8_ball_responses.txt"

    # Write responses to file
    write_responses_to_file(filename)

    # Read responses from file
    responses = read_responses_from_file(filename)

    print("Welcome to the Magic 8 Ball game!")

    while True:
        question = input("\nAsk a 'yes or no' question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            print("Thank you for playing!")
            break
        response = get_random_response(responses)
        print("Magic 8 Ball says: ", response)


if __name__ == "__main__":
    main()