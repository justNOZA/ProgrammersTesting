import java.util.Scanner;

public class Homework2 {
	static Scanner scan = new Scanner(System.in);

	public static void main(String[] args) {
		int num = 0, num2 = 0, number;
		String result;
		String str = "";
		while(true){
			try{
				num = scan.nextInt();
				scan.nextLine();
				if(num != 2 && num != 8 && num != 10 && num != 16){
					System.out.println("재입력해주세요");
					continue;
				}
				else{
					str = scan.nextLine();
					num2 = scan.nextInt();
					scan.nextLine();
					if(num2 != 2 && num2 != 8 && num2 != 10 && num2 != 16){
						System.out.println("2재입력해주세요");
						continue;
					}
					number = Integer.parseInt(str, num);
					switch(num2){
						case 2 :
							result = Integer.toBinaryString(number); break;
						case 8 :
							result = Integer.toOctalString(number); break;
						case 16 :
							result = Integer.toHexString(number); break;
						default :
							result = number+"";
					}
					break;
				}
			}
			catch(Exception e){
				System.out.println("다시 입력해 주세요");
				scan.nextLine();
				continue;
			}
		}
		System.out.println("변환 값은 : "+result);
  }
}
