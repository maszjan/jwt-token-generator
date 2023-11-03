import tkinter as tk
import random as r
import pyperclip
import webbrowser


def go_to_repo():
    webbrowser.open("https://github.com/maszjan")


class JwtTokenGeneratorApp:

    def __init__(self):
        self.copy_button = None
        self.generate_button = None
        self.text = None
        self.root = root
        self.root.title("JWT Token Generator 1.0.0")
        self.root.geometry("650x300")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.init_ui()

    def init_ui(self):
        self.create_widgets()

    def create_widgets(self):
        self.create_label("JWT Token Generator 1.0.0", 16)
        self.text = self.create_text(2, 68, 12)
        self.generate_button = self.create_button("Generate", self.generate_token)
        self.copy_button = self.create_button("Copy", self.copy_to_clipboard)
        self.create_label("Created by", 12)
        self.create_button("@maszjan", go_to_repo)
        self.create_button("Exit", self.exit_app)

    def create_label(self, text, font_size):
        label = tk.Label(self.root, text=text)
        label.config(font=("Impact", font_size), fg="green", bg="black", pady=5)
        label.pack()
        return label

    def create_text(self, height, width, font_size):
        text = tk.Text(self.root, height=height, width=width)
        text.config(font=("Roboto", font_size), fg="green", bg="black", border=0, pady=5, padx=5)
        text.tag_configure("center", justify="center")
        text.pack()
        return text

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command)
        button.config(font=("Impact", 16), fg="green", bg="black", border=0, pady=5)
        button.pack()
        return button

    def generate_token(self):
        jwt_token_arr = [r.randint(0, len(charsString) - 1) for _ in range(64)]
        generated_jwt_token = [charsString[index] for index in jwt_token_arr]
        generated_jwt_token_str = ''.join(generated_jwt_token)
        self.text.delete("1.0", "end")
        self.text.insert("1.0", generated_jwt_token_str)
        print("Generated JWT Token:", generated_jwt_token_str)

    def copy_to_clipboard(self):
        generated_jwt_token = self.text.get("1.0", "end-1c")
        pyperclip.copy(generated_jwt_token)

    def exit_app(self):
        self.root.destroy()


if __name__ == '__main__':
    charsString = "QWERTYUIOPASDFGHHJKKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"

    root = tk.Tk()
    app = JwtTokenGeneratorApp()
    root.mainloop()
