# 入门指南

欢迎使用 DSAA3041 算法课程学习工作区！

## 环境设置

### C++ 开发环境

确保安装了 C++ 编译器：

```bash
# Linux/Mac
g++ --version

# Windows (MinGW or MSVC)
g++ --version
```

编译和运行 C++ 程序：

```bash
g++ -std=c++11 your_file.cpp -o output
./output
```

### Python 开发环境

确保安装了 Python 3：

```bash
python3 --version
```

运行 Python 程序：

```bash
python3 your_file.py
```

### Java 开发环境

确保安装了 JDK：

```bash
javac -version
java -version
```

编译和运行 Java 程序：

```bash
javac YourClass.java
java YourClass
```

## 工作流程

### 1. 选择学习内容

根据你的学习目标选择：
- **学习新的数据结构**：前往 `data_structures/` 目录
- **学习新的算法**：前往 `algorithms/` 目录
- **练习题目**：前往 `practice/` 目录

### 2. 使用模板

从 `templates/` 目录复制适合的模板：

```bash
cp templates/problem_template.py practice/leetcode/new_problem.py
```

### 3. 实现解决方案

在模板中填写：
1. 问题基本信息（名称、来源、难度、标签）
2. 问题描述
3. 解题思路
4. 代码实现
5. 测试用例

### 4. 测试和验证

运行你的代码并验证结果：

```bash
python3 your_solution.py
# 或
g++ -std=c++11 your_solution.cpp -o solution && ./solution
```

## 学习建议

### 数据结构学习顺序

1. **基础线性结构**
   - 数组、链表
   - 栈、队列

2. **树形结构**
   - 二叉树、二叉搜索树
   - 堆、优先队列

3. **高级结构**
   - 图、哈希表
   - 并查集、字典树

### 算法学习顺序

1. **基础算法**
   - 排序算法（冒泡、选择、插入、快排、归并）
   - 搜索算法（线性搜索、二分搜索）

2. **进阶算法**
   - 递归和分治
   - 动态规划
   - 贪心算法

3. **图算法**
   - DFS/BFS
   - 最短路径（Dijkstra、Floyd）
   - 最小生成树（Kruskal、Prim）

## 常见问题

### Q: 应该用什么语言？

A: 选择你最熟悉的语言。C++ 和 Python 是最常用的选择。

### Q: 如何组织代码？

A: 遵循项目的目录结构，将代码放在相应的子目录中。

### Q: 如何测试代码？

A: 在 main 函数或 if __name__ == "__main__" 块中添加测试用例。

## 其他资源

- 查看每个目录下的 README.md 了解更多详情
- 参考已有的示例实现学习代码风格
