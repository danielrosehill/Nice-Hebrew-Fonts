import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GOOGLE_FONTS_API')

url = f'https://www.googleapis.com/webfonts/v1/webfonts?key={api_key}'

response = requests.get(url)
fonts_data = response.json()

hebrew_fonts = [font for font in fonts_data['items'] if 'hebrew' in font['subsets']]

os.makedirs('downloaded_fonts', exist_ok=True)

with open('list.md', 'w') as file:
    for font in hebrew_fonts:
        font_name = font['family']
        font_link = font['files'].get('regular', list(font['files'].values())[0])
        
        response = requests.get(font_link)
        if response.status_code == 200:
            font_filename = f"downloaded_fonts/{font_name.replace(' ', '_')}.ttf"
            with open(font_filename, 'wb') as font_file:
                font_file.write(response.content)
        
        file.write(f"# {font_name}\n[Link]({font_link})\n\n")

print("Markdown file 'list.md' and fonts have been downloaded.")