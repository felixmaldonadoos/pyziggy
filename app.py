import subprocess
from downloader import Downloader

"""
This program keeps track of all of our books
version : 2.0.0
Date :15.05.2022
"""

class App:
    def __init__(self):
        self.choices = {
            'os': None, 
            'architecture': None,
            'has_signature': None, 
            'latest_version': None,
        }
        self.default_choices = {
            'os': 'linux', 
            'architecture': 'x86_64',
            'has_signature': True, 
            'latest_version': True,
        }
        self.options = {
            'os': ['linux', 'windows', 'macos'],
            'architecture': ['x86_64', 'arm64', 'armv6', 'armv7', 'armv8'],
            'has_signature': [True, False],
            'latest_version': [True, False],
        }
        
        self.intro = None
        self.download_url = Downloader().download_url

    def display_main_menu(self):
        print("*** Select value to set ***")
        print("0) Use default values")
        for index, key in enumerate(self.choices.keys(), start=1):
            status = f"(OK - {self.choices[key]})" if self.choices[key] is not None else ""
            print(f"{index}) {key} {status}")
        print(f"{len(self.choices) + 1}) Continue")
        print(f"{len(self.choices) + 2}) Quit")

    def display_options_menu(self, key):
        options = self.options[key]
        print(f"Select an option for {key}:")
        for index, option in enumerate(options, start=1):
            print(f"{index}) {option}")

    def set_default_choices(self):
        for key in self.choices:
            self.choices[key] = self.default_choices[key]

    def run_selector(self,debug:bool=False)->dict:
        if self.intro: 
            self.intro()
        if debug: 
            print("Running in debug mode")
            return self.default_choices
        while True:
            self.display_main_menu()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input, please enter a number.")
                continue

            if choice == 0:
                self.set_default_choices()
                print("Default values have been set.")
            elif choice == len(self.choices) + 1:
                if all(value is not None for value in self.choices.values()):
                    print("Continuing with current choices...")
                    break
                else:
                    print("Please set all values or use default values.")
            elif choice == len(self.choices) + 2:
                print("Quitting...")
                return None
            elif 1 <= choice <= len(self.choices):
                selected_key = list(self.choices.keys())[choice - 1]

                if self.options[selected_key] is not None:
                    self.display_options_menu(selected_key)
                    try:
                        sub_choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Invalid input, please enter a number.")
                        continue

                    if 1 <= sub_choice <= len(self.options[selected_key]):
                        self.choices[selected_key] = self.options[selected_key][sub_choice - 1]
                    else:
                        print("Invalid choice, please try again.")
                else:
                    new_value = input(f"Enter new value for {selected_key}: ")
                    self.choices[selected_key] = new_value
            else:
                print("Invalid choice, please try again.")

        print("Final choices:", self.choices)
        return self.choices
    
    def outro(self):
        print("Thank you for using the Zig downloader!")
    
    def display_url_menu(self, urls):
        print("*** Select URL to download ***")
        for index, (url, _) in enumerate(urls, start=1):
            print(f"{index}) {url}")
        print(f"{len(urls) + 1}) Quit")