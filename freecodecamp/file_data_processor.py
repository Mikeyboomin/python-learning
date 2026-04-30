def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            lines = contents.split('\n')
            total = 0
            for line in lines:
                total += int(line)
            print(f"Total: {total}")
    except FileNotFoundError:
        print(f"{filename} not found.")
        return
    except ValueError:
        print(f"Invalid data found in {filename}.")
        return

process_file("numbers.txt")
process_file("missing.txt")
process_file("corrupt.txt")