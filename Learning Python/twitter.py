import re

url = input("URL: ").strip()

'''
username = url.replace("https://twitter.com", "")
print(f"username: {username}")
'''

'''
username = url.removeprefix("https://twitter.com/")
print(f"username: {username}")
'''

'''
username = re.sub(r"^(https://)?(www\.)?twitter.com/", "", url)
print(f"Username: {username}")
'''

'''
matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))
'''

'''
matches = re.search(r"^https?://(www\.)?twitter\.com/([a-z0-9])", re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))
'''

