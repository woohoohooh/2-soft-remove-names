import os
import re

folder = r"C:\путь\к\папке"

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)

    if os.path.isfile(old_path):
        new_filename = re.sub(r"-(Charon|Zephyr)", "", filename)

        if new_filename != filename:
            new_path = os.path.join(folder, new_filename)
            os.rename(old_path, new_path)
            print(f"{filename} -> {new_filename}")