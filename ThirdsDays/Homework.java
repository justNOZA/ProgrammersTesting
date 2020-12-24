import java.util.Scanner;

public class Homework {
  static Scanner scan = new Scanner(System.in);
	public static void main(String[] args) {
    int num = 0, num2 = 0, number;
		String result;
		String str = "";
    num = scan.nextInt();
		scan.nextLine();
		str = scan.nextLine();
		num2 = scan.nextInt();
		scan.nextLine();
		number = Integer.parseInt(str, num);
    result = Integer.toString(number, num2);
		System.out.println("변환 값은 : "+result);
  }
}
