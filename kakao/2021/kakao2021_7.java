import java.util.*;
class Solution {
    static ArrayList<Integer>[] adj = new ArrayList[300005];
    static ArrayList<Integer> s = new ArrayList<Integer>();
    static long INF = 0x7fffffff7fffffffL;
    static long d[][] = new long[300005][2];
    static void dfs(int cur){
        if(adj[cur].isEmpty()){
            d[cur][0] = s.get(cur);
            d[cur][1] = 0;
            return;
        }
        long mingap = INF;
        d[cur][0] = s.get(cur);
        for(Integer x : adj[cur]){
            dfs(x);
            d[cur][0] += Math.min(d[x][0], d[x][1]);
            mingap = Math.min(mingap, d[x][0] - d[x][1]);
        }
        if(mingap < 0) mingap = 0;
        d[cur][1] = d[cur][0] + mingap - s.get(cur);
    }
    public int solution(int[] sales, int[][] links) {
        int n = sales.length;
        for(int i = 1; i <= n; i++) adj[i] = new ArrayList<Integer>();
        s.add(0);
        for(int i = 0; i < n; i++) s.add(sales[i]);
        for(int i = 0; i < n-1; i++)
            adj[links[i][0]].add(links[i][1]);            
        dfs(1);
        return (int)Math.min(d[1][0], d[1][1]);
    }
}






import java.util.*;
class Solution {
    int memos[];
    public int solution(int[] sales, int[][] links) {
        Node nodes[] = new Node[sales.length+1];
        for(int i = 0; i < sales.length; i++)
            nodes[i+1] = new Node(sales[i], i+1);

        for(int[] link : links)
            nodes[link[0]].add(nodes[link[1]]);

        memos = new int[sales.length+1];
        Arrays.fill(memos, -1);

        return recursion(nodes[1]);
    }

    int recursion(Node node){
        if(node == null) return 0;
        if(memos[node.num] != -1)
            return memos[node.num];
        if(node.childs.size() == 0) return 0;

        int min = Integer.MAX_VALUE>>1;

        int sum = 0;
        for(int i = 0; i < node.childs.size(); i++){
            sum = 0;
            for(int j = 0; j < node.childs.size(); j++){
                if(i == j) continue;
                sum += recursion(node.childs.get(j));
            }
            for(Node child : node.childs.get(i).childs) {
                sum += recursion(child);
            }
            min = Math.min(min, sum+node.childs.get(i).sales);
        }
        sum = 0;
        for(Node child : node.childs)
            sum += recursion(child);
        min = Math.min(min, sum+node.sales);
        memos[node.num] = min;
        return min;
    }

    class Node{
        int sales;
        int num;
        List<Node> childs = new ArrayList<>();
        Node(int sales, int num){
            this.sales = sales;
            this.num = num;
        }
        void add(Node node){
            childs.add(node);
        }
    }
}