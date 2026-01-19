# 复杂度分析指南

理解算法的时间和空间复杂度对于编写高效代码至关重要。

## 时间复杂度

### 常见复杂度类别

从快到慢排序：

1. **O(1)** - 常数时间
   - 示例：数组索引访问、哈希表查找

2. **O(log n)** - 对数时间
   - 示例：二分搜索、平衡二叉搜索树操作

3. **O(n)** - 线性时间
   - 示例：遍历数组、链表遍历

4. **O(n log n)** - 线性对数时间
   - 示例：归并排序、快速排序（平均情况）、堆排序

5. **O(n²)** - 平方时间
   - 示例：冒泡排序、选择排序、插入排序

6. **O(2ⁿ)** - 指数时间
   - 示例：递归斐波那契数列、子集生成

7. **O(n!)** - 阶乘时间
   - 示例：全排列生成

### 如何分析时间复杂度

1. **识别基本操作**：确定算法中的主要操作
2. **计算执行次数**：确定基本操作执行的次数
3. **忽略常数和低阶项**：只保留增长最快的项
4. **考虑最坏情况**：通常分析最坏情况复杂度

### 示例分析

```python
# O(n) - 单层循环
def linear_search(arr, target):
    for i in range(len(arr)):  # 执行 n 次
        if arr[i] == target:
            return i
    return -1

# O(n²) - 嵌套循环
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):         # 外层循环 n 次
        for j in range(n-i-1): # 内层循环约 n 次
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# O(log n) - 每次减半
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:       # 最多执行 log n 次
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 空间复杂度

### 空间使用来源

1. **输入空间**：存储输入数据
2. **辅助空间**：算法执行期间使用的额外空间
3. **输出空间**：存储输出结果

通常我们关注 **辅助空间复杂度**。

### 常见空间复杂度

- **O(1)**：只使用固定数量的额外空间
- **O(n)**：使用与输入大小成正比的额外空间
- **O(n²)**：使用二维数组等结构

### 示例

```python
# 空间复杂度 O(1) - 原地排序
def bubble_sort_inplace(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # 只使用了有限的额外变量

# 空间复杂度 O(n) - 使用额外数组
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # 需要额外空间
    right = merge_sort(arr[mid:])  # 需要额外空间
    return merge(left, right)

# 空间复杂度 O(log n) - 递归调用栈
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)   # 递归深度最多 log n
        quick_sort(arr, pi+1, high)
```

## 权衡取舍

- **时间-空间权衡**：有时可以用更多空间来获得更快的时间
  - 示例：记忆化（memoization）在动态规划中

- **平均 vs 最坏情况**：
  - 快速排序：平均 O(n log n)，最坏 O(n²)
  - 选择合适的情况进行优化

## 实用技巧

1. **使用大O记号**：关注增长率，忽略常数因子
2. **识别循环模式**：嵌套循环通常导致复杂度相乘
3. **递归分析**：使用递归树或主定理
4. **均摊分析**：某些操作的平均成本
