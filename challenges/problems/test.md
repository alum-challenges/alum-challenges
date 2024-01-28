# Test problem

https://facelessuser.github.io/pymdown-extensions/extensions/superfences/

```{.python #id linenums="1" title="Example code block" pygments_style="monokai"}
def hello(name="world"):
    print(f"Hello, {name}")
name = input("Name: ")
hello(name)
```

    #!py3 "monokai"
    def hello(name="world"):
        print(f"Hello, {name}")
    name = input("Name: ")
    hello(name)

## LaTeX

https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/
\begin{align} E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i
v_i - \sum_j c_j h_j \end{align}

\begin{align} p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right)
\\ p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right) \end{align}

## Blocks

/// details | Did you know? open: True

You can create a note with Blocks! /// /// details | Hidden note!

Secret hint inside ///
