class Solution {
    public String solution(String code) {
        Boolean mode = false;
        String ret = "";
        
        for (int i=0; i<code.length(); i++) {
            if (code.charAt(i) == '1') {
                mode = !(mode);
            }
            else {
                if (mode && (i%2==1)) {
                    ret += code.charAt(i);
                }
                else if ((!mode) && (i%2==0)) {
                    ret += code.charAt(i);
                }
            }
        }
        if (ret.equals("")) {
            ret = "EMPTY";
        }
        return ret;
    }
}