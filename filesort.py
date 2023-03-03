import os
import shutil
import re

# Define the categories and subcategories
categories = {
    'Browser': ['.exe', '.dmg'],
    'Programs': ['.msi', '.dmg', '.pkg'],
    'Operating System Install': ['.iso'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Video': ['.mp4', '.mov', '.avi', '.mkv'],
    'Compressed': ['.zip', '.rar', '.7z'],
    'Emails': ['.eml', '.msg'],
}

# Define the subcategories
subcategories = {
    'Browser': ['Chrome', 'Firefox', 'Safari', 'Opera'],
    'Programs': ['Microsoft Office', 'Adobe Creative Suite', 'Productivity', 'Media'],
    'Operating System Install': ['Windows', 'MacOS', 'Linux'],
    'Documents': ['Resumes', 'Invoices', 'Reports', 'School Work', 'Personal'],
    'Images': ['Wallpapers', 'Screenshots', 'Photographs', 'Icons'],
    'Audio': ['Music', 'Podcasts', 'Audiobooks'],
    'Video': ['Movies', 'TV Shows', 'Youtube Videos'],
    'Compressed': ['Software Downloads', 'Backups'],
    'Emails': ['Work', 'Personal'],
}

# Get the current working directory
cwd = os.getcwd()

# Loop through all files in the current working directory
for filename in os.listdir(cwd):
    file_extension = os.path.splitext(filename)[1]

    # Check if the file extension matches a category
    for category, extensions in categories.items():
        if file_extension in extensions:
            # Create the category directory if it doesn't exist
            category_dir = os.path.join(cwd, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

            # Determine the subcategory based on file contents
            subcategory = None
            if category == 'Browser':
                for browser in subcategories['Browser']:
                    if browser.lower() in filename.lower():
                        subcategory = browser
                        break
            elif category == 'Emails':
                with open(os.path.join(cwd, filename), 'r') as f:
                    contents = f.read()
                    for email in subcategories['Emails']:
                        if email.lower() in contents.lower():
                            subcategory = email
                            break

            # If the subcategory is not determined by file contents, choose a default subcategory
            if not subcategory:
                subcategory = subcategories[category][0]

            # Create the subcategory directory if it doesn't exist
            subcategory_dir = os.path.join(category_dir, subcategory)
            if not os.path.exists(subcategory_dir):
                os.makedirs(subcategory_dir)

            # Move the file to the subcategory directory
            file_path = os.path.join(cwd, filename)
            new_file_path = os.path.join(subcategory_dir, filename)
            shutil.move(file_path, new_file_path)
