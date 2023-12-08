import sysimport sys

if __name__ == "__main__":
    print(ans)
    print(calculate_f(T, D))
  from collections import defaultdict

def calculate_f(t, d):
  if t % 2 == 0:
      half_t = t // 2
      if half_t * (t - half_t) >= d:
          return half_t + 1
      else:
          return half_t
  else:
      half_t = t // 2
      return half_t + 1 if half_t * (t - half_t) >= d else half_t





data = open("input.txt").read().strip().split('\n')
times, dist = data

times = [int(x) for x in times.split(':')[1].split()]
dist = [int(x) for x in dist.split(':')[1].split()]

T = int(''.join(map(str, times)))
D = int(''.join(map(str, dist)))

ans = 1
for i in range(len(times)):
    ans *= calculate_f(times[i], dist[i])

if __name__ == "__main__":
    print(ans)
    print(calculate_f(T, D))
  