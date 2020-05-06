state_string = "We are at the {} state.\nCondition/output:{}/{}\n\n"


def main():
    file_log = open("C:\logMealy.txt","w+")

    # Y1,S0

    print(state_string.format('S0', '1', 'Y1'))
    file_log.write(state_string.format('S0', '1', 'Y1'))

    path_in = "C:\input.txt"
    path_out = "C:\output.txt"
    file_in = open(path_in, "r+")
    file_out = open(path_out, "w+")
    counter, condition, increment = '', '', ''
    num_of_for = 0
    read_str = file_in.readline()

    # X1
    while read_str:
        # S1

        print(state_string.format('S1', 'X1', 'Y2'))
        file_log.write(state_string.format('S1', 'X1', 'Y2'))

        # Y2
        tab_str = "\t" * num_of_for
        # X2
        ####################
        # condition_str and output_str are for any conditions.
        # Program can go to the S3 bt 3 ways.
        # The 3 ways contain own condotion and output
        ####################
        condition_str = ""
        output_str = ""
        if "for (" in read_str or "for(" in read_str:
            # Y3
            # get from the line a counter, a condition,an increament of the cycle
            counter, condition, increment = read_cycle_start(read_str)
            read_str = tab_str + counter + ";\n" + tab_str + "while({})".format(condition) + "{\n"
            num_of_for += 1

            condition_str = "X2"
            output_str = "Y3"

        else:
            # X3

            # Program can get in the if and pass the if
            condition_str = "!X3"
            output_str = "-"

            if "}" in read_str:
                # Y5
                num_of_for -= 1
                read_str = tab_str + increment + ";" + "\n" + "\t" * num_of_for + "}\n"

                condition_str = "!X2X3"
                output_str = "Y5"

        # Y4,S3

        print(state_string.format('S3', condition_str, output_str))
        file_log.write(state_string.format('S3', condition_str, output_str))


        file_out.writelines(read_str)
        read_str = file_in.readline()


# get from string a counter, a condition, a increment by extraction from string
def read_cycle_start(start_cycle_str):
    cycle_counter = start_cycle_str[start_cycle_str.find("(") + 1: start_cycle_str.find(";")].strip()
    cycle_condition = start_cycle_str[start_cycle_str.find(";") + 1:start_cycle_str.rfind(";")].strip()
    cycle_increment = start_cycle_str[start_cycle_str.rfind(";") + 1:start_cycle_str.rfind(")")].strip()
    return cycle_counter, cycle_condition, cycle_increment


if __name__ == '__main__':
    main()
