import java.io.File;
import java.io.FileNotFoundException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Main {
    public static int bitWidthOfOperand = 4;
    public static int bitWidthOfCommand = 2;
    public static int standardLengthOfCommand = bitWidthOfCommand + bitWidthOfOperand * 2;
    public static String multiplication = "00";
    public static String division = "11";


    public static void main(String[] args) {
        System.out.printf("|State | X %-8s| Y %-6s|", " "," ");
        System.out.println("\n______________________________");
        printMealy("S0","","");

        String path = "C:\\Temp\\example.txt";
        String command = fetchCommandLine(path);

        printMealy("S1","1","Y1");

        if (command == null) {
            System.out.println("000 error: file is not found. Check your file.");
            printMealy("S0","X1","Y2");
            return;
        }

        if(command.length() != standardLengthOfCommand){
            if(isLongerCommand(command)){
                System.out.println("001 error: command line is too long. Recheck it.");
                printMealy("S0","","!X1X2X3");
            }else {
                System.out.println("002 error: command line is too short. Recheck it.");
                printMealy("S0","","!X1!X2X3");
            }
            return;
        }

        // array of registers, value = 3: code operation, 1st and 2nd operands
        String[] partsOfCommand = fetchPartsOfCommand(command);
        printMealy("S2","!X1!X2","Y5");
        if (!checkCommandOfOperation(partsOfCommand[0])) {
            System.out.println("003 error: operation command code is wrong. Please check it.");
            printMealy("S0", "X4","Y6");
            return;
        }

        outputRegisters(partsOfCommand);



        int num1 = convert2DecimalNotation(partsOfCommand[1]);
        int num2 = convert2DecimalNotation(partsOfCommand[2]);

        printMealy("S3", "!X4","Y7");
        if (partsOfCommand[0].equals(multiplication)) {
            num1 = num1 * num2;
            printMealy("S4", "X5", "Y8");
        } else {
            if (secondOperandIsZero(num2)) {
                System.out.println("004 error: operation is prohibited. Second operand is zero.");
                printMealy("S0", "!X5X6", "Y10");
                return;
            }
            num1 = num1 / num2;
            printMealy("S4", "!X5!X6", "Y9");

        }
        String resOfOperation = convert2BinaryNotation(num1);
        printMealy("S5","1","Y11");
        if (isCorrectAnswer(resOfOperation)) {
            partsOfCommand[1] = resOfOperation;
            printMealy("S6", "X7", "Y12");
        } else {
            System.out.println("005 error: cannot execute multiplication. The first register is overflowed. Please correct your data.");
            printMealy("S0", "!X7", "Y13");
            return;
        }
        outputRegisters(partsOfCommand);
        System.out.println("The program have finished successfully.");

        printMealy("S0", "1", "Y14");
    }

    public static void printMealy(String state,  String X, String Y){
        System.out.printf("|%-6s| X:%-8s| Y:%-6s|", state, X, Y);
        System.out.println();
    }

    public static boolean isCorrectAnswer(String result) {
        return result.length() <= bitWidthOfOperand;
    }


    public static int convert2DecimalNotation(String binaryNumber) {
        return Integer.parseInt(binaryNumber, 2);
    }

    public static String convert2BinaryNotation(int decimalNumber) {
        StringBuilder binaryNum = new StringBuilder(Integer.toBinaryString(decimalNumber));
        while (binaryNum.length() < bitWidthOfOperand) {
            binaryNum.insert(0, "0");
        }
        return binaryNum.toString();
    }

    public static boolean secondOperandIsZero(int secondOperand) {
        return secondOperand == 0;
    }

    public static boolean checkCommandOfOperation(String command) {
        return command.equals(multiplication) || command.equals(division);
    }

    public static void outputRegisters(String[] partsOfCommand) {
        System.out.print("Registers is ");
        for (String part : partsOfCommand) {
            System.out.print(part + " ");
        }
        System.out.println();
    }

    public static String fetchCommandLine(String path) {
        File file = new File(path);
        Scanner scanner;
        String string;
        try {
            scanner = new Scanner(file);
            string = scanner.nextLine();
        } catch (FileNotFoundException | NoSuchElementException e) {
            return null;
        }
        return string;
    }

    public static String[] fetchPartsOfCommand(String command) {
        String[] partsOfCommand = new String[3];
        partsOfCommand[0] = command.substring(0, bitWidthOfCommand);
        partsOfCommand[1] = command.substring(bitWidthOfCommand,
                bitWidthOfCommand + bitWidthOfOperand);
        partsOfCommand[2] = command.substring(bitWidthOfCommand + bitWidthOfOperand,
                standardLengthOfCommand);

        return partsOfCommand;
    }
    public static boolean isLongerCommand(String command){
        return command.length() > standardLengthOfCommand;
    }
}
