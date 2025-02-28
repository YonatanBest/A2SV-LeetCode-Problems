# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

songs, moments = map(int, input().split())
music = []
for i in range(songs):
    times, min_time = map(int, input().split())
    music.append([times, min_time])
 
arr = list(map(int, input().split()))
total = 0
index = 0
for i in arr:
    while total < i:
        total += music[index][0] * music[index][1]
        index += 1
    print(index)