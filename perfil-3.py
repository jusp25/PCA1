import customtkinter
import random
from database import food_items, animal_items, object_items, people_items, instructions_text
import pygame

pygame.init()
music = pygame.mixer_music.load('11 BoxCat Games - Assignment.mp3')
pygame.mixer_music.play(-1)

customtkinter.set_appearance_mode("light")
window = customtkinter.CTk()
window.geometry("800x450")

logo = customtkinter.CTkLabel(
    window, text="WHO AM I?", text_color="#FFAC33", font=("Arial", 35)
)
logo.pack(padx=10, pady=(10, 80))

category_page_title = customtkinter.CTkLabel(
    window, text="Select the category", font=("Arial", 24)
)

categories = ["Food", "Animal", "Object", "People"]


def handle_exit():
    window.destroy()

instructions_label = customtkinter.CTkLabel(window, text=instructions_text)
def display_instructions_page():
    play_button.pack_forget()
    instruction_button.pack_forget()
    quit_button.pack_forget()
    

    instructions_label.pack(padx=10, pady=(20, 30))

    back_to_menu_button.pack(padx=10, pady=10)

def display_menu_page():
    back_to_menu_button.pack_forget()
    category_1_button.pack_forget()
    category_2_button.pack_forget()
    category_3_button.pack_forget()
    category_4_button.pack_forget()
    category_page_title.pack_forget()
    instructions_label.pack_forget()

    logo.pack(padx=10, pady=(10, 70))
    play_button.pack(padx=10, pady=10)
    instruction_button.pack(padx=10, pady=10)
    quit_button.pack(padx=10, pady=10)


def display_category_page():
    logo.pack_forget()
    play_button.pack_forget()
    instruction_button.pack_forget()
    quit_button.pack_forget()

    logo.pack(padx=10, pady=15)
    category_page_title.pack(padx=10, pady=(20, 30))

    category_1_button.pack(padx=10, pady=10)
    category_2_button.pack(padx=10, pady=10)
    category_3_button.pack(padx=10, pady=10)
    category_4_button.pack(padx=10, pady=(10, 30))

    back_to_menu_button.pack(padx=10, pady=10)


def display_play_page(category_name, item):
    category_page_title.pack_forget()
    category_1_button.pack_forget()
    category_2_button.pack_forget()
    category_3_button.pack_forget()
    category_4_button.pack_forget()
    back_to_menu_button.pack_forget()

    random_item = random.choice(item)
    item.remove(random_item)
    answer = random_item[0]
    attempts = 5

    message_label = customtkinter.CTkLabel(window, font=("Arial", 24))
    if category_name == categories[0]:
        message_label.configure(text=f"I'm a {category_name}")
    elif category_name == categories[1] or category_name == categories[2]:
        message_label.configure(text=f"I'm an {category_name}")
    elif category_name == categories[3]:
        message_label.configure(text="I'm a person")

    message_label.pack(padx=10, pady=(20, 30))

    def check_guess():
        nonlocal attempts
        user_input = user_guess.get()
        if user_input.lower() == answer.lower():
            fail_label.configure(text="Congratulations! you're right!")
            next_round()
        else:
            fail_label.configure(text="Try again.")
            attempts -= 1
            attempts_label.configure(text=f"{attempts}/5 Chances")
            if attempts == 0:
                game_over()

    guess_frame = customtkinter.CTkFrame(window, fg_color="transparent")
    guess_frame.pack(padx=10, pady=10)

    guess_label = customtkinter.CTkLabel(guess_frame, text="I'm a...")
    guess_label.pack(side="left", padx=(0, 10))

    user_guess = customtkinter.CTkEntry(guess_frame)
    user_guess.pack(side="left")

    submit_button = customtkinter.CTkButton(
        guess_frame, text="Submit", command=check_guess
    )
    submit_button.pack(side="left", padx=(10, 0))

    attempts_label = customtkinter.CTkLabel(guess_frame, text="5/5 Chances")
    attempts_label.pack(side="left", padx=(10, 0))

    fail_label = customtkinter.CTkLabel(window, text="", text_color="red")
    fail_label.pack(padx=10, pady=(2, 10))

    hint_label = customtkinter.CTkLabel(window, text="")
    hint_label.pack(padx=10, pady=10)

    hint_frame = customtkinter.CTkFrame(window, fg_color="transparent")
    hint_frame.pack(padx=10, pady=10)

    def show_hint():
        if random_item[1:4]:
            random_hint = random.choice(random_item[1:4])
            random_item.remove(random_hint)
            hint_label.configure(text=random_hint)
        else:
            hint_label.configure(text="No more hints", text_color="red")

    hint_button = customtkinter.CTkButton(hint_frame, text="Hint", command=show_hint)
    hint_button.pack(side="left", padx=10, pady=10)

    def next_round():
        nonlocal attempts, answer
        user_guess.delete(0, "end")
        hint_label.configure(text="")

        if item:
            next_item = random.choice(item)
            item.remove(next_item)
            answer = next_item[0]

            if category_name == categories[0]:
                message_label.configure(text=f"I'm a {category_name}")
            if category_name == categories[1] or category_name == categories[2]:
                message_label.configure(text=f"I'm an {category_name}")
            elif category_name == categories[3]:
                message_label.configure(text="I'm a person")

            answer = next_item[0]
            attempts = 5
            attempts_label.configure(text=f"{attempts}/5 Chances")
            hint_button.configure(text_color="white")
            hint_label.configure(text="")

            random_item.clear()
            random_item.extend(next_item)

        else:
            exit_match()

    def game_over():
        message_label.pack_forget()
        hint_frame.pack_forget()
        guess_frame.pack_forget()
        hint_button.pack_forget()
        submit_button.pack_forget()
        attempts_label.pack_forget()
        fail_label.pack_forget()
        hint_label.pack_forget()
        exit_match_button.pack_forget()

        game_over_label = customtkinter.CTkLabel(
            window, text="Game Over", font=("Arial", 35), text_color="red"
        )
        game_over_label.pack(padx=10, pady=(20, 30))

        def try_again():
            game_over_label.pack_forget()
            try_again_button.pack_forget()
            display_category_page()

        try_again_button = customtkinter.CTkButton(
            window, text="Try Again", command=try_again
        )
        try_again_button.pack(padx=10, pady=10)

        

    def exit_match():
        message_label.pack_forget()
        hint_frame.pack_forget()
        guess_frame.pack_forget()
        exit_match_button.pack_forget()
        hint_label.pack_forget()
        fail_label.pack_forget()

        window.after(10, show_menu_buttons)

    def show_menu_buttons():
        play_button.pack(padx=10, pady=10)
        instruction_button.pack(padx=10, pady=10)
        quit_button.pack(padx=10, pady=10)

    exit_match_button = customtkinter.CTkButton(
        window, text="Quit Match", fg_color="#e60000", command=exit_match
    )
    exit_match_button.pack(padx=10, pady=10)


play_button = customtkinter.CTkButton(
    window, text="Play", command=display_category_page
)
play_button.pack(padx=10, pady=10)

instruction_button = customtkinter.CTkButton(window, text="Instructions", command=display_instructions_page)
instruction_button.pack(padx=10, pady=10)

quit_button = customtkinter.CTkButton(window, text="Exit", command=handle_exit)
quit_button.pack(padx=10, pady=10)

back_to_menu_button = customtkinter.CTkButton(
    window, text="Back", command=display_menu_page
)

category_1_button = customtkinter.CTkButton(
    window,
    text=categories[0],
    command=lambda: display_play_page(categories[0], food_items),
)
category_2_button = customtkinter.CTkButton(
    window,
    text=categories[1],
    command=lambda: display_play_page(categories[1], animal_items),
)
category_3_button = customtkinter.CTkButton(
    window,
    text=categories[2],
    command=lambda: display_play_page(categories[2], object_items),
)
category_4_button = customtkinter.CTkButton(
    window,
    text=categories[3],
    command=lambda: display_play_page(categories[3], people_items),
)

window.mainloop()
