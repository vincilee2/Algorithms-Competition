# Binary Indexed Tree

construct binary indexed tree from array
```
5 3 7 9 6 4 1 2 9 10
```

run `sh run.py.sh`, will output the process of construction below:
```
update value 5 from arr[1]
add value 5 to tree[1] = 0 get 5
update index from 1 to view parent 10
current tree is :
------------------------------------------1000:0
-------------------100:0
--------10:0            -------110:0            ------1010:0
---1:5      --11:0      -101:0      -111:0      1001:0
add value 5 to tree[2] = 0 get 5
update index from 10 to view parent 100
current tree is :
------------------------------------------1000:0
-------------------100:0
--------10:5            -------110:0            ------1010:0
---1:5      --11:0      -101:0      -111:0      1001:0
add value 5 to tree[4] = 0 get 5
update index from 100 to view parent 1000
current tree is :
------------------------------------------1000:0
-------------------100:5
--------10:5            -------110:0            ------1010:0
---1:5      --11:0      -101:0      -111:0      1001:0
add value 5 to tree[8] = 0 get 5
update index from 1000 to view parent 10000
current tree is :
------------------------------------------1000:5
-------------------100:5
--------10:5            -------110:0            ------1010:0
---1:5      --11:0      -101:0      -111:0      1001:0
update value 3 from arr[2]
add value 3 to tree[2] = 5 get 8
update index from 10 to view parent 100
current tree is :
------------------------------------------1000:5
-------------------100:5
--------10:8            -------110:0            ------1010:0
---1:5      --11:0      -101:0      -111:0      1001:0
add value 3 to tree[4] = 5 get 8
update index from 100 to view parent 1000
current tree is :
------------------------------------------1000:5
-------------------100:8
--------10:8            -------110:0            ------1010:0
---1:5      --11:0      -101:0      -111:0      1001:0
add value 3 to tree[8] = 5 get 8
update index from 1000 to view parent 10000
current tree is :
------------------------------------------1000:8
-------------------100:8
--------10:8            -------110:0            ------1010:0
---1:5      --11:0      -101:0      -111:0      1001:0
update value 7 from arr[3]
add value 7 to tree[3] = 0 get 7
update index from 11 to view parent 100
current tree is :
------------------------------------------1000:8
-------------------100:8
--------10:8            -------110:0            ------1010:0
---1:5      --11:7      -101:0      -111:0      1001:0
add value 7 to tree[4] = 8 get 15
update index from 100 to view parent 1000
current tree is :
------------------------------------------1000:8
------------------100:15
--------10:8            -------110:0            ------1010:0
---1:5      --11:7      -101:0      -111:0      1001:0
add value 7 to tree[8] = 8 get 15
update index from 1000 to view parent 10000
current tree is :
-----------------------------------------1000:15
------------------100:15
--------10:8            -------110:0            ------1010:0
---1:5      --11:7      -101:0      -111:0      1001:0
update value 9 from arr[4]
add value 9 to tree[4] = 15 get 24
update index from 100 to view parent 1000
current tree is :
-----------------------------------------1000:15
------------------100:24
--------10:8            -------110:0            ------1010:0
---1:5      --11:7      -101:0      -111:0      1001:0
add value 9 to tree[8] = 15 get 24
update index from 1000 to view parent 10000
current tree is :
-----------------------------------------1000:24
------------------100:24
--------10:8            -------110:0            ------1010:0
---1:5      --11:7      -101:0      -111:0      1001:0
update value 6 from arr[5]
add value 6 to tree[5] = 0 get 6
update index from 101 to view parent 110
current tree is :
-----------------------------------------1000:24
------------------100:24
--------10:8            -------110:0            ------1010:0
---1:5      --11:7      -101:6      -111:0      1001:0
add value 6 to tree[6] = 0 get 6
update index from 110 to view parent 1000
current tree is :
-----------------------------------------1000:24
------------------100:24
--------10:8            -------110:6            ------1010:0
---1:5      --11:7      -101:6      -111:0      1001:0
add value 6 to tree[8] = 24 get 30
update index from 1000 to view parent 10000
current tree is :
-----------------------------------------1000:30
------------------100:24
--------10:8            -------110:6            ------1010:0
---1:5      --11:7      -101:6      -111:0      1001:0
update value 4 from arr[6]
add value 4 to tree[6] = 6 get 10
update index from 110 to view parent 1000
current tree is :
-----------------------------------------1000:30
------------------100:24
--------10:8            ------110:10            ------1010:0
---1:5      --11:7      -101:6      -111:0      1001:0
add value 4 to tree[8] = 30 get 34
update index from 1000 to view parent 10000
current tree is :
-----------------------------------------1000:34
------------------100:24
--------10:8            ------110:10            ------1010:0
---1:5      --11:7      -101:6      -111:0      1001:0
update value 1 from arr[7]
add value 1 to tree[7] = 0 get 1
update index from 111 to view parent 1000
current tree is :
-----------------------------------------1000:34
------------------100:24
--------10:8            ------110:10            ------1010:0
---1:5      --11:7      -101:6      -111:1      1001:0
add value 1 to tree[8] = 34 get 35
update index from 1000 to view parent 10000
current tree is :
-----------------------------------------1000:35
------------------100:24
--------10:8            ------110:10            ------1010:0
---1:5      --11:7      -101:6      -111:1      1001:0
update value 2 from arr[8]
add value 2 to tree[8] = 35 get 37
update index from 1000 to view parent 10000
current tree is :
-----------------------------------------1000:37
------------------100:24
--------10:8            ------110:10            ------1010:0
---1:5      --11:7      -101:6      -111:1      1001:0
update value 9 from arr[9]
add value 9 to tree[9] = 0 get 9
update index from 1001 to view parent 1010
current tree is :
-----------------------------------------1000:37
------------------100:24
--------10:8            ------110:10            ------1010:0
---1:5      --11:7      -101:6      -111:1      1001:9
add value 9 to tree[10] = 0 get 9
update index from 1010 to view parent 1100
current tree is :
-----------------------------------------1000:37
------------------100:24
--------10:8            ------110:10            ------1010:9
---1:5      --11:7      -101:6      -111:1      1001:9
update value 10 from arr[10]
add value 10 to tree[10] = 9 get 19
update index from 1010 to view parent 1100
current tree is :
-----------------------------------------1000:37
------------------100:24
--------10:8            ------110:10            -----1010:19
---1:5      --11:7      -101:6      -111:1      1001:9
```