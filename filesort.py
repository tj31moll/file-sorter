import os
import shutil
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Define the categories and subcategories
categories = {
    'Programs': ['.exe', '.msi', '.dmg'],
    'Operating System Install': ['.iso'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Video': ['.mp4', '.mov', '.avi', '.mkv'],
    'Compressed': ['.zip', '.rar', '.7z'],
    'Emails': ['.eml'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.odt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv']
}

# Define the subcategories
subcategories = {
    'Programs': ['Browsers', 'Microsoft Office', 'Adobe Creative Suite'],
    'Operating System Install': ['Windows', 'MacOS', 'Linux'],
    'Images': ['Wallpapers', 'Screenshots', 'Photographs'],
    'Audio': ['Music', 'Podcasts', 'Audiobooks'],
    'Video': ['Movies', 'TV Shows', 'Youtube Videos'],
    'Compressed': ['Software Downloads', 'Backups'],
    'Emails': ['Inbox', 'Sent', 'Spam'],
    'Documents': ['Resumes', 'Invoices', 'Reports']
}

# Get the current working directory
cwd = os.getcwd()

# Initialize the count vectorizer and decision tree classifier
vectorizer = CountVectorizer()
clf = DecisionTreeClassifier()

# Train the classifier on the documents in the Documents category
documents_dir = os.path.join(cwd, 'Documents')
documents = []
labels = []
for subcategory in subcategories['Documents']:
    subcategory_dir = os.path.join(documents_dir, subcategory)
    for filename in os.listdir(subcategory_dir):
        file_path = os.path.join(subcategory_dir, filename)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            document = f.read()
            documents.append(document)
            labels.append(subcategory)

X = vectorizer.fit_transform(documents)
y = labels
clf.fit(X, y)

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

            # Get the file content and predict the subcategory using the trained classifier
            file_path = os.path.join(cwd, filename)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                document = f.read()
                X_test = vectorizer.transform([document])
                subcategory = clf.predict(X_test)[0]

            # Create the subcategory directory if it doesn't exist
            subcategory_dir = os.path.join(category_dir, subcategory)
            if not os.path.exists(subcategory_dir):
                os.makedirs(subcategory_dir)

            # Move the file to the subcategory directory
            shutil.move(file_path, os.path.join(subcategory_dir, filename))
