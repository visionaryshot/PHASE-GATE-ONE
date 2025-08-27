import java.util.Scanner;

public class Mbitt {
    public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
String[] questions = {
	        "1.You regularly make new friends.",
		"2.Complex and novel ideas excite you more than simple and straightforward ones.",
		"3.You usually feel more persuaded by what resonates emotionally with you than by factual arguments.",
		"4.Your living and working spaces are clean and organized.",
		"5.You usually stay calm, even under a lot of pressure.",
		"6.You find the idea of networking or promoting yourself to strangers very daunting.",
		"7.You prioritize and plan tasks effectively, often completing them well before the deadline.",
		"8.People’s stories and emotions speak louder to you than numbers or data.",
		"9.You like to use organizing tools like schedules and lists.",
		"10.Even a small mistake can cause you to doubt your overall abilities and knowledge.",
		"11.You feel comfortable just walking up to someone you find interesting and striking up a conversation.",
		"12.You are not too interested in discussions about various interpretations of creative works",
		"13.You prioritize facts over people’s feelings when determining a course of action.",
		"14.You often allow the day to unfold without any schedule at all.",
		"15.You rarely worry about whether you make a good impression on people you meet.",
		"16.You enjoy participating in team-based activities.",
		"17.You enjoy experimenting with new and untested approaches.",
		"18.You prioritize being sensitive over being completely honest.",
		"19.You actively seek out new experiences and knowledge areas to explore.",
		"20.You prefer to do your chores before allowing yourself to relax.",
	};
		

public static String[]  personality = {
            
            "A. Expend energy, enjoy groups     B. Conserve energy, enjoy one-on-one",
            "A. Interpret literally     B. Look for meaning and possibilities",
            "A. Logical, thinking, questioning     B. Empathetic, feeling, accommodating",
            "A. Organized, orderly     B. Flexible, adaptable",
            "A. More outgoing, think out loud     B. More reserved, think to yourself",
            "A. Practical, realistic, experiential     B. Imaginative, innovative, theoretical",
            "A. Candid, straight forward, frank     B. Tactful, kind, encouraging",
            "A. Plan, schedule     B. Unplanned, spontaneous",
            "A. Seek many tasks, public activities, interaction     B. Seek private, solitary activities with quiet",
            "A. Standard, usual, conventional     B. Different, novel, unique",
            "A. Firm, tend to criticize, hold the line     B. Gentle, tend to appreciate, conciliate",
            "A. Regulated, structured     B. Easygoing, 'live' and 'let live'",
            "A. External, communicative, express yourself     B. Internal, reticent, keep to yourself",
            "A. Focus on here-and-now     B. Look to the future, global perspective, big picture",
            "A. Tough-minded, just     B. Tender-hearted, merciful",
            "A. Preparation, plan ahead     B. Go with the flow, adapt as you go",
            "A. Active, initiate     B. Reflective, deliberate",
            "A. Facts, things, 'what is'     B. Ideas, dreams, 'what could be', philosophical",
            "A. Matter of fact, issue-oriented     B. Sensitive, people-oriented, compassionate",
            "A. Control, govern     B. Latitude, freedom"
   
        };


        System.out.println("MBTI TEST");
        for (int counter = 0; counter < questions.length; counter++) {
	while(true){
            System.out.println((counter + 1) + "-> " + questions[counter]);
            String answer = scanner.nextLine().trim().toUpperCase();

		if(answer.equals("A")|| answer.equals("B")){
		break;

}
               else {
	System.out.println("Expected A  or B as Response\nI know this is an error, pls try again.");
        }
	}
}
  
       
    }
}
