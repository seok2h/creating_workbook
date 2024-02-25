
'''
url: https://www.acmicpc.net/problem/11495
제목: 격자 0 만들기
번호: 11495

문제
음수가 아닌 정수들의 격자가 주어진다. 당신은 이 격자에 다음 연산을 행할 수 있다.

1. 격자에서 가로 또는 세로로 인접한 정수 2개를 고른다.
2. 각 정수가 양수일 때 1 감소시킨다.

다음 그림은 총 4개의 연속한 연산을 2*2 격자에 가해서 모든 정수를 0으로 만든 과정을 보여준다.

위 예제에서는 모든 정수를 0으로 만들기 위해 4번의 연산을 행했다. 이보다 적은 횟수의 연산으로는 모든 정수를 0으로 만들 수 없다는 것을 쉽게 알 수 있다.
격자가 주어졌을 때 모든 정수를 0으로 만들기 위해 필요한 최소 연산의 횟수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 n과 m (2 ≤ n, m ≤ 50)이 주어지며, n은 격자의 행 개수, m은 격자의 열 개수를 나타낸다. 그 다음 n개의 줄에 각각 격자의 해당 행에 있는 m개의 정수가 열 순서대로 주어진다. 각 정수는 0 이상 1,000 이하이다.

출력
각 테스트 케이스마다 필요한 연산의 최소 횟수를 한 줄에 출력한다.
'''
