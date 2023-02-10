import os
import shutil

# Define the categories and subcategories
categories = {
    'Browser': ['.exe', '.dmg'],
    'Programs': ['.msi', '.dmg'],
    'Operating System Install': ['.iso'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Video': ['.mp4', '.mov', '.avi', '.mkv'],
    'Compressed': ['.zip', '.rar', '.7z'],
}

# Define the subcategories
subcategories = {
    'Browser': ['Chrome', 'Firefox', 'Safari', 'Opera'],
    'Programs': ['Microsoft Office', 'Adobe Creative Suite'],
    'Operating System Install': ['Windows', 'MacOS', 'Linux'],
    'Documents': ['Resumes', 'Invoices', 'Reports'],
    'Images': ['Wallpapers', 'Screenshots', 'Photographs'],
    'Audio': ['Music', 'Podcasts', 'Audiobooks'],
    'Video': ['Movies', 'TV Shows', 'Youtube Videos'],
    'Compressed': ['Software Downloads', 'Backups'],
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

            # Loop through the subcategories for this category
            for subcategory in subcategories[category]:
                subcategory_dir = os.path.join(category_dir, subcategory)
                if not os.path.exists(subcategory_dir):
                    os.makedirs(subcategory_dir)

                # Move the file to the subcategory directory
                file_path = os.path.join(cwd, filename)
                new_file_path = os.path.join(subcategory_dir, filename)
                shutil.move(file_path, new_file_path)

