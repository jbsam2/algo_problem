import java.util.*;
class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        int playTime = conv(play_time);
        int advTime = conv(adv_time);
        long playNums[] = new long[playTime+10];

        for(String log : logs){
            String tmp[] = log.split("-");
            playNums[conv(tmp[0])]++;
            playNums[conv(tmp[1])]--;
        }
        for(int i = 0; i < playNums.length-1; i++)
            playNums[i+1] += playNums[i];

        int startTime = 0;
        long timeSum = 0;
        long max = timeSum;
        long maxStartTime = 0;
        while(startTime+advTime <= playTime){
            if(max < timeSum){
                max = timeSum;
                maxStartTime = startTime;
            }
            timeSum -= playNums[startTime];
            timeSum += playNums[startTime+advTime];
            startTime++;
        }
        return String.format("%02d:%02d:%02d",
                maxStartTime/3600,
                (maxStartTime/60)%60,
                maxStartTime%60);
    }

    int conv(String time){
        String splitted[] = time.split(":");
        return Integer.parseInt(splitted[0])*3600
                + Integer.parseInt(splitted[1])*60
                + Integer.parseInt(splitted[2]);
    }
}