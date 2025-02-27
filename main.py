import os
import shutil
import time
import pandas as pd

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def normalize_file(file_path):
    """ Normalize attributes in a CSV file (e.g., standardizing column names, formats) """
    df = pd.read_csv(file_path)

    # Example: Convert column names to lowercase
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Example: Convert date formats (if a 'date' column exists)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.strftime("%Y-%m-%d")

    # Save processed file
    new_file_path = os.path.join(PROCESSED_FOLDER, os.path.basename(file_path))
    df.to_csv(new_file_path, index=False)
    return new_file_path

def upload_file(file_path):
    """ Upload a file for processing """
    if not os.path.exists(file_path):
        print("File not found!")
        return
    
    dest_path = os.path.join(UPLOAD_FOLDER, os.path.basename(file_path))
    shutil.copy(file_path, dest_path)
    print(f" File uploaded: {dest_path}")

    # Normalize file
    processed_file = normalize_file(dest_path)
    print(f" File normalized: {processed_file}")

def list_files(folder):
    """ List files in a folder """
    files = os.listdir(folder)
    if files:
        for file in files:
            print(f" {file}")
    else:
        print(" No files found.")

def main():
    while True:
        print("\n Attribute Normalization System 🔹")
        print("1️ Upload & Normalize File")
        print("2️ List Uploaded Files")
        print("3️ List Processed Files")
        print("4️ Exit")
        choice = input("Select an option: ")

        if choice == "1":
            file_path = input("Enter file path to upload: ").strip()
            upload_file(file_path)
        elif choice == "2":
            print("\n Uploaded Files:")
            list_files(UPLOAD_FOLDER)
        elif choice == "3":
            print("\n Processed Files:")
            list_files(PROCESSED_FOLDER)
        elif choice == "4":
            print(" Exiting... ")
            break
        else:
            print(" Invalid choice! Try again.")

if __name__ == "__main__":
    main()
