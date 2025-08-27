import java.util.Scanner;
public class CardValidator {

public static void main(String[] args) {
Scanner input = new Scanner(System.in);
     
System.out.print("Enter your credit card number:");
String number = input.nextLine().trim();

while(true){
if (number.equals("0-9")) {
break;
}
else {

System.out.println("Wrong input. Enter digits only.\nSo please try again");
}
}
break;

int length = number.length();
while(true){

if(length == 13 || length == 16) {
break;
} else{
System.out.println("Invalid card length. Must be between 13 and 16 digits.



public static String getType(String number) {
    if (number == null ) {
        return "invalid";
    }

    if (number.startsWith("4")) {
        return "Visa";
    } else if (number.startsWith("5")) {
        return "MasterCard";
    } else if (number.startsWith("37")) {
        return "American Express";
    } else if (number.startsWith("6")) {
        return "Discover";
    } else {
        return "invalid";
    }
}
