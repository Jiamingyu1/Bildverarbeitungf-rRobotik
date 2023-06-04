# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def split_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into columns
            columns = line.split()

            if len(columns) > 0:
                # Extract the first column
                first_column = columns[0]

                # Open the output file for the current first column value
                output_file = open(first_column + '.txt', 'a')

                # Write the line to the corresponding output file
                output_file.write(line)

                # Close the output file
                output_file.close()

    print("Splitting complete!")

# Usage example
split_file('bbox_labels.txt')



