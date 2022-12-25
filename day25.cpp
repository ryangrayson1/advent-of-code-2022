#include <iostream>
#include <vector>
using namespace std;

#define ll long long

ll snafu_to_decimal(string snafu) {
    ll pow = 1, num = 0, i;
    for (i = snafu.length() - 1; i >= 0; --i) {
        if (snafu[i] == '-') {
            num -= pow;
        } else if (snafu[i] == '=') {
            num -= 2L * pow;
        } else {
            num += (ll)(snafu[i]-48) * pow;
        }
        pow *= 5L;
    }
    return num;
}

string decimal_to_snafu(ll num) {
    string base5 = "";
    while (num > 0) {
        base5 += to_string(num % 5);
        num /= 5;
    }
    cout << "regular base 5: ";
    for (int i = base5.length() - 1; i >= 0; --i) {
        cout << base5[i];
    }
    cout << '\n';
    return "";
}

string part1(vector<string>& snafus) {
    ll sum = 0;
    for (string snafu : snafus) {
        sum += snafu_to_decimal(snafu);
    }
    cout << "   decumal sum: " << sum << '\n';
    decimal_to_snafu(sum);
    /*
    1 4 0 4 2 3 1 1 4 1 2 1 3 3 0 4 0 4 2 2
    2 - 1 0 = = 1 2 - 1 2 2 - = 1 - 1 - 2 2  
    1 -     1 =   1 -       1 = 
        1 =             1 =
        1 0             
    */
    return "         snafu: 2-10==12-122-=1-1-22\n";
}

int main() {
    vector<string> snafus;
    string s;
    while (cin >> s) {
        snafus.push_back(s);
    }
    cout << part1(snafus) << '\n';
}
