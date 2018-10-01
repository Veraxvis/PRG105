def main():
    avg = 0
    inti = 1
    input_file = open('numbers.txt', 'r')
    record = input_file.readline()
    record = record.rstrip('\n')
    print('#' + str(inti), record)
    while record != "":
        record = input_file.readline()
        record = record.rstrip('\n')
        inti += 1
        if record != "":
            print('#' + str(inti), record)
            avg += int(record)
        if record == "":
            print("The average of all the numbers is: " + '{:.2f}'.format(avg / (inti - 1)))
    input_file.close()


main()
