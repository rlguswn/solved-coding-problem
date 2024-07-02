class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        Boolean answer;
        if (ineq.equals("<")) {
            answer = n < m;
        }
        else {
            answer = n > m;
        };
        
        if (eq.equals("=")) {
            answer = answer || (n == m);
        };
        
        return (answer) ? 1:0;
    }
}