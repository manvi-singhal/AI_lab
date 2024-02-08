def check(nodeArr, count, s):
    val = 0
    m = 1

    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        for j in range(count):
            if nodeArr[j].c == ch:
                break
        val += m * nodeArr[j].v
        m *= 10

    return val


def permutation(count, nodeArr, n, s1, s2, s3, use):
    if n == count - 1:
        for i in range(10):
            if use[i] == 0:
                nodeArr[n].v = i
                if check(nodeArr, count, s1) + check(nodeArr, count, s2) == check(nodeArr, count, s3):
                    print("\nSolution found: ", end="")
                    for j in range(count):
                        print(nodeArr[j].c, "=", nodeArr[j].v, end=" ")
                    return True
        return False

    for i in range(10):

        if use[i] == 0:
            nodeArr[n].v = i
            use[i] = 1
            if permutation(count, nodeArr, n + 1, s1, s2, s3, use):
                return True
            use[i] = 0
    return False


def solveCryptographic(s1, s2, s3):
    count = 0
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    freq = [0] * 26

    for i in range(l1):
        freq[ord(s1[i]) - ord('A')] += 1
    for i in range(l2):
        freq[ord(s2[i]) - ord('A')] += 1
    for i in range(l3):
        freq[ord(s3[i]) - ord('A')] += 1

    for i in range(26):
        if freq[i] > 0:
            count += 1

    if count > 10:
        print("Invalid strings")
        return False

    class Node:
        pass

    nodeArr = [Node() for _ in range(count)]

    j = 0
    for i in range(26):
        if freq[i] > 0:
            nodeArr[j].c = chr(i + ord('A'))
            j += 1

    use = [0] * 10

    return permutation(count, nodeArr, 0, s1, s2, s3, use)

def main():
    s1 = input("Enter first string: ").upper()
    s2 = input("Enter second string: ").upper()
    s3 = input("Enter third string: ").upper()
    if not solveCryptographic(s1, s2, s3):
        print("No solution")


if __name__ == "__main__":
    main()

# Enter first string: SCOOBY
# Enter second string: DOOO
# Enter third string: BUSTED
# Solution found: B = 2 C = 9 D = 7 E = 6 O = 4 S = 1 T = 8 U = 0 Y = 3 