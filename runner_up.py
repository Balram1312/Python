# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arm = sorted(list(arr))

    for i in range(len(arm)):
        if i < len(arm) - 1:
            if arm[i] < arm[i + 1]:
                x= arm[i]
    print(x)