day1_file = open("um-deliveries-20140519.txt")
day2_file = open("um-deliveries-20140520.txt")
day3_file = open("um-deliveries-20140521.txt")
all_files = [day1_file, day2_file, day3_file]


def turn_files_into_pretty_text(text_files):
    """takes list of files as parameter, prints out readible version

    Fn strips each file by line, gets rid of duplicates, then splits the line
    into usable chunks before printing out the usable version"""
    list_of_all_lines = []
    for item in text_files:
        for line in item:
            line = line.rstrip()
            if line not in list_of_all_lines:
                list_of_all_lines.append(line)
    return list_of_all_lines


def prints_pretty_data(list_of_strings):
    """takes list of strings, splits it, prints pretty looking data""" 
    for item in list_of_strings:

        words = item.split('|')
        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(count, melon, amount)

prints_pretty_data(turn_line_into_list(all_files))

### There are two ways to write this--as one

