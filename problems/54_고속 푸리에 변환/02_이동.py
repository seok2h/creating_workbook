
'''
url: https://www.acmicpc.net/problem/1067
제목: 이동
번호: 1067

문제
N개의 수가 있는 X와 Y가 있다. 이때 X나 Y를 순환 이동시킬 수 있다. 순환 이동이란 마지막 원소를 제거하고 그 수를 맨 앞으로 다시 삽입하는 것을 말한다. 예를 들어, {1, 2, 3}을 순환 이동시키면 {3, 1, 2}가 될 것이고, {3, 1, 2}는 {2, 3, 1}이 된다. 순환 이동은 0번 또는 그 이상 할 수 있다. 이 모든 순환 이동을 한 후에 점수를 구하면 된다. 점수 S는 다음과 같이 구한다.
S = X[0]×Y[0] + X[1]×Y[1] + ... + X[N-1]×Y[N-1]
이때 S를 최대로 하면 된다.

입력
첫째 줄에 N이 주어진다. 둘째 줄에는 X에 들어있는 N개의 수가 주어진다. 셋째 줄에는 Y에 있는 수가 모두 주어진다. N은 60,000보다 작거나 같은 자연수이고, X와 Y에 들어있는 모든 수는 100보다 작은 자연수 또는 0이다.

출력
첫째 줄에 S의 최댓값을 출력한다.
'''
