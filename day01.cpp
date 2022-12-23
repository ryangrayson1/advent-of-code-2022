#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int part1() {
    int cal = 0, res = 0;
    string line;
    while (getline(cin, line)) {
        if (line == "") {
            res = max(res, cal);
            cal = 0;
        } else {
            cal += stoi(line);
        }
    }
    return max(res, cal);
}

int part2() {
    int cal = 0;
    vector<int> elves;
    string line;
    while (getline(cin, line)) {
        if (line == "") {
            elves.push_back(cal);
            cal = 0;
        } else {
            cal += stoi(line);
        }
    }
    elves.push_back(cal);
    sort(elves.begin(), elves.end());
    return elves[elves.size() - 3] + elves[elves.size() - 2] + elves[elves.size() - 1];
}

int main() {
    // cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
    return 0;
}
