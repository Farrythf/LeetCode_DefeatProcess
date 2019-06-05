## 题目描述

此题是一道经典的数学题？！说有个m x n的表格，你要从这个表格的左上角走到右下角，每次只能往右走或者往下走，那么有多少种走法呢？

```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

## 思路

那么都说了是经典的数学题了，学过排列组合的朋友们肯定做过这题。所以答案很显而易见的是C(m+n-2,m-1)。物理意义是你一共要走m+n-2步，而这其中呢有m-1步是往右走的，所以你需要从总步数里找m-1个位置，所以答案就是一个C。那么问题来了，怎么写这个C呢？math库里有个factory函数，用现成的库函数做得到的结果还贼好。那我肯定是不能屈服于其淫威之下（？？？）于是FirstTry写了个递归，结果time exceed...然后写了个垃圾版的self-design factory草草结束。   
`math库牛逼！math库对不起！`

## 成绩

快于70.76%的python玩家，内存使用低于59.40%的python玩家
