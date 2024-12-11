class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();
        
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0)); //dp[i][j]  ni text1iin ehnii i temdeg text 2iin ehnii j temdgiin lcs urtiig hadgalna

        for (int i = 1; i <= m; ++i) { 
            for (int j = 1; j <= n; ++j) {
                if (text1[i - 1] == text2[j - 1]) { //text 1ini i-1 2iin j-1 adilhn baiwl
                    dp[i][j] = dp[i - 1][j - 1] + 1; //uridchlsn subseq 1eer nemegdene
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]); //uur bvl text1 2 oos neg temdegt hasahad lcsiin urtiinih utgiig hadgalna
                }
            }
        }

        return dp[m][n];
    }
};

//text1 = "abcde"
//text2 = "ace"