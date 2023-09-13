import os
from typing import List


class Line:
    index: int = 0
    content_sort: str = ""
    content_full: str = ""

    def __init__(self, index, content_full):
        self.index = index
        self.content_full = content_full


def cut_out_the_bs(input: str):
    # not very nice way to get rid of the months in THC but it'll do
    months: List[str] = ["1 jan", "2 feb", "3 mar", "4 apr", "5 may", "6 jun",
                         "7 jul", "8 aug", "9 sep", "10 oct", "11 nov", "12 dec"]
    folder_name = input.split("/", 1)[1].lower()
    no_thc_month = ""
    m: str
    for m in months:
        if m in folder_name:
            no_thc_month = folder_name[len(m) + 3:]
            break
        else:
            no_thc_month = folder_name
    no_jayce = no_thc_month[13:] if no_thc_month.startswith("(-[jayce]-) -") else no_thc_month 
    no_parens = no_jayce[no_jayce.index(
        ")") + 1:] if no_jayce.startswith("(") and not no_jayce.endswith(")") else no_jayce
    no_dashes = no_parens[no_parens.index(
        "-") + 1:] if no_parens.startswith("-") and not no_parens.endswith("-") else no_parens
    no_brackets = no_dashes[no_dashes.index(
        "]") + 1:] if no_dashes.startswith("[") and not no_dashes.endswith("]") else no_dashes
    no_brackets = no_brackets.lstrip()
    no_brackets2 = no_brackets[no_brackets.index(
        "]") + 1:] if no_brackets.startswith("[") and not no_brackets.endswith("]") else no_brackets
    fixed_input = no_brackets2.lstrip()

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
