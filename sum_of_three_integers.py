def findTriplets(arr, num):
    for i in range(0, num - 2):

        for j in range(i + 1, num - 1):

            for k in range(j + 1, num):

                if arr[i] + arr[j] + arr[k] == 0:
                    print(arr[i], arr[j], arr[k])

    # Driver code

arr = list(map(int, input("Enter the array Elements:").split()))
num = len(arr)
findTriplets(arr, num)

