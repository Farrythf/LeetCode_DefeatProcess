## 题目描述

判断一个数是不是回文数

```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 121
Output: true
```

## 思路

本题思路是比较，我把他们一个一个digit分离出来然后从头开始一个一个比较，虽对但慢，一行solution中转成str，反向再一次性比对的方法牛逼，只能说是学到了。

## 成绩

时间快于13.62%的其他玩家，内存低于61.29%的其他玩家
