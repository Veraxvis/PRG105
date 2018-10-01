def main():
    input_file = open('names.txt', 'r')
    record = input_file.readline()
    x = 1
    print('#' + str(x), record)
    while record != "":
        record = input_file.readline()
        x += 1
        if record != "":
            print('#', x, record)

    input_file.close()


main()
