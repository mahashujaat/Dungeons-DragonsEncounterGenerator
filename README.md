This Python-based tool automatically generates Dungeons & Dragons encounters by combining user-defined difficulty levels and specific search criteria (tags). The generator operates with three core functionalities:

Difficulty Slider: This adjustable slider lets you set the encounter difficulty level, ranging from "Easy" to "Deadly." The difficulty level determines the total experience points (EXP) budget, which the generator uses to select and combine monsters.

Filter System: You can refine the encounter by specifying tags you want to include or avoid. These tags (such as "undead," "humanoid," "flying") help tailor the encounter to your specific needs, ensuring the selected monsters match your desired theme or setting.

Monster Database Integration: The generator reads from a notepad document (filename.txt) that contains a list of monsters with attributes like "name," "exp," "tags," and a "link." The program processes this data to generate encounters that fit within the chosen difficulty and tag criteria.

How It Works:
The program reads the monster data from the filename.txt file, where each line represents a different monster with attributes formatted as key-value pairs.
The generator uses the provided difficulty level to calculate the required total EXP for the encounter. It then filters monsters based on the user's tag preferences.
The program assembles an encounter by selecting appropriate monsters whose combined EXP matches the chosen difficulty. The more difficult the encounter, the more or stronger monsters will be included.

