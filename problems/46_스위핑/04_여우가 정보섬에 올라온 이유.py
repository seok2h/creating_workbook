
'''
url: https://www.acmicpc.net/problem/17131
제목: 여우가 정보섬에 올라온 이유
번호: 17131

문제
여우가 정보섬에 올라왔다!
오늘도 하늘에는 아름다운 별들이 빛나고 있다. 정보섬은 언덕 꼭대기에 위치해 있기 때문에 별이 잘 보이기로 유명하다. 그래서인지, 여우 한 마리가 정보섬에 올라와 밤하늘을 바라보며 별자리를 만들고 있다. 여우는 세 개의 별을 연결하여 V형 별자리를 만드는데, 그 이유는 V가 자신의 얼굴과 닮았기 때문이라나 뭐라나. 여우는 자신의 시점을 기준으로 생각하기 때문에, V가 회전한 모양(<, >, ㄴ, ㄱ, ^ 등)은 V라고 생각하지 않는다.
여우는 만들 수 있는 V형 별자리의 총 개수가 궁금해졌다. 그러나 일일이 세보기에는 별이 너무 많았기 때문에, 여우는 뛰어난 프로그래머인 당신에게 도움을 요청했다! 귀여운 여우를 위해 얼마나 많은 V형 별자리가 만들어질 수 있는지 계산해 주자.
V형 별자리를 명확하게 정의하면 다음과 같다. 세 별 (s,t,u)가 s.x < t.x < u.x이고 s.y > t.y < u.y이면 V형 별자리이다. 예를 들어 아래의 '정보섬의 밤하늘 참고도'에서 (a,b,c)는 V형 별자리를 이루지만 (d,b,c)는 d.x < b.x가 아니므로 V형 별자리가 아니다. V형 별자리의 개수를 셀 때, 한 별이 여러 별자리에 속할 수 있다.

답이 매우 커질 수 있으므로 (109+7)로 나눈 나머지를 출력한다.

입력
첫 줄에 별의 개수 N이 주어진다. 그 다음 줄부터 N개의 줄에 걸쳐 별의 좌표 x y가 주어진다.

출력
(만들 수 있는 V형 별자리의 개수) mod (109+7)을 출력한다.
'''
