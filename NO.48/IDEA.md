## 题目描述

这个题是给你一个矩阵，然后你需要将这个矩阵翻转90度。这里的矩阵是一个list的list。你需要在原来的那个矩阵上直接修改把他倒过来。

```
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

## 思路

第一眼看上去莫得任何想法，于是first try就开启暴力模式= = 所谓翻转就是大list里每个list的第n个元素重新组成一个新的list呗，那就先取个长度，这个长度就是n然后做两个循环让每个竖行变成横行就完事了，然后随便跑了一下发现，哎这结果还行啊那果断就这样了-^-

## 成绩

时间快于95.97%的其他玩家，内存低于56.99%的其他玩家
