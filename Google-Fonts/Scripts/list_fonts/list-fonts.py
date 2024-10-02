import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv('GOOGLE_FONTS_API')

url = f'https://www.googleapis.com/webfonts/v1/webfonts?key={api_key}'

response = requests.get(url)

fonts_data = response.json()

hebrew_fonts = [font for font in fonts_data['items'] if 'hebrew' in font['subsets']]

current_date = datetime.now().strftime("%d%m%y")

filename = f'google_fonts_hebrew_{current_date}.md'

with open(filename, 'w') as file:
    file.write("# Google Fonts In Hebrew\n\n")
    file.write(f"## Generated: {datetime.now().strftime('%d-%m-%y')}\n\n")
    
    for font in hebrew_fonts:
        font_name = font['family']
        font_link = font['files'].get('regular', list(font['files'].values())[0])
        file.write(f"# {font_name}\n[Link]({font_link})\n\n")

print(f"Markdown file '{filename}' has been created.")