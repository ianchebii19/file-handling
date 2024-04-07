def write_to_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("I'm Ian Chebii\n")
            file.write("Programming student\n")
            file.write("I'm going to Make it\n")
        print("Data has been written to", filename)
    except FileNotFoundError:
        print("Error: File not found or path is incorrect.")
    except PermissionError:
        print("Error: Permission denied to write to file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("File writing process completed.")


def read_and_display(filename):
    try:
        with open(filename, 'r') as file:
            print("Contents of", filename + ":")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: File not found or path is incorrect.")
    except PermissionError:
        print("Error: Permission denied to read the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)


def append_to_file(filename):
    try:
        with open(filename, 'a') as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("Data has been appended to", filename)
    except FileNotFoundError:
        print("Error: File not found or path is incorrect.")
    except PermissionError:
        print("Error: Permission denied to append to the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("File appending process completed.")


if __name__ == "__main__":
    filename = "my_file.txt"

    write_to_file(filename)
    read_and_display(filename)
    append_to_file(filename)
