path_in = "C:\input.txt"
path_out = "C:\output.txt"


def main():
    fill_cycle_list(fileIn=open(path_in, 'r+'), fileOut=open(path_out, 'w+'))


def fill_cycle_list(fileIn, fileOut):
    counter, condition, increment = '', '', ''
    num_of_for = 0
    read_str = fileIn.readline()
    while read_str:
        tab_str = "\t" * num_of_for
        if "for (" in read_str or "for(" in read_str:
            # get from the line counter, condition, increament of cycle
            counter, condition, increment = read_cycle_start(read_str)
            read_str = tab_str + counter + ";\n" + tab_str + "while({})".format(condition) + "{\n"
            num_of_for += 1
        else:
            if "}" in read_str:
                num_of_for -= 1
                read_str = tab_str + increment + ";" + "\n" + "\t" * num_of_for + "}\n"
        fileOut.writelines(read_str)
        read_str = fileIn.readline()


def read_cycle_start(start_cycle_str):
    cycle_counter = start_cycle_str[start_cycle_str.find("(") + 1: start_cycle_str.find(";")].strip()
    cycle_condition = start_cycle_str[start_cycle_str.find(";") + 1:start_cycle_str.rfind(";")].strip()
    cycle_increment = start_cycle_str[start_cycle_str.rfind(";") + 1:start_cycle_str.rfind(")")].strip()
    return cycle_counter, cycle_condition, cycle_increment


if __name__ == '__main__':
    main()
