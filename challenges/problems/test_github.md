# Test problem

https://facelessuser.github.io/pymdown-extensions/extensions/superfences/
```python
def hello(name="world"):
    print(f"Hello, {name}")
name = input("Name: ")
hello(name)
```
```c
#include <stdio.h>
int main() {
    // printf() displays the string inside quotation marks Lorem ipsum
    printf("Hello, World!");
    return 0;
}
```

## LaTeX

https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/

$`\begin{align} E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i
v_i - \sum_j c_j h_j \end{align}`$

$`\begin{align} p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right)
\\ p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right) \end{align}`$

## Blocks
<details open>
    <summary>Did you know?</summary>
    You can create a note with Blocks!
</details>
<details>
    <summary>Hidden note</summary>
    Secret inside!
</details>
