import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public int[] solution(String[] info, String[] query) {
        HashMap< String, ArrayList<Integer>> data = new HashMap<>();
        int[] answer = new int[query.length];
        String[] langs = {"cpp", "java", "python", "-"},
                 deps = {"backend", "frontend", "-"},
                 exps = {"junior", "senior", "-"},
                 foods = {"chicken", "pizza", "-"};
        for(String lang:langs)
            for(String dep:deps)
                for(String exp:exps)
                    for(String food:foods)
                        data.put(lang+dep+exp+food,new ArrayList<Integer>());
        
        for(String i: info)
        {
            String[] tmp = i.split(" ");
            String[] a = {tmp[0],"-"}, b = {tmp[1],"-"}, c = {tmp[2],"-"},d = {tmp[3],"-"};
            for(String e:a)
                for(String f:b)
                    for(String g:c)
                        for(String h:d)
                            data.get(e+f+g+h).add(Integer.parseInt(tmp[4]));
        }
        
        for(ArrayList<Integer> i: data.values())
        {
            i.sort(null);
        }
        int cnt = 0;
        for(String q:query)
        {
            String[] tmp = q.split(" ");
            ArrayList<Integer> pool = data.get(tmp[0]+tmp[2]+tmp[4]+tmp[6]);
            //answer[cnt] = pool.get(0);
            int score = Integer.parseInt(tmp[7]);
            int l = 0;
            int r = pool.size();
            int mid = 0;
            while(l<r)
            {
                mid = (l+r)/2;
                if(pool.get(mid) >= score)
                {
                    r = mid;
                }
                else
                {
                    l = mid + 1;
                }
            }
            answer[cnt] = pool.size() - l;
            cnt++;
        }
        
        return answer;
    }
}