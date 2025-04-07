
import random
import tkinter as tk

prompts = [
    "A mysterious package arrives at your door with no return address.",
    "You wake up in a world where no one can lie. What happens next?",
    "Describe a dinner between a vampire and a werewolf.",
    "A child discovers a portal in their backyard.",
    "You find a journal with entries dated 100 years into the future.",
    "Write about someone who remembers every detail of their past lives.",
    "An AI becomes obsessed with writing poetry.",
    "Two strangers swap lives every time they fall asleep.",
    "A library where every book is a memory from someone else's life.",
    "You inherit a house that only appears during a full moon."
]

class PromptGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Writing Prompt Generator")
        self.master.geometry("500x300")

        self.prompt_label = tk.Label(master, text="Click below to get a prompt!", wraplength=450, font=("Helvetica", 14), justify="center")
        self.prompt_label.pack(pady=40)

        self.generate_button = tk.Button(master, text="Generate Prompt", command=self.display_prompt, font=("Helvetica", 12))
        self.generate_button.pack()

    def display_prompt(self):
        prompt = random.choice(prompts)
        self.prompt_label.config(text=prompt)

if __name__ == "__main__":
    root = tk.Tk()
    app = PromptGeneratorApp(root)
    root.mainloop()
