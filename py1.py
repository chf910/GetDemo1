def pair_digital(n):
    # 初始化二维列表
    a = [[0 for _ in range(10)] for _ in range(10)]
    x1 = 0
    x2 = 0

    # 输入值
    x1 = int(input())
    for i in range(1, n):
        x2 = int(input())
        a[x1][x2] += 1
        x1 = x2

    # 输出结果
    for i in range(10):
        for j in range(i + 1):
            if a[i][j] != 0 and a[j][i] != 0:
                if i != j:
                    print(f"({i},{j})={a[i][j]},({j},{i})={a[j][i]}", end="\t")
                elif a[i][j] > 1:
                    print(f"({i},{j})={a[i][j]}", end="\t")
    print("\n====================")

    # 输出二维列表
    for i in range(10):
        for j in range(10):
            print(a[i][j], end="\t")
        print()

def main():
    n = int(input("input n: "))
    pair_digital(n)

if __name__ == "__main__":
    main()