
如果我是这个 Agent，我不会把它写成普通教程。

而是写成一本书。

更准确地说，是一种 **"Research Reconstruction Notebook（科研重构笔记）"**。

它不是告诉用户答案，而是在模拟作者当年的思维过程。

下面就是我认为的 Stage3 最终交付物。

---

# Stage 3 · Reconstructing the Paper

> Goal
>
> 我们现在不会阅读论文，也不会阅读源码。
>
> 我们的目标是重新经历作者发明算法的过程。
>
> 当这一阶段结束时，你应该已经能够独立设计出论文最核心的数学表达式，并能够预测源码的大致结构。
>
> 如果这一阶段完成得足够好，那么阅读论文将变成一种"验证"，而不是"学习"。

---

# Chapter 1：今天，如果世界上还没有这篇论文……

假设今天是：

```
2023.01.01
```

GitHub 是空的。

论文不存在。

整个实验室只有一句话。

> 我们想研究 Federated Reinforcement Learning 在 Byzantine Attack 下为什么会失败。

现在。

你就是第一作者。

请忘记论文。

从零开始。

---

# Chapter 2：先不要写代码。

真正的软件工程师第一件事情：

不是 Coding。

而是：

> **建模（Modeling）。**

所以第一件事情不是：

```text
class Attack
```

而是：

整个系统里面到底有哪些对象？

我们画出整个世界。

```
          Environment
                │
                ▼
          Reinforcement Learning
                │
                ▼
             Client
                │
        Local Training
                │
                ▼
            Gradient
                │
                ▼
             Server
                │
      Gradient Aggregation
                │
                ▼
          Global Model
                │
                ▼
           Broadcast Back
```

观察整个 Pipeline。

真正移动的是什么？

不是：

Environment。

不是：

Server。

不是：

Policy。

真正移动的是：

> **Gradient。**

于是。

整个系统最重要的数据对象终于出现。

```
Gradient
```

这就是整个论文真正的主角。

---

# Chapter 3：重新设计 Repository

既然已经知道世界里有哪些对象。

Repository 自然就出现了。

```
frl/

├── train.py
├── client.py
├── server.py
├── aggregator.py
└── attack.py
```

为什么只有五个文件？

因为整个世界也只有五种职责。

| 文件            | 职责       |
| ------------- | -------- |
| train.py      | 驱动整个训练流程 |
| client.py     | 本地 RL 训练 |
| server.py     | 接收梯度并广播  |
| aggregator.py | 聚合算法     |
| attack.py     | 恶意客户端    |

注意。

这里还没有任何论文。

整个 Repository 已经设计出来了。

这就是：

> **Architecture First**

---

# Chapter 4：真正的数据结构是什么？

现在。

开始设计程序。

第一步不是函数。

而是：

数据。

整个程序到底在传递什么？

答案其实只有三个。

---

## Data Structure ①

```
Policy
```

数学表示：

[
\pi_\theta
]

它代表：

整个 Agent 的行为。

它几乎不会离开 Client。

---

## Data Structure ②

```
Gradient
```

数学表示：

[
g_i
]

这是整个系统真正流动的数据。

Client 输出。

Server 输入。

所有攻击都围绕它展开。

于是：

论文里的

[
g_i
]

终于有了真正的软件身份。

```
gradient
```

不是公式。

只是一个变量。

---

## Data Structure ③

```
Global Gradient
```

数学表示：

[
g_{global}
]

它是：

Server 唯一真正关心的数据。

整个 Aggregation 的目的：

就是把很多：

```
gradient
```

变成：

```
global_gradient
```

---

# Chapter 5：先让程序跑起来

真正优秀的软件工程师。

第一件事情不是写算法。

而是：

让程序：

> **先跑起来。**

于是。

整个训练流程。

只剩下最小 Skeleton。

```python
for round in training:

    gradients = []

    for client in clients:

        gradient = client.train()

        gradients.append(gradient)

    global_gradient = aggregate(gradients)

    broadcast(global_gradient)
```

停。

现在不要继续。

观察一下。

整个程序。

已经完成了吗？

答案：

已经完成了。

虽然没有任何攻击。

但是：

Federated Reinforcement Learning

已经存在。

---

# Chapter 6：论文真正开始的地方

重新观察 Pipeline。

```
Client

↓

Gradient

↓

Server
```

如果我是攻击者。

我能改哪里？

Environment？

不能。

Server？

通常不能。

Client？

可以。

但真正上传服务器之前。

还有一个位置。

```
Client

↓

Gradient

↓

Attack

↓

Server
```

于是。

第五个模块终于诞生。

```
attack.py
```

注意。

不是因为论文有：

attack.py

所以我们才写。

而是：

Pipeline 强迫我们必须拥有：

attack.py。

这就是：

Architecture 推导。

---

# Chapter 7：重新发明论文

现在。

终于进入论文真正的创新。

目标：

攻击 Server。

第一反应：

修改 Gradient。

于是：

```
gradient

↓

attack()

↓

gradient'
```

问题来了。

Attack 应该改什么？

两个选择。

```
长度

或者

方向
```

以前所有工作。

几乎都在修改：

长度。

于是：

```
gradient *= 100
```

或者：

```
gradient *= -100
```

但是。

如果服务器：

检查异常值。

这些攻击。

都会暴露。

所以。

新的问题出现。

---

> 有没有可能：

> **方向变化很大。**

> **长度几乎不变。**

如果能够做到。

Server 会发生什么？

---

# Chapter 8：公式不是数学，而是设计语言

现在。

不要翻论文。

开始真正设计。

我们的目标：

```
方向改变

长度保持
```

第一步。

定义方向。

```
u
```

要求：

它只能代表方向。

不能代表长度。

所以：

[
||u||=1
]

为什么？

因为：

单位向量。

天然没有长度。

第二步。

恢复长度。

于是：

我们得到：

[
g'=\alpha u
]

停。

这里就是整篇论文最重要的一刻。

不要继续。

观察这个式子。

它其实什么都没决定。

真正没有决定的是：

[
\alpha
]

它到底应该是多少？

如果：

太大。

容易暴露。

太小。

攻击失败。

那么。

唯一合理的答案就是：

> 保持和正常梯度一样长。

于是：

[
\alpha = ||g||
]

整个攻击公式终于出现。

[
g'=||g||\cdot u
]

注意。

这是我们自己推出来的。

不是论文告诉我们的。

---

# Chapter 9：公式如何变成代码？

现在。

公式已经完成。

开始翻译。

第一步。

读取正常梯度长度。

```python
norm = torch.norm(gradient)
```

对应：

[
||g||
]

第二步。

准备攻击方向。

```python
direction = attack_direction
```

对应：

[
u
]

第三步。

保证方向没有长度。

```python
direction = direction / direction.norm()
```

对应：

[
\frac{u}{||u||}
]

第四步。

恢复正常长度。

```python
attacked_gradient = norm * direction
```

对应：

[
g'=||g||\cdot u
]

于是。

整个论文最核心的公式。

最后只剩下四行代码。

---

# Chapter 10：论文、数学、代码，终于统一

直到现在。

我们才建立真正的映射关系。

| 作者脑中的想法  | 数学表达       | 代码实现               | 软件职责   |   |          |                                 |           |
| -------- | ---------- | ------------------ | ------ | - | -------- | ------------------------------- | --------- |
| 保持正常梯度长度 | (          |                    | g      |   | )        | `torch.norm()`                  | 获取统计量     |
| 只保留方向    | (u)        | `attack_direction` | 构造攻击方向 |   |          |                                 |           |
| 去掉方向的长度  | (\frac{u}{ |                    | u      |   | })       | `direction /= direction.norm()` | Normalize |
| 恢复正常长度   | (          |                    | g      |   | \cdot u) | `norm * direction`              | 最终攻击梯度    |

请注意这里的阅读顺序。

不是：

> 数学 → 代码。

而是：

> **问题 → 软件架构 → 数据结构 → Pipeline → 数学约束 → 数学公式 → 代码实现。**

数学公式只是整个设计过程中的一种中间表示，它既不是起点，也不是终点。

---

# 本阶段总结

完成本阶段后，你应该已经能够做到：

* 不看论文，画出整个 FRL 系统的数据流。
* 独立设计最小 Repository，并解释每个模块的职责。
* 说明为什么攻击模块必须位于 Client 与 Server 之间。
* 从"方向改变、长度保持"这一设计目标，自然推导出攻击公式，而不是死记硬背。
* 将论文核心公式逐项映射到对应的代码实现。

此时再打开论文，你看到的不再是陌生的公式，而是**你已经亲手设计过的软件系统，用数学语言重新描述了一遍。**

---

**我认为，这种交付物还可以继续进化。** 我不会把它叫做"教程"，而会叫做 **Research Reconstruction Notebook**。它的每一章都遵循固定模式：

> **为什么会有这个模块？ → 软件架构如何演化？ → 数据如何流动？ → 数学如何约束设计？ → 数学如何落到代码？ → 真实仓库中对应哪个文件、哪个类、哪个函数。**

这样，用户最终学到的不只是这一篇论文，而是一种可以迁移到任何优秀论文上的研究与工程思维。
