class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int num;
        for (int i=0; i<included.length; i++) {
            num = a + (d*i);
            if (included[i]) {
                answer+=num;
            }
        }
        return answer;
    }
}