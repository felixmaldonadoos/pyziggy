from getlinks import GetLinks
import subprocess
from downloader import Downloader
from asciiart import AsciiArt
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

def intro(header="PyZiggy"):
    # AsciiArt(header, font="tinker-toy").display()
    print('')
    AsciiArt(header, font="basic").display()
    print("\nWelcome to the Zig downloader!")
    print("This program will help you download Zig for your system.")
    print("Let's get started!\n")
    print("Author: Alexander Maldonado (felixmaldonado2023@u.northwestern.edu)")
    print("Date: 08-02-2024")

if __name__=='__main__':
    
    # start app 
    app = App()
    app.intro = intro
    
    # run
    choices = app.run_selector()
    url = 'https://ziglang.org/download/'
    gl = GetLinks(url)
    gl.run()
    
    my_urls = None
    if choices:
        my_urls = gl.get_download_url(url_list=None, 
                        os=choices['os'], 
                        architecture=choices['architecture'], 
                        has_signature=choices['has_signature'], 
                        latest_version=choices['latest_version'])
    
    # check if urls are found and exit if not    
    if not my_urls or len(my_urls) == 0: 
        print("No urls found, exiting...")
        exit()

    # if found: display urls to download 
    while True:
        app.display_url_menu(my_urls)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if 1 <= choice <= len(my_urls):
            selected_url = my_urls[choice - 1][0]
            if app.download_url(selected_url): print("Download successful!")
            else: print("Download failed.")
            break
        elif choice == len(my_urls) + 1:
            print("Quitting...")
            break
        else:
            print("Invalid choice, please try again.")
            
    app.outro()