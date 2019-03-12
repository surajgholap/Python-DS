import heapq


def main():
    "Implementation of heap using heapq"
    lis = [54, 2, 46, 2, 6, 54, 14, 3]
    heapq.heapify(lis)
    print(lis)
    print(heapq.heappop(lis))
    (heapq.heappush(lis, 66))
    print(lis)
    print(heapq.nlargest(3, lis))

if __name__ == "__main__":
    main()
