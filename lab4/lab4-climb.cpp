class Solution {
public:
//shatnii toog integer helbereer avna. Shataar garah bolomjit arguudiin toog butsaana. dnmc
    int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;

        int first = 1;
        int second = 2;
        int result;
//3dah shatnaas ehlen n hurtel toirno 1 2r shat hurtel todorhoi
        for (int i = 3; i <= n; i++) {
            result = first + second; //odoogin shatand hureh arguudin too ni umnuh 2 argiin niilber bna
            first = second;
            second = result;
        }

        return result;
    }
};
