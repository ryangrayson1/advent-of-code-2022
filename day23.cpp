#include <iostream>
#include <unordered_map>
using namespace std;

const int N = 250;
const int B = 90;

void p(char grid[N][N]) {
    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            if (grid[r][c]) {
                cout << "# ";
            } else {
                cout << ". ";
            }
        }
        cout << '\n';
    }
    cout << "\n\n";
}

struct C {
    int r, c;
    C(int rr, int cc) : r(rr), c(cc) {}
};

int hsh(int r, int c) {
    return r * N + c;
}

C unhash(int h) {
    return C(h / N, h % N);
}

int part12(char grid[N][N], int rounds, bool part2) {
    C moves[4][3] = {
        {C(-1, -1), C(-1, 1), C(-1, 0)},
        {C(1, -1), C(1, 1), C(1, 0), },
        {C(-1, -1), C(1, -1), C(0, -1)},
        {C(-1, 1), C(1, 1), C(0, 1),},
    };
    char grid2[N][N] = {};
    unordered_map<int, C*> propose;
    int round, row, col, r, c, i, j, h, nxt_row, nxt_col;
    bool alone, prop, move;
    for (round = 0; round < rounds; ++round) {
        for (row = 0; row < N; ++row) {
            for (col = 0; col < N; ++col) {
                if (!grid[row][col]) {
                    continue;
                }
                alone = true;
                for (r = -1; r < 2; ++r) {
                    for (c = -1; c < 2; ++c) {
                        if ((r != 0 || c != 0) && grid[row+r][col+c]) {
                            alone = false;
                        }
                    }
                }
                if (alone) {
                    grid2[row][col] = 1;
                    continue;
                }
                prop = false;
                for (c = 0; c < 4; ++c) {
                    i = (round + c) % 4;
                    for (j = 0; j < 3; ++j) {
                        nxt_row = row + moves[i][j].r;
                        nxt_col = col + moves[i][j].c;
                        if (row == 13 && col == 8) {
                            cout << nxt_row << " " << nxt_col << endl;
                        }
                        if (grid[nxt_row][nxt_col]) {
                            break;
                        }
                        if (j == 2) {
                            h = hsh(nxt_row, nxt_col);
                            if (propose.count(h)) {
                                grid2[row][col] = 1;
                                if (propose[h]->r != -1) {
                                    grid2[propose[h]->r][propose[h]->c] = 1;
                                    propose[h]->r = -1;
                                }                                
                            } else {
                                propose[h] = new C(row, col);
                            }
                            prop = true;
                            break;
                        }
                    }
                    if (prop) {
                        break;
                    }
                }
                if (!prop) {
                    grid2[row][col] = 1;
                }
            }
        }

        for (pair<int, C*> ft : propose) {
            if (ft.second->r != -1) {
                C dest = unhash(ft.first);
                grid2[dest.r][dest.c] = 1;
            }
            delete ft.second;
        }
        propose.clear();

        bool same = true;
        for (row = 0; row < N; ++row) {
            for (col = 0; col < N; ++col) {
                if (grid[row][col] != grid2[row][col]) {
                    same = false;
                }
                grid[row][col] = grid2[row][col];
                grid2[row][col] = 0;
            }
        }
        if (part2 && same) {
            // p(grid);
            return round + 1;
        }
    }

    if (part2) {
        return -1;
    }

    int top = N-1, bottom = 0, left = N-1, right = 0;
    for (row = 0; row < N; ++row) {
        for (col = 0; col < N; ++col) {
            if (grid[row][col]) {
                top = min(top, row);
                bottom = max(bottom, row);
                left = min(left, col);
                right = max(right, col);
            }
        }
    }

    int free = 0;
    for (row = top; row <= bottom; ++row) {
        for (col = left; col <= right; ++col) {
            if (!grid[row][col]) {
                ++free;
            }
        }
        cout << endl;
    }
    // p(grid);
    return free;
}

int main() {
    char grid[N][N] = {};
    int r, c; string s;
    for (r = 0; r < N-B-B; ++r) {
        cin >> s;
        for (c = 0; c < N-B-B; ++c) {
            if (s[c] == '#') {
                grid[r+B][c+B] = 1;
            }
        }
    }

    // part 1: set N = 92, B = 11;
    // cout << part12(grid, 10, false) << '\n';
    // part 2: set N = 250, B = 90
    cout << part12(grid, 1000, true) << '\n';

    return 0;
}