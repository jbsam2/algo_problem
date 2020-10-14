import java.util.*;
import java.util.concurrent.*;

class Solution {
    public long solution(String s) {
        ArrayList<Integer>[] charIndex = new ArrayList[26];
        for (int i = 0; i < 26; i++) {
            charIndex[i] = new ArrayList<Integer>();
        }
        ArrayList<Integer>[] charBlkSize = new ArrayList[26];
        for (int i = 0; i < 26; i++) {
            charBlkSize[i] = new ArrayList<Integer>();
        }
        HashMap<Integer, Integer>[] sumBlkSize = new HashMap[26]; // 블록: 같은 알파벳이 연속으로 존재하는 구간 // 각 알파벳의 블록 크기 통계를 저장하는 Map
        for (int i = 0; i < 26; i++) {
            sumBlkSize[i] = new HashMap<Integer, Integer>();
        }

        ArrayList<Integer> charIndexAll = new ArrayList<>();// 모든 알파벳 블록의 시작 위치를 저장하는 배열
        final int S_LENGTH = s.length();
        long answer = 0;

        // 문자 길이가 2 미만
        if (S_LENGTH < 2) {
            return 0L;
        }

        {
            boolean bOnlyOneChar = true;// 단일 문자만 존재하는지 확인하기 위한 변수
            int blkSize = 1;// 블록 크기 계산을 위한 변수
            char chBefore = s.charAt(0);// 이전 블록의 알파벳을 저장
            // 가장 첫 문자의 블록 시작 위치(0)을 저장
            charIndexAll.add(0);
            charIndex[chBefore - 'a'].add(0);

            for (int i = 1; i < S_LENGTH; i++) {
                // 다른 문자가 나타나면 해당 사항을 저장
                char chCurrent = s.charAt(i);
                if (chCurrent != chBefore) {// 다른 문자의 위치를 배열에 추가
                    charIndexAll.add(i);
                    charIndex[chCurrent - 'a'].add(i);
                    charBlkSize[chBefore - 'a'].add(blkSize);// 이전 문자의 블럭 크기 값을 통계에 추가
                    if (sumBlkSize[chBefore - 'a'].containsKey(blkSize)) {
                        sumBlkSize[chBefore - 'a'].replace(blkSize, sumBlkSize[chBefore - 'a'].get(blkSize) + 1);
                    } else {
                        sumBlkSize[chBefore - 'a'].put(blkSize, 1);
                    }// 다음 블록 크기 계산을 위한 초기화
                    blkSize = 0;// 다음 블록을 찾기 위해 이전 문자 값을 현재 문자 값으로 갱신
                    chBefore = chCurrent;// 다른 문자를 한번이라도 발견한 경우
                    bOnlyOneChar = false;// 단일 문자만 존재하는지 확인하기 위한 변수를 거짓으로 변경
                }
                blkSize++;// 현재 블럭의 크기를 1 증가
            }
            charBlkSize[chBefore - 'a'].add(blkSize);// 마지막 블럭을 통계에 반영
            if (sumBlkSize[chBefore - 'a'].containsKey(blkSize)) {
                sumBlkSize[chBefore - 'a'].replace(blkSize, sumBlkSize[chBefore - 'a'].get(blkSize) + 1);
            } else {
                sumBlkSize[chBefore - 'a'].put(blkSize, 1);
            }

            // 모든 문자가 동일한 경우 바로 0 반환
            if (bOnlyOneChar) {
                return 0L;
            }

            // 끝을 표시하는 값을 추가로 저장
            charIndexAll.add(S_LENGTH);
            for (int i = 0; i < 26; i++) {
                charIndex[i].add(S_LENGTH);
            }
        }

        for (int i = 0; i < charIndexAll.size() - 1; i++) {// 위에서 정리한 위치 값 및 통계를 이용하여 실제 값 계산
            int currentIndex = charIndexAll.get(i);
            int endIndex = charIndexAll.get(i + 1);
            int currentBlkSize = endIndex - currentIndex;
            char chCurrentBlk = s.charAt(currentIndex);

            {
                int sumOfcurrentBlkSize = sumBlkSize[chCurrentBlk - 'a'].get(currentBlkSize) - 1;
                if (sumOfcurrentBlkSize == 0) {
                    sumBlkSize[chCurrentBlk - 'a'].remove(currentBlkSize);
                } else {
                    sumBlkSize[chCurrentBlk - 'a'].replace(currentBlkSize, sumOfcurrentBlkSize);
                }
            }

            for (int j = currentIndex; j < endIndex; j++) {
                int frontBlkSize = endIndex - j;
                answer += (long)(S_LENGTH - j) * (S_LENGTH - j - 1) / 2;
                answer -= (long)frontBlkSize * (frontBlkSize - 1) / 2;

                Set<Integer> sumOfBlkSize = sumBlkSize[chCurrentBlk - 'a'].keySet();
                for (Integer blkSize : sumOfBlkSize) {
                    if (blkSize <= frontBlkSize) {
                        answer -= blkSize * (blkSize + 1) / 2 * sumBlkSize[chCurrentBlk - 'a'].get(blkSize);
                    } else {
                        answer -= (frontBlkSize * (frontBlkSize + 1) / 2 + frontBlkSize * (blkSize - frontBlkSize)) * sumBlkSize[chCurrentBlk - 'a'].get(blkSize);
                    }
                }
            } // for j
        } // for i

        return answer;
    }
}