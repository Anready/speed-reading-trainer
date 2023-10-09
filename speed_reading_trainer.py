import tkinter as tk
import time


def update_text():
    if not update_text.running:
        update_text.running = True
        for i in range(1, 6):
            label.config(text=i)
            root.update()
            time.sleep(1)

        label.config(text="START!")
        root.update()
        time.sleep(1)

        for word in input_text.split(' '):
            time.sleep(words_per_minute)
            label.config(text=word)
            root.update()  # Update window

        time.sleep(1)
        label.config(text="THE END")
        root.update()
        update_text.running = False
        root.attributes("-fullscreen", False)


update_text.running = False

root = tk.Tk()
root.title("Speed words")

root.attributes("-fullscreen", True)  # Migrate window to full screen mod

text = "Press her to start"
label = tk.Label(root, text=text, fg="white", bg="black", font=("Helvetica", 30))
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.configure(bg="black")

label.bind("<Button-1>", lambda event: update_text())

input_text = input("Enter text here (replace all 'enter' in your text of 'space'):\n").replace('\n', ' ')
words_per_minute = 60 / int(input("Enter words per second: (Optimal: 320)\n"))

root.mainloop()
