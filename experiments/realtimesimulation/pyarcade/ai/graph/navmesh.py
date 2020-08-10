import heapq

open_list = []

heapq.heappush(open_list, (40, 1))
heapq.heappush(open_list, (20, 3))
heapq.heappush(open_list, (30, 4))
heapq.heappush(open_list, (10, 5))

print(open_list[0][1])

nodes =[]