with open('shared_workspace/sort_of_clevr/transformers.py', 'r') as f1, open('shared_workspace/Triangle/transformers.py', 'r') as f2:
    # Read the lines of the files
    file1_lines = f1.readlines()
    file2_lines = f2.readlines()

# Compare the lines of the files
for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines)):
    if line1 != line2:
        print(f"Line {i+1} is different:")
        print(f"File 1: \"{line1.strip()}\"")
        print(f"File 2: \"{line2.strip()}\"")