from bs4 import BeautifulSoup
import os
file_name = input("Enter the name of the HTML file (with .html extension): ")
# Load your HTML file
with open(file_name, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all <a> tags (hyperlinks)
links = soup.find_all("a")

# Create a list of [title, link] pairs
link_info = []
for link in links:
    title = link.get_text(strip=True)
    href = link.get("href")
    if title and href:
        link_info.append([title, href])

# Example: print all link entries
for item in link_info:
    print(item)



# Folder to save the .url files
output_folder = "shortcuts"
os.makedirs(output_folder, exist_ok=True)

# Save each item as a .url file
for i, (title, url) in enumerate(link_info, start=1):
    # Clean filename to avoid invalid characters
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    filename = f"{safe_title}.url"
    filepath = os.path.join(output_folder, filename)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write("[InternetShortcut]\n")
        file.write(f"URL={url}\n")

    print(f"Saved: {filepath}")