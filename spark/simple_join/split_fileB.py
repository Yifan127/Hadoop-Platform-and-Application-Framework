def split_fileB(line):
    # split the input line in word and count on the comma
    key_value = line.split(",")
    date_word = key_value[0].split(" ")
    date = date_word[0]
    word = date_word[1]
    # turn the count to an integer
    count_string = key_value[1]
    return (word, date + " " + count_string)

test_line = "Jan-01 able,5"
split_fileB(test_line)