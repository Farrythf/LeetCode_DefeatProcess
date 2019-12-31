## 题目描述

找给定字符串中的最长回文子字符串

```
Given "babad"

The answer is "bab", "aba" is also a valid answer, not necessary to provide all of them.
```

## 思路

找回文字符串就迭代判断就好了，我的代码中分成了奇数回文字符串和偶数回文字符串分别判断，其实这两种回文子串是可以合并的。只要将迭代函数的参数改成待判断字符的index就可以合并起来了。

## 成绩

时间快于43.42%的其他玩家，内存低于46.10%的其他玩家
