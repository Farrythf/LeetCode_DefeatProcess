## 题目描述

题目是给你一个矩阵，然后你需要将这个矩阵螺旋输出= =

```
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
```

## 思路

对于这道题，想法就很simple了，观察一下然后在纸上画画，发现所谓的螺旋输出就是首先，把第一行搞出来，然后贴着边输出一排。所以我的想法就是对于一个拿到的矩阵，首先把第一行放出来，然后对于横竖各输出一次边长减1，然后再对于横竖输出一次边长减2。以这四个动作为一个循环，以4X3的矩阵为例，先输出第一行的3个数然后竖着输出3个数`4-1`然后横着输出2个数`3-1`然后竖着输出2个数`4-2`最后横着输出1个数`3-2`以这四个动作为一个循环直到某次动作的时候输出个数减到0。然后就是算好起止点就ok啦。FirstTry Pass！撒花撒花
然后放个一行的代码接着模拜……

## 成绩

用时短于95.23%的python玩家，内存低于14.27%的python玩家