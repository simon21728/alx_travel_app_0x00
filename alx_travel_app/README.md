import os

readme_path = "README.md"

if os.path.isfile(readme_path) and os.path.getsize(readme_path) > 0:
    print("README file exists and is not empty ")
else:
    print("README file is missing or empty ")
