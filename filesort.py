import os 
import shutil 

# Define the categories and subcategories 
categories = { 
    'Programs': ['.exe', '.msi', '.dmg'], 
    'Documents': ['.doc', '.docx', '.pdf', '.txt'], 
    'Images': ['.jpg', '.jpeg', '.png', '.gif'], 
    'Audio': ['.mp3', '.wav', '.aac'], 
    'Video': ['.mp4', '.mov', '.avi', '.mkv'], 
    'Compressed': ['.zip', '.rar', '.7z'], 
}

subcategories = { 
    'Programs': ['Browsers', 'Microsoft Office', 'Adobe Creative Suite'], 
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
    file_path = os.path.join(cwd, filename)

    # Check if the file extension matches a category 
    for category, extensions in categories.items():
        if file_extension in extensions:
            # Create the category directory if it doesn't exist 
            category_dir = os.path.join(cwd, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

            # If the category is 'Programs', add a subcategory directory 
            if category == 'Programs':
                program_name = None

                # Check if the file is a browser and assign it to the 'Browsers' subcategory 
                for line in open(file_path, 'rb'):
                    if b'Chrome' in line:
                        program_name = 'Chrome'
                        break
                    elif b'Firefox' in line:
                        program_name = 'Firefox'
                        break
                    elif b'Safari' in line:
                        program_name = 'Safari'
                        break
                    elif b'Opera' in line:
                        program_name = 'Opera'
                        break

                if program_name is not None:
                    subcategory_dir = os.path.join(category_dir, 'Browsers', program_name)
                    if not os.path.exists(subcategory_dir):
                        os.makedirs(subcategory_dir)
                else:
                    # Otherwise, assign it to the 'Programs' subcategory 
                    subcategory_dir = os.path.join(category_dir, subcategories[category][0])
                    if not os.path.exists(subcategory_dir):
                        os.makedirs(subcategory_dir)
            else:
                # For other categories, assign the file to the first subcategory 
                subcategory_dir = os.path.join(category_dir, subcategories[category][0])
                if not os.path.exists(subcategory_dir):
                    os.makedirs(subcategory_dir)

            # Move the file to the subcategory directory 
            new_file_path = os.path.join(subcategory_dir, filename) 
            shutil.move(file_path, new_file_path)
