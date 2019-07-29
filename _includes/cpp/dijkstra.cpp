#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

const int INF = (1 << 30) - 1;
const int MAX_V = 100001;

struct edge {
  int to, cost;
};
typedef pair<int, int> P; // firstは最短距離, secondは頂点の番号

int V, E;
vector<edge> G[MAX_V];
int d[MAX_V];

// 負辺のない単一始点全点間最短路を求めるアルゴリズム。
void dijkstra(int s) {
  priority_queue<P, vector<P>, greater<P>> que;
  fill(d, d + V, INF);
  d[s] = 0;
  que.push(P(0, s));

  while (!que.empty()) {
    P p = que.top();
    que.pop();
    int v = p.second;
    if (d[v] < p.first) {
      continue;
    }

    for (int i = 0; i < G[v].size(); i++) {
      edge e = G[v][i];
      if (d[e.to] > d[v] + e.cost) {
        d[e.to] = d[v] + e.cost;
        que.push(P(d[e.to], e.to));
      }
    }
  }
}