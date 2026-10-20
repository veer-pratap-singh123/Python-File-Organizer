import os
import shutil

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Error: Folder does not exist!")

else:
    count = 0

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            extension = os.path.splitext(file)[1][1:].lower()

            if extension == "":
                extension = "Others"

            new_folder = os.path.join(folder, extension)
            os.makedirs(new_folder, exist_ok=True)

            shutil.move(path, os.path.join(new_folder, file))
            count += 1

    print(f"Successfully organized {count} files!")
