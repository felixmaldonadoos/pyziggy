class Configurator:
    def __init__(self):
        self.choices = {
            'os': None, 
            'architecture': None,
            'has_signature': None, 
            'latest_version': None,
        }
        self.options = {
            'os': ['linux', 'windows', 'macos'],
            'architecture': ['x86_64', 'arm64', 'armv6', 'armv7', 'armv8'],
            'has_signature': [True, False],
            'latest_version': [True, False],
        }

    def display_main_menu(self):
        print("*** Select value to set ***")
        for index, key in enumerate(self.choices.keys(), start=1):
            status = f"(OK - {self.choices[key]})" if self.choices[key] is not None else ""
            print(f"{index}) {key} {status}")
        print(f"{len(self.choices) + 1}) Quit")

    def display_options_menu(self, key):
        options = self.options[key]
        print(f"Select an option for {key}:")
        for index, option in enumerate(options, start=1):
            print(f"{index}) {option}")

    def run(self):
        found_all = False

        while not found_all:
            self.display_main_menu()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input, please enter a number.")
                continue

            if choice == len(self.choices) + 1:
                print("Quitting...")
                break
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

                # Check if all values are set (none of them is None)
                found_all = all(value is not None for value in self.choices.values())

                if found_all:
                    print("All values have been set.")
            else:
                print("Invalid choice, please try again.")

        print("Final choices:", self.choices)

if __name__ == "__main__":
    configurator = Configurator()
    configurator.run()
