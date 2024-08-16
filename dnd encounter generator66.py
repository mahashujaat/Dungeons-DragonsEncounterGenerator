import random
import tkinter as tk
from tkinter import ttk

# Sample data for the notepad document with parameters "monster name," "exp," "tags," "link"
# Replace this data with your actual monster data
def read_monster_data_from_file(filename):
    monster_data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                monster_info = eval("{" + line + "}")
                monster_data.append(monster_info)
    return monster_data
monster_data = read_monster_data_from_file("filename.txt")
def generate_encounter(difficulty, search_tags, avoid_tags):
    filtered_monsters = []
    for monster in monster_data:
        monster_tags = set(monster["tags"])
        if all(tag in monster_tags for tag in search_tags) and not any(tag in monster_tags for tag in avoid_tags):
            filtered_monsters.append(monster)

    max_exp = 0.8 * (100 + 50 * int(difficulty))  # Convert difficulty to integer
    available_monsters = [m for m in filtered_monsters if m["exp"] <= max_exp]

    if not available_monsters:
        return "No suitable encounter found."

    num_monsters = random.randint(1, min(5, int(difficulty)))  # Convert difficulty to integer
    num_monsters = min(num_monsters, len(available_monsters))

    encounter = random.choices(available_monsters, k=num_monsters)
    return encounter

# ... (rest of the code remains the same)



def generate_button_click():
    difficulty = difficulty_slider.get()
    search_tags = search_tags_entry.get().lower().split(",")
    avoid_tags = avoid_tags_entry.get().lower().split(",")

    encounter = generate_encounter(difficulty, search_tags, avoid_tags)

    if isinstance(encounter, str):
        output_label.config(text=encounter)
    else:
        output_label.config(text="Encounter:\n")
        for monster in encounter:
            output_label.config(
                text=output_label.cget("text") + f"{monster['monster name']} ({monster['exp']} exp)\n"
                f"Tags: {', '.join(monster['tags'])}\n"
                f"Link: {monster['link']}\n\n"
            )

# GUI setup
# GUI setup
root = tk.Tk()
root.title("Dungeons and Dragons Encounter Generator")

# Set the window size and position it at the center of the screen
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Use ttk.Style to customize the appearance of the widgets
style = ttk.Style()
style.configure("TLabel", font=("Arial", 16))
style.configure("TButton", font=("Arial", 14))

# Heading label
heading_label = ttk.Label(root, text="Dungeons and Dragons Encounter Generator", style="TLabel")
heading_label.pack(pady=20)


difficulty_label = tk.Label(root, text="Select Difficulty:")
difficulty_label.pack()

difficulty_slider = ttk.Scale(root, from_=1, to=10, orient="horizontal", length=200)
difficulty_slider.pack()

search_tags_label = tk.Label(root, text="Enter Search Tags (comma-separated):")
search_tags_label.pack()

search_tags_entry = tk.Entry(root)
search_tags_entry.pack()

avoid_tags_label = tk.Label(root, text="Enter Avoid Tags (comma-separated):")
avoid_tags_label.pack()

avoid_tags_entry = tk.Entry(root)
avoid_tags_entry.pack()

generate_button = tk.Button(root, text="Generate Encounter", command=generate_button_click)
generate_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
