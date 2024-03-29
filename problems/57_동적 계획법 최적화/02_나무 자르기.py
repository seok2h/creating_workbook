
'''
url: https://www.acmicpc.net/problem/13263
제목: 나무 자르기
번호: 13263

문제
높이가 a1, a2, ..., an인 나무 n개를 전기톱을 이용해서 자르려고 한다.
i번 나무에 전기톱을 사용할 때 마다 그 나무의 높이는 1만큼 감소한다. 전기톱은 사용할 때 마다 충전해야 한다. 전기톱을 충전하는 비용은 완전히 자른 나무의 번호에 영향을 받는다. 즉, 높이가 0이 되어버린 나무의 번호에 영향을 받는다. 완전히 잘려진 나무의 번호 중 최댓값이 i이면, 전기톱을 충전하는 비용은 bi이다. 완전히 잘려진 나무가 없다면 전기톱은 충전할 수가 없다. 가장 처음에 전기톱은 충전되어져 있다.
나무의 높이 ai와 각각의 나무에 대한 충전 비용 bi가 주어졌을 때, 모든 나무를 완전히 자르는데 (높이를 0으로 만드는데) 필요한 충전 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄에는 a1, a2, ..., an이, 셋째 줄에는 b1, b2, ..., bn이 주어진다. (1 ≤ ai ≤ 109, 0 ≤ bi ≤ 109)
a1 = 1이고, bn = 0이며, a1 < a2 < ... < an, b1 > b2 > ... > bn을 만족한다.

출력
나무를 완전히 자르는 충전 비용의 최솟값을 출력한다.
'''
