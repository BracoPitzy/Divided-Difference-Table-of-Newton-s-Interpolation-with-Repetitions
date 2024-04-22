# Divided-Difference-Table-of-Newton-s-Interpolation-with-Repetitions
SCU College of Mathematics Numerical Analysis Assignment: Construct a divided difference table of Newton's interpolation formula with repetitions based on the given interpolation constraint conditions.

# Problem
Construct a divided difference table of Newton's interpolation formula with repetitions based on the given interpolation constraint conditions. The interpolation polynomial $p(x)$ satisfies the interpolation constraints at each node $x_k$:
$$p^{(k)}(x_k)=f^{(k)}(x_k),k=0,1,2,\cdots,s.    (1)$$
For example, the interpolation constraint conditions are shown in the following table:
<table align="center">
    <tr>
        <td>$x_i$</td>
        <td>1</td>
        <td>2</td>
        <td>3.5</td>
    </tr>
    <tr>
        <td>$f(x_i)$</td>
        <td>0.5</td>
        <td>2.5</td>
        <td>0.3</td>
    </tr>
    <tr>
        <td>$f′(x_i)$</td>
        <td>-</td>
        <td>-0.1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>$f′′(x_i)$</td>
        <td>-</td>
        <td>-</td>
        <td>-0.5</td>
    </tr>
</table>

<div style="text-align:center;">
<h4>Table 1: Interpolation Constraint Conditions</h4>
</div>

input:
6
1 2 2 3.5 3.5 3.5
0.5 2.5 -0.1 0.3 1 -0.5

* The first line of numbers represents the number of interpolation constraints, which in the example is 6.
* The second line contains interpolation node data organized in increasing order, and the number of data points is specified by the number in the first line.
* The third line represents the constraints corresponding to the interpolation nodes, and the number of constraints is specified by the number in the first line. If duplicate nodes appear in the second line of data, it indicates that the constraint at a node is determined by Equation (1) and is sorted in increasing order of derivative order.

The algorithm is required to design to construct the divided difference table of Newton's interpolation formula with repetitions as shown below. Table 2 presents the calculated Newton's divided differences (rounded to 4 decimal places).
| Table 2: Interpolation Constraint Conditions |
| $f(x^i)$ | $D^f$ | $D^2f$ | $D^3f$ | $D^4f$ | $D^5f$ |
| 0.5000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 2.5000 | 2.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 2.5000 | -0.1000 | -2.1000 | 0.0000 | 0.0000 | 0.0000 |
| 0.3000 | -1.4667 | -0.9111 | 0.4756 | 0.0000 | 0.0000 |
| 0.3000 | 1.0000 | 1.6444 | 1.7037 | 0.4913 | 0.0000 |
| 0.3000 | 1.0000 | -0.2500 | -1.2630 | -1.9778 | -0.9876 |
