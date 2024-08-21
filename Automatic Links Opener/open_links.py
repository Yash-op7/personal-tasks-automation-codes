import webbrowser
import re

def open_links_from_text(file_path):
    # Regular expression to match URLs
    url_regex = re.compile(r'https?://[^\s]+')

    with open(file_path, 'r') as file:
        content = file.read()

    # Find all URLs in the text
    urls = url_regex.findall(content)

    # Open each URL in the default web browser
    for url in urls:
        webbrowser.open(url)

# Path to your text file with links
text_file_path = 'currently_doing.txt'

# Call the function
open_links_from_text(text_file_path)
