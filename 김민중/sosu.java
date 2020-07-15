import java.util.Scanner;
import java.io.IOException;
class Main {
  public static void main(String[] args) throws IOException{
    Scanner scanner = new Scanner(System.in);

    int num = scanner.nextInt();
    int sosuCnt = 0;
    int cnt = 0;

    for(int i = 1; i<=num; i++) {
      int sNum = scanner.nextInt();
      sosuCnt = 0;

      for(int j = 1; j<=sNum; j++) {
        if(sNum % j == 0) {
          sosuCnt++;
        }
      }
      if(sosuCnt == 2) {
        cnt++;
      }
    }
    System.out.println(cnt);
}
}