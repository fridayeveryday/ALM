path_in = "C:\input.txt"
path_out = "C:\output.txt"


def main():
    fill_cycle_list(fileIn=open(path_in, 'r+'), fileOut=open(path_out, 'w+'))


def fill_cycle_list(fileIn, fileOut):
    counter, condition, increament = '', '', ''
    num_of_for = 0
    for read_str in fileIn:
        tab_str = "\t" * num_of_for
        if "for (" in read_str or "for(" in read_str:
            # get from the line counter, condition, increament of cycle
            counter, condition, increament = read_cycle_start(read_str)
            read_str = tab_str + counter + ";\n" + tab_str + "while({})".format(condition) + "{\n"
            num_of_for += 1
        else:
            if "}" in read_str:
                num_of_for -= 1
                read_str = tab_str + increament + ";" + "\n" + "\t" * num_of_for + "}\n"
        fileOut.writelines(read_str)


def read_cycle_start(start_cycle_str):
    cycle_counter = start_cycle_str[start_cycle_str.find("(") + 1: start_cycle_str.find(";")].strip()
    cycle_condition = start_cycle_str[start_cycle_str.find(";") + 1:start_cycle_str.rfind(";")].strip()
    cycle_increament = start_cycle_str[start_cycle_str.rfind(";") + 1:start_cycle_str.rfind(")")].strip()
    return cycle_counter, cycle_condition, cycle_increament


if __name__ == '__main__':
    main()
