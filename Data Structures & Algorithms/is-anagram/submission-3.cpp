class Solution {
public:
    bool isAnagram(string s, string t) {
        /*
        add to map, then go through second string and decrement counts. if -1 then return false
        if key not in map, return false
        walk through map again, if any is not 0 then return false
        */
        unordered_map<char,int> mpp;

        if(t.size() != s.size()) {
            return false;
        }

        for(int i = 0; i < s.size(); i++) {
            mpp[s[i]] += 1;
        }

        for(int j = 0; j < t.size(); j++) {
            if(!mpp.contains(t[j])) {
                return false;
            }
            mpp[t[j]] -= 1;
            if(mpp[t[j]] < 0) {
                return false;
            }
        }

        for (const auto& [key, value] : mpp) {
            if(value != 0) {
                return false;
            }
        }
        return true;

    }
};
