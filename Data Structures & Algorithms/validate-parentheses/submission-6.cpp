#include <stack>

class Solution {
public:
    bool isValid(string s) {

        stack<char> stored;
        char check;
        for(char c : s) {
            if(c == '(' || c == '{' || c == '[') {
                stored.push(c); 
            } else {
                if (stored.empty()) {
                    return false;
                }
                check = stored.top();
                stored.pop();
                if(c == ')' && check != '(' || c == '}' && check != '{' || c == ']' && check != '[') {
                    return false;
                }
            }
        }
        return stored.empty();

    }
};
