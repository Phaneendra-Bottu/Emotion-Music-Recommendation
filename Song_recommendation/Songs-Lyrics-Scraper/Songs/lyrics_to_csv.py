import csv
import re

# Dictionary to map file names to artist names
file_to_artist_map = {
    'lyrics_scraped.txt': 'Ed Sheeran',
    'lyrics_scraped2.txt': 'Eminem',
    'lyrics_scraped3.txt': 'Taylor Swift',
    'lyrics_scraped4.txt': 'Rihanna',
    'lyrics_scraped5.txt': 'Ariana Grande',
    'lyrics_scraped6.txt': 'Coldplay',
    'lyrics_scraped7.txt': 'Lana Del Rey',
    'lyrics_scraped8.txt': 'Maroon 5',
    'lyrics_scraped9.txt': 'Michael Jackson',
    'lyrics_scraped10.txt': 'One Direction'
}

# Initialize lists to store artist names, song names, and lyrics
artist_names = []
song_names = []
lyrics_list = []

# List of input files
input_files = [
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped2.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped3.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped4.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped5.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped6.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped7.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped8.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped9.txt',
    'Songs-Lyrics-Scraper/Songs/lyrics_scraped10.txt'
]

# Read content from each file
for file_path in input_files:
    # Extract the file name to use in the dictionary lookup
    file_name = file_path.split('/')[-1]
    
    # Get artist name from the dictionary using the file name
    artist_name = file_to_artist_map.get(file_name, 'Unknown Artist')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Use regex to find all song names and their corresponding lyrics
    songs = re.findall(r'###"(.+?)"###\s*(.*?)\s*(?=###"|$)', content, re.DOTALL)

    # Append artist name, song names, and lyrics to the respective lists
    for song in songs:
        song_names.append(song[0])
        # Remove unwanted commas, new lines, and redundant quotes, making lyrics a single line
        cleaned_lyrics = song[1].replace('\n', ' ').replace(',', '').replace('"', '').strip()
        lyrics_list.append(cleaned_lyrics)
        artist_names.append(artist_name)

# Write the extracted data into a CSV file
with open('lyrics_CSV.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Artist Name', 'Song Name', 'Lyrics'])  # Writing header
    for artist, name, lyrics in zip(artist_names, song_names, lyrics_list):
        # Escape any quotes in song names
        name = name.replace('"', '""')
        writer.writerow([artist, name, lyrics])

print("Lyrics have been successfully written to main_CSV.csv")
