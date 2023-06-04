# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

class2id = {'dirt': 0, 'business_cards': 1, 'keys': 2, 'other': 3, 'paper_and_notebooks': 4, 'pens': 5, 'rulers': 6,
            'scissors': 7,
            'tapes': 8, 'usb_sticks': 9}


def process_file(filename):
    # Open the input file
    with open(filename, 'r') as file:
        # Read the content
        lines = file.readlines()
    modified_lines = []
    for line in lines:
        line_list = line.split()
        x = (int(line_list[1]) + int(line_list[3])) / (2.0 * 1280)
        y = (int(line_list[2]) + int(line_list[4])) / (2.0 * 1024)
        w = abs(((int(line_list[3]) - int(line_list[1])) / 1280))
        h = abs(((int(line_list[4]) - int(line_list[2])) / 1024))
        c = class2id[line_list[5]]
        newlist = [c, x, y, w, h]
        modified_line = ' '.join(str(element) for element in newlist) + '\n'
        modified_lines.append(modified_line)
    # Save the modified content back to the file
    with open(filename, 'w') as file:
        file.writelines(modified_lines)


def batch_process_files(directory):
    # Get a list of all files in the directory
    files = sorted(os.listdir(directory))

    # Process each file in the directory
    for filename in files:
        # Check if the file is a text file
        if filename.endswith(".txt"):
            # Get the full path of the file
            file_path = os.path.join(directory, filename)

            # Process the file
            process_file(file_path)

    print("Batch processing complete!")


# Usage example
batch_process_files('/Users/jiamingyu/Desktop/ultralytics-main/datasets/dirtdtataset/train/labels1')
