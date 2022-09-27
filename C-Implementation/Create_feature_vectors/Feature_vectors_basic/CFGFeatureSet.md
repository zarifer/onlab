# CFG feature set

+ \# of edges

+ \# of nodes

+ density

    + \# of edges / maximum \# of edges
    + $\frac{|E|}{(|V|*(|V|-1))}$

+ shortest path

    + for all node pairs, i guess

+ betweenness centrality

    + $C_B(v) =\sum_{s,t \in V} \frac{\sigma(s, t|v)}{\sigma(s, t)}$

        + $\sigma(s, t) = $ number of shortest $(s, t)$ paths
        + $\sigma(s, t|v) = $ number of shortest $(s, t)$ paths through $v$

+ closeness centrality

    + $C_C(v) = \frac{n - 1}{\sum_{u \in V} d(u, v)},$

        + $n = |V|$, the number of nodes
        + $d(v, u) = $ shortest path from $v$ to $u$

+ degree centrality

    + $C_D(v) = deg(v)$

        + degree of nodes
        + networkx normalizes it by dividing by the max possible degree $(n - 1)$

**for path & centrality metrics: minimum, maximum, median, mean, and standard deviation**


# CNN

+ 3 blocks

    + ConvB1
        + Conv1 (1D)
        + Conv2 (1D)
        + MaxPooling
        + Dropout
    + ConvB2
        + Conv3 (1D)
        + Conv4 (1D)
        + MaxPooling
        + Dropout
    + CB (classification block)
        + Flatten
        + Dense
        + Dropout
        + SoftMax

+ epochs: 200, batch size: 100
+ activation function for convolutional & fully connected layers: ReLU

# GEA

```
To generate AEs, we connected each selected graph with all samples from the opposite class using shared entry and exit nodes as illustrated in the basic example in subsection III-B.

Then, to study the effect of changing number of edges on the misclassification rate, we fixed the number of nodes and selected three samples with different number of edges as x sel in the AEs generation process
```
