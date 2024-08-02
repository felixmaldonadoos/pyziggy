import requests
import re

# URL of the Zig download page
url = 'https://ziglang.org/download/'

try:
    # Fetch the HTML content of the Zig download page
    response = requests.get(url)
    response.raise_for_status()
    page_content = response.text
    
    print(f"Page content: {page_content}\n ========= \n")
    # Regex pattern to find the latest Linux x86_64 release link (excluding the master branch)
    # pattern = r'([a-z0-9]+(-[a-z0-9]+)+_64)-[0-9]+\.[0-9]+\.[0-9]+\.tar\.xz'
    pattern = r'href=(https://ziglang\.org/builds[^>]+\.tar\.xz)>'

    # Find all matching links
    
    matches = re.findall(pattern, page_content)
    # print(f'Matches: \n {np.array(matches).T}\n')

    # Filter out any links containing "master"
    matches = [match for match in matches if "master" not in match]
    for match in matches:
        print(f"match: {match}")
        

    # Check if any matches were found
    if not matches:
        print("No latest Zig release found for Linux x86_64.")
    else:
        # Take the first match as the latest version
        latest_link = matches[0]
        full_link = f"https://ziglang.org{latest_link}"
        print(f"Latest Zig release for Linux x86_64: {full_link}")

except requests.RequestException as e:
    print(f"Error fetching the page: {e}")
