
'''
url: https://www.acmicpc.net/problem/4008
제목: 특공대
번호: 4008

문제
1부터 n까지 번호가 붙여진 n명의 병사들로 이루어진 군대의 지휘관이 있다. 이 지휘관은 앞으로의 전투를 위하여 n명의 병사들을 여러 개의 특공대로 나누고자 한다. 결속력과 사기를 높이기 위하여 각 특공대는 {i, i+1, ..., i+k}형태의 번호가 연속하는 병사들로 구성된다. 
각 병사 i의 전투력은 xi이다. 병사들 {i, i+1, ..., i+k}로 구성된 특공대의 전투력 x는 원래는 각 병사의 전투력의 합으로 계산되었다. 달리 말하면 x = xi + xi+1 + ... + xk이었다.
그러나 여러 해의 영광스러운 승리를 통하여 특공대의 전투력을 다음과 같이 조정해야 하는 것으로 결론을 내렸다: 특공대의 조정된 전투력 x′는 등식 x′ = ax2 + bx + c로 계산한다. 여기서 a, b, c는 알려져 있는 계수들로서 a<0이고, x는 특공대의 원래 정의된 전투력이다.
여러분이 할 일은 모든 특공대의 조정된 전투력의 합을 최대화하도록 병사들을 특공대로 나누는 것이다.
예를 들어, 4명의 병사들이 있고, 각 병사의 전투력 x1 = 2, x2 = 2, x3 = 3, x4 = 4라 하자. 특공대의 조정된 전투력 등식에 있는 계수가 a=-1, b=10, c=-20이라 하자. 이러한 경우, 최적인 해는 병사들을 다음과 같이 세 개의 특공대로 나누는 것이다: 첫 번째 특공대는 병사 1과 2로 구성하고, 두 번째 특공대는 병사 3으로 구성하고, 세 번째 특공대는 병사 4로 구성한다. 이들 세 특공대의 원래의 전투력은 각각 4, 3, 4이고 조정된 전투력은 각각 4, 1, 4이다. 이렇게 나눌 때 조정된 전체 전투력은 각 특공대의 조정된 전투력의 합인 9이며, 이보다 더 좋은 해가 없음을 알 수 있다.

입력
입력은 세 줄로 구성된다. 첫 번째 줄에 전체 병사들 수인 양의 정수 n이 주어진다. 두 번째 줄에 특공대의 조정된 전투력 계산 등식의 계수인 세 정수 a, b, c가 주어진다. 마지막 줄에 병사들 1, 2, ..., n의 전투력을 나타내는 n개의 정수 x1, x2, ..., xn이 공백을 사이에 두고 주어진다.
n ≤ 1,000,000, -5 ≤ a ≤ -1, |b| ≤ 10,000,000, |c| ≤ 30,000,000, 1 ≤ xi ≤ 100

출력
얻을 수 있는 최대의 조정된 전체 전투력을 나타내는 하나의 정수를 한 줄에 출력한다.
'''
