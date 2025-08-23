//DO
//Ask user for last period date, cycle length, and period duration
//Calculate:
//- Next period date
//- Ovulation date
//- Fertile window (ovulation ± 2 days)
//- Safe periods (after period and before next period)

//Display all results
//Ask if user wants to repeat
//WHILE user says 'Y'
//Display closing message

import java.util.Scanner;
public class AdvanceContracepticPlan {
 public static void main(String[] args) {
  Scanner input = new Scanner(System.in);
int day;
int month;
int year;
int cycleLength;
int periodDuration;
char repeat;

do {
System.out.println("Menstrual Cycle plan ");
System.out.print("Enter last period day (1-31): ");
day = input.nextInt();

 System.out.print("Enter last period month (1-12): ");
 month = input.nextInt();
 System.out.print("Enter last period year : ");
 year = input.nextInt();
 System.out.print("Enter cycle length in days: ");
 
 cycleLength = input.nextInt();
 System.out.print("Enter period duration in days: ");
 periodDuration = input.nextInt();
 int nextDay = day + cycleLength;
 int nextMonth = month;
 int nextYear = year;

while (nextDay > 30) {
nextDay -= 30;
nextMonth++;
if (nextMonth > 12) {
nextMonth = 1;
nextYear++;}
}

int ovulationDay = day + (cycleLength / 2);
int ovulationMonth = month;
int ovulationYear = year;
while (ovulationDay > 30) {
ovulationDay -= 30;
ovulationMonth++;
if (ovulationMonth > 12) {
ovulationMonth = 1;
ovulationYear++;
}
}

int fertileStart = ovulationDay - 2;
int fertileEnd = ovulationDay + 2;

System.out.println("Next Period: " + nextDay + "/" + nextMonth + "/" + nextYear);
System.out.println("Ovulation Date: " + ovulationDay + "/" + ovulationMonth + "/" + ovulationYear);
System.out.println("Fertile Window: " + fertileStart + " to " + fertileEnd );
System.out.println("Safe Periods:");
System.out.println("  After Period: Day " + (day + periodDuration) + " to " + (fertileStart - 1));
System.out.println("  Before Next Period: Day " + (fertileEnd + 1) + " to " + (nextDay - 1));
System.out.print("\nDo you want to calculate again? (Y/N): ");
repeat = input.next().charAt(0);
} while (repeat == 'Y' || repeat == 'y');

System.out.println("Your consultation has ended. Stay sharp,\nMay we not be victim of parent of unwanted pregnancy\nDr. Adedeji Fareed Cares!");
}
}