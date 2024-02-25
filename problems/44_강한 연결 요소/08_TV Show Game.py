
'''
url: https://www.acmicpc.net/problem/16367
제목: TV Show Game
번호: 16367

문제
Mr. Dajuda, who is famous for a TV show program, occasionally suggests an interesting game for the audience and gives them some gifts as a prize. The game he suggested this week can be explained as follows.
The k(> 3) lamps on the stage are all turned off at the beginning of the game. For convenience, lamps are numbered from 1 to k. Each lamp has a color, either red or blue. However, the color of a lamp cannot be identified until it is turned on. Game participants are asked to select three lamps at random and to guess the colors of them. Then each participant submits a paper on which the predicted colors of selected lamps are recorded to Mr. Dajuda, the game host. When all the lamps are turned on, each participant checks how many predicted colors match the actual colors of the lamps. If two or more colors match, he/she will receive a nice gift as a prize.
Mr. Dajuda prepared a special gift today. That is, after reviewing all the papers received from the game participants he tries to adjust the color of each lamp so that every participant can receive a prize if possible.
Given information about the predicted colors as explained above, write a program that determines whether the colors of all the lamps can be adjusted so that all the participants can receive prizes.

입력
Your program is to read from standard input. The input starts with a line containing two integers, k and n (3 < k ≤ 5,000, 1 ≤ n ≤ 10,000), where k is the number of lamps and n the number of game participants. Each of the following n lines contains three pairs of (l, c), where l is the lamp number he/she selected and c is a character, either B for blue or R for red, which denotes the color he/she guessed for the lamp. There is a blank between l and c and each pair of (l, c) is separated by a blank as well as shown in following samples.

출력
Your program is to write to standard output. If it is possible that all the colors can be adjusted so that every participant can receive a prize, print k characters in a line. The ith character, either B for blue or R for red represents the color of the ith lamp. If impossible, print -1. If there are more than one answer, you can print out any of them.
'''
