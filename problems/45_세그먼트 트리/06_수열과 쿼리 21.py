
'''
url: https://www.acmicpc.net/problem/16975
제목: 수열과 쿼리 21
번호: 16975

문제
길이가 N인 수열 A1, A2, ..., AN이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

1 i j k: Ai, Ai+1, ..., Aj에 k를 더한다.
2 x: Ax 를 출력한다.

입력
첫째 줄에 수열의 크기 N (1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 1,000,000)
셋째 줄에는 쿼리의 개수 M (1 ≤ M ≤ 100,000)이 주어진다.
넷째 줄부터 M개의 줄에는 쿼리가 한 줄에 하나씩 주어진다. 1번 쿼리의 경우 1 ≤ i ≤ j ≤ N, -1,000,000 ≤ k ≤ 1,000,000 이고, 2번 쿼리의 경우 1 ≤ x ≤ N이다. 2번 쿼리는 하나 이상 주어진다.

출력
2번 쿼리가 주어질 때마다 출력한다.
'''
