from tkinter import *
import json
import random

player_score = 0

# Load questions from the JSON file
def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

# Variables to keep track of state
current_question = None
counter = 0
time_left = 15  # Time for each question

# Display a random question
def display_question():
    global current_question, counter, time_left

    # Reset timer
    time_left = 15
    update_timer()

    # Increment counter
    counter += 1

    # Change button text on first click
    if counter == 1:
        generate_btn.config(text="Generate New Question")

    # Select a random question
    current_question = random.choice(questions)
    question_label.config(text=current_question["question"])

    # Set options
    option_1_btn.config(text=current_question["options"][0], state=NORMAL)
    option_2_btn.config(text=current_question["options"][1], state=NORMAL)
    option_3_btn.config(text=current_question["options"][2], state=NORMAL)
    option_4_btn.config(text=current_question["options"][3], state=NORMAL)

    option_1_btn.grid(row=0, column=0, padx=10, pady=10)
    option_2_btn.grid(row=0, column=1, padx=10, pady=10)
    option_3_btn.grid(row=1, column=0, padx=10, pady=10)
    option_4_btn.grid(row=1, column=1, padx=10, pady=10)

    timer_label.config(text=f"Time Left: {time_left} sec")

    # Reset result label
    result_label.config(text="", bg=root.cget("bg"))

# Check if the selected option is correct
def check_answer(selected_option):
    global time_left, player_score
    time_left = 0  # Stop timer when an answer is selected

    if current_question["options"][selected_option] == current_question["answer"]:
        result_label.config(text="Correct Answer!", bg="green")
        player_score += 1
        player.config(text=f"Your Score: {player_score}")
    else:
        result_label.config(text="Wrong Answer!", bg="red")
        player_score -= 1
        player.config(text=f"Your Score: {player_score}")

    # Disable buttons after answering
    disable_option_buttons()

# Disable all option buttons
def disable_option_buttons():
    option_1_btn.config(state=DISABLED)
    option_2_btn.config(state=DISABLED)
    option_3_btn.config(state=DISABLED)
    option_4_btn.config(state=DISABLED)

# Timer functionality
def update_timer():
    global time_left

    if time_left > 0:
        timer_label.config(text=f"Time Left: {time_left} sec")
        time_left -= 1
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's Up!")
        disable_option_buttons()

# Initialize Tkinter
root = Tk()
root.geometry("700x600")
root.minsize(300, 200)
root.title("Quiz App")

# Load questions from the JSON file
questions = load_questions()

# Widgets
generate_btn = Button(root, text="Generate Question", width=50, command=display_question)
generate_btn.pack(pady=20)

question_label = Label(root, text="", font=("Arial", 15))
question_label.pack(pady=20)

timer_label = Label(root, text="", font=("Arial", 12), fg="red")
timer_label.pack()

options_frame = Frame(root)
options_frame.pack(pady=10)

option_1_btn = Button(options_frame, text="", width=20, padx=5, pady=8, command=lambda: check_answer(0))


option_2_btn = Button(options_frame, text="", width=20, padx=5, pady=8, command=lambda: check_answer(1))


option_3_btn = Button(options_frame, text="", width=20, padx=5, pady=8, command=lambda: check_answer(2))


option_4_btn = Button(options_frame, text="", width=20, padx=5, pady=8, command=lambda: check_answer(3))


result_label = Label(root, text="", font=("Arial", 12), pady=10)
result_label.pack()

# Showing player score
player = Label(root, text="", padx=10, pady=10, font=("Arial", 15))
player.pack(pady=10)

# Start Tkinter main loop
root.mainloop()
