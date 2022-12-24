#include <iostream>
#include <unordered_set>
#include <queue>
using namespace std;

const int R = 25;
const int C = 120;
const int G = 600;
char grids[G][R][C] = {};

void setup() {
    char grid[R][C];
    int row, col;
    string line; cin >> line;
    for (row = 0; row < R; ++row) {
        cin >> line;
        for (col = 0; col < C; ++col) {
            grid[row][col] = line[col+1];
        }
    }
    int i, r, c, row2, col2;
    for (i = 0; i < G; ++i) {
        for (row = 0; row < R; ++row) {
            for (col = 0; col < C; ++col) {
                r = c = 0;
                if (grid[row][col] == '^') {
                    r = -1;
                } else if (grid[row][col] == 'v') {
                    r = 1;
                } else if (grid[row][col] == '<') {
                    c = -1;
                } else if (grid[row][col] == '>') {
                    c = 1;
                } else {
                    continue;
                }
                row2 = (((row + i * r) % R) + R) % R;
                col2 = (((col + i * c) % C) + C) % C;
                grids[i][row2][col2] = 1;
            }
        }
    }
}

struct State {
    int row, col, gid, time; string hash;
    State(int r, int c, int g, int t) : row(r), col(c), gid(g), time(t) {
        hash = to_string(r) + ',' + to_string(c) + ',' + to_string(g);
    }
};

int bfs(State *start, State *end) {
    int inc[10] = {0, 0, -1, 0, 1, 0, 0, -1, 0, 1};
    unordered_set<string> seen;
    queue<State*> q;
    q.push(new State(start->row, start->col, start->gid, 0));
    State *cur, *nxt; int i;
    while (!q.empty()) {
        cur = q.front(); q.pop();
        for (i = 0; i < 10; i += 2) {
            nxt = new State(cur->row + inc[i], cur->col + inc[i+1], (cur->gid + 1) % G, cur->time + 1);
            if (nxt->row == end->row && nxt->col == end->col) {
                end->gid = nxt->gid;
                return nxt->time;
            }
            if (0 <= nxt->row && nxt->row < R && 0 <= nxt->col && nxt->col < C && !grids[nxt->gid][nxt->row][nxt->col] && !seen.count(nxt->hash)) {
                seen.insert(nxt->hash);
                q.push(nxt);
            } else if (cur->row == start->row && cur->col == start->col && nxt->row == start->row && nxt->col == start->col && cur->time < 10) { // to allow waiting at start
                q.push(nxt);
            } else {
                delete nxt;
            }
        }
        delete cur;
    }
    return -1;
}

int part1() {
    State *s1, *s2;
    s1 = new State(-1, 0, 0, 0);
    s2 = new State(R, C-1, 0, 0);
    return bfs(s1, s2);
}

int part2() {
    State *s1, *s2, *s3, *s4;
    s1 = new State(-1, 0, 0, 0);
    s2 = new State(R, C-1, 0, 0);
    s3 = new State(-1, 0, 0, 0);
    s4 = new State(R, C-1, 0, 0);
    return bfs(s1, s2) + bfs(s2, s3) + bfs(s3, s4);
}

int main () {
    setup();
    cout << part1() << "\n";
    cout << part2() << "\n";
    return 0;
}
