import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        
        int i = 0;
        String s = "";
        while (i < n) {
            s += str;
            i++;
        };
        System.out.println(s);
    }
}