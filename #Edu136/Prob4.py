from sortedcontainers import SortedList
import bisect

sl = SortedList()

sl.add(2)
sl.add(0)
sl.add(4)

index = bisect.bisect_right(sl, 2)
print(index)


