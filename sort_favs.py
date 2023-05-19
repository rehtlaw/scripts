# Put this file into your profile's folder (the same one containing favorites.txt) and run it.
# It will back up the original file in case something goes horribly wrong.

import os


class Line:
    index: int = 0
    content_sort: str = ""
    content_full: str = ""

    def __init__(self, index, content_full):
        self.index = index
        self.content_full = content_full


def cut_out_the_bs(input: str):
    folder_name = input.split("/", 1)[1].lower()
    no_brackets = folder_name[folder_name.index(
        "]") + 1:] if folder_name.startswith("[") else folder_name
    no_parens = no_brackets[no_brackets.index(
        ")") + 1:] if no_brackets.startswith("(") else no_brackets
    fixed_input = no_parens.lstrip()
    return fixed_input


lines_list = []

os.rename("favorites.txt", "favorites.txt.bak")

with open("favorites.txt.bak", "r") as file:
    all_lines = file.readlines()
    for i in range(len(all_lines)):
        newline = Line(i, all_lines[i])
        newline.content_sort = cut_out_the_bs(newline.content_full)
        lines_list.append(newline)

sorted_lines = sorted(lines_list, key=(lambda x: x.content_sort))

with open("favorites.txt", "w") as file:
    for line in sorted_lines:
        file.write(line.content_full)

print("Old favourites file has been renamed to \'favorites.txt.bak\', in case something went horribly wrong.")
