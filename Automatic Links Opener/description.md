# 🝡 Use Case
If you have a large text files with a bunch of links and you to wish to open all or some of them in a browser, instead of manually clicking each one of them you can just configure and run this python script.

# ∵ Why I made it
I found an article on LinkedIn about topic wise must do leetcode questions and I wanted to go through each link and solve the ones that I haven't already but the article was huge and I didn't want to open problem link manually so I made this.

# ⚙️ Steps to use
1. Install dependencies:
    - Ensure python and pip is installed
    - Run this: `​pip3 install webbrowser`

2. Paste your text with embedded links in the links.txt file or create it
3. Run: python3 open_links.py

# ❗️ Note
- The webbrowser.open(url) command will open each URL in a new tab. Depending on your browser settings, opening too many tabs at once may slow down your browser or computer.
- Be cautious about the number of links you are opening simultaneously. Consider adding a delay between openings if necessary, using time.sleep(seconds) from the time module.
- Ensure your system's default browser settings are configured according to your preferences, like default browsre.
