
'''
url: https://www.acmicpc.net/problem/10067
제목: 수열 나누기
번호: 10067

문제
은기는 음이 아닌 정수 n개로 이루어진 수열을 이용해 시간을 때우고 있다. 은기는 수열을 총 k+1개로 나누어야 하고, 각 부분은 비어있지 않아야 한다. 수열을 k+1개로 나누러면, 아래와 같은 과정을 k번 반복해야 한다.

원소를 두 개 이상 가지고 있는 부분을 고른다. (가장 처음에는 수열 전체밖에 없다)
임의의 두 원소 사이를 기준으로 수열을 두 부분으로 나눈다.

위의 과정을 할 때마다 얻게되는 점수는 새로 나누어진 각 부분에 들어있는 원소의 합을 곱한 것이다. 위의 과정을 k번 반복하면서 은기가 얻을 수 있는 점수의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 정수 n과 k가 주어진다. (2 ≤ n ≤ 100,000, 1 ≤ k ≤ min(n-1, 200)) 둘째 줄에는 수열을 나타내는 음이 아닌 정수 n개 a1, a2, ..., an이 주어진다. (0 ≤ ai ≤ 104)

출력
첫째 줄에 얻을 수 있는 가장 큰 점수를 출력한다. 둘째 줄에는 그러한 점수를 얻기 위해 몇 번째 원소 다음에 수열을 나누어야 하는지 순서대로 출력한다. 가능한 답이 여러개라면, 아무거나 출력한다.
'''
