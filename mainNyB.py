from tkinter import Tk, Button, Label, Entry
from NyB_module import NyBClass, nyb_function


def main():
    root = Tk()
    root.title("Beadandó - Nyári Bianka OVH077")
    root.geometry("400x300")


    welcome_label = Label(root, text="Ez a beadandóm")
    welcome_label.pack(pady=10)


    input_label = Label(root, text="Írj ide valamit:")
    input_label.pack(pady=5)
    input_entry = Entry(root)
    input_entry.pack(pady=5)


    def on_button_click():
        user_input = input_entry.get()
        current_time = nyb_function()
        nyb_instance = NyBClass()
        result = f"{nyb_instance.get_message()} - Ez lett beírva: {user_input} - Pontos dátum és idő: {current_time}"
        output_label.config(text=result)

    action_button = Button(root, text="Nyomj meg gyorsan!", command=on_button_click)
    action_button.pack(pady=20)


    output_label = Label(root, text="")
    output_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()