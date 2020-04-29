from sys import stdin,stdout
def main():
    for a in range(int(input())):
        n,ml = [int(x) for x in stdin.readline().split()]
        m = [int(x) for x in stdin.readline().split()]
        prof = 0
        remc = 0
        ans = ['-']*n
        for i in range(n):
            d,f,b = [int(x) for x in stdin.readline().split()]
            if m[d-1]:
                m[d-1] -= 1
                ans[i] = d
                prof += f
            else:
                prof += b
                remc += 1
        remd = []
        for i in range(ml):
            if m[i]:
                remd.extend([i+1]*m[i])
            if len(remd) >= remc:
                break
        i = 0
        print(remd)
        for j in range(n):
            if ans[j] == '-':
                ans[j] = remd[i]
                i += 1
        print(prof)
        print(' '.join([str(x) for x in ans]))
if __name__ == "__main__":
    main()