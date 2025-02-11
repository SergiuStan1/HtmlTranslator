import os
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Directory containing the .html files
directory = 'd:/LoyaltyHub'

# Directories to exclude from translation
exclude_dirs = ['node_modules', 'dist']

# Function to translate text
def translate_text(text, dest_language='ro'):
    return translator.translate(text, dest=dest_language).text

# Function to translate HTML file
def translate_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Translate the content
    translated_content = translate_text(content)
    
    # Write the translated content back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(translated_content)

# Iterate over all .html files in the directory
for root, dirs, files in os.walk(directory):
    # Skip excluded directories
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    for file in files:
        if file.endswith('.html') and 'component' in file:
            filepath = os.path.join(root, file)
            translate_html_file(filepath)
            print(f'Translated {filepath}')