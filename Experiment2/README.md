## 2. 0/1 Knapsack Using Dynamic Programming

### Aim

To implement the 0/1 Knapsack problem using Dynamic Programming and
analyze its time and space complexity.

### Algorithm

1.  Take the weights, values, and knapsack capacity.
2.  Create a Dynamic Programming table.
3.  For each item, decide whether to include it or exclude it.
4.  Choose the maximum value.
5.  Return the maximum profit.

### Python Program

``` python
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

result = knapsack(weights, values, capacity)

print("Maximum value:", result)
```

### Data (Input)

``` text
Weights: [2, 3, 4, 5]
Values: [3, 4, 5, 6]
Capacity: 5
```

### Result (Output)

``` text
Maximum value: 7
```

### Inference

The 0/1 Knapsack algorithm finds the maximum value within the given
capacity using Dynamic Programming.

### Analysis

-   Time complexity: `O(n × W)`
-   Space complexity: `O(n × W)`
-   `n` represents the number of items.
-   `W` represents the knapsack capacity.
