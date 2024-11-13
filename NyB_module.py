from datetime import datetime


class NyBClass:
    def __init__(self):
        self.message = ""

    def get_message(self):
        return self.message


def nyb_function():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Pontos dátum és idő {formatted_time}")
    return formatted_time