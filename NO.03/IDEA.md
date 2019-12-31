## 题目描述

找给定字符串中没有重复的最长子字符串长度

```
Given "abcabcbbd"

"abcd" is a subsequence and not a substring!
The answer is "abc", with the length of 3. 
```

## 思路

找不重复的子列无非找两个index然后判断长度是否最长。所有元素一个一个放字典，如果看到一个已经存在的，就计算一下他之前的index只差够不够大，然后改变子字符串的头和重复元素的index，重复操作到最后就好了。

## 成绩

时间快于60.99%的其他玩家，内存低于46.10%的其他玩家
