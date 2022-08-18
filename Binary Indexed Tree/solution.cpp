#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

struct BIT {
    int n;
    int *tree;
    BIT(int n) {
        this->n = n;
        tree = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            tree[i] = 0;
        }
    }
    
    void update(int idx, int val) {
        for (int i = idx + 1; i <= n; i += i & -i) {
            tree[i] += val;
        }
    };

    void sum(int idx) {
        int ret = 0;
        for (int i = idx + 1; i > 0; i -= i & -i) {
            ret += tree[i];
        }
    }

    void print() {

    }
};

int main(int argc, char* argv[]) {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
}

