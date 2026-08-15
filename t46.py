import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? (YYYY-MM-DD): ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")

song_spans = soup.select("li ul li h3#title-of-a-story")
song_names = [song.getText().strip() for song in song_spans]

# Save to a text file
with open("t46billboard_top_100.txt", "w", encoding="utf-8") as file:
    for song in song_names:
        file.write(f"{song}\n")

print(f"Successfully saved {len(song_names)} songs to billboard_top_100.txt!")