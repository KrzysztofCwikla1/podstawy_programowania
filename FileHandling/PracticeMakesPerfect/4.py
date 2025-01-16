def display_file_in_chunks(filename):
    with open(filename, 'r') as file:
        while True:
            lines = []
            i = 0
            while i < 5:
                line = file.readline().strip()
                if not line:
                    break
                lines.append(line)
                i += 1
            if not lines:  # Break when there are no more lines
                break
            print("\n".join(lines))
            input("Press Enter key...")

display_file_in_chunks('FileHandling\\PracticeMakesPerfect\\it_company.csv')
