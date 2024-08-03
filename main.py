from asciiart import AsciiArt
from getlinks import GetLinks
from app import App

def intro(header="PyZiggy"):
    # AsciiArt(header, font="tinker-toy").display()
    print('')
    AsciiArt(header, font="basic").display()
    print("\nWelcome to the Zig downloader!")
    print("This program will help you download Zig for your system.")
    print("Let's get started!\n")
    print("Author: Alexander Maldonado (felixmaldonado2023@u.northwestern.edu)")
    print("Date: 08-02-2024")
    print("")

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