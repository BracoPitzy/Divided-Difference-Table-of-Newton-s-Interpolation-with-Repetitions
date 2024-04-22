# Divided-Difference-Table-of-Newton-s-Interpolation-with-Repetitions
SCU College of Mathematics Numerical Analysis Assignment: Construct a divided difference table of Newton's interpolation formula with repetitions based on the given interpolation constraint conditions.

# Problem
Construct a divided difference table of Newton's interpolation formula with repetitions based on the given interpolation constraint conditions. The interpolation polynomial $p(x)$ satisfies the interpolation constraints at each node $x_k$:
$$p^{(k)}(x_k)=f^{(k)}(x_k),k=0,1,2,\cdots,s.\quad \quad \quad(1)$$
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
        <td>${f}′(x_i)$</td>
        <td>-</td>
        <td>-0.1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>${f}′′(x_i)$</td>
        <td>-</td>
        <td>-</td>
        <td>-0.5</td>
    </tr>
</table>

<p align="center">
    <b>Table 1: Interpolation Constraint Conditions</b>
</p>

input:  
6  
1 2 2 3.5 3.5 3.5  
0.5 2.5 -0.1 0.3 1 -0.5  

* The first line of numbers represents the number of interpolation constraints, which in the example is 6.
* The second line contains interpolation node data organized in increasing order, and the number of data points is specified by the number in the first line.
* The third line represents the constraints corresponding to the interpolation nodes, and the number of constraints is specified by the number in the first line. If duplicate nodes appear in the second line of data, it indicates that the constraint at a node is determined by Equation $(1)$ and is sorted in increasing order of derivative order.

The algorithm is required to design to construct the divided difference table of Newton's interpolation formula with repetitions as shown below. Table 2 presents the calculated Newton's divided differences (rounded to 4 decimal places).

<table align="center">
    <tr>
        <td>$f(x_i)$</td>
        <td>$Df$</td>
        <td>$D^2f$</td>
        <td>$D^3f$</td>
        <td>$D^4f$</td>
        <td>$D^5f$</td>
    </tr>
    <tr>
        <td>0.5000</td>
        <td>0.0000</td>
        <td>0.0000</td>
        <td>0.0000</td>
        <td>0.0000</td>
        <td>0.0000</td>
    </tr>
    <tr>
        <td>2.5000</td>
        <td>2.0000</td>
        <td>0.0000</td>
        <td>0.0000</td>
        <td>0.0000</td>
        <td>0.0000</td>
    </tr>
    <tr>
        <td>2.5000</td>
        <td>-0.1000</td>
        <td>-2.1000</td>
        <td>0.0000</td>
        <td>0.0000</td>
        <td>0.0000</td>
    </tr>
    <tr>
        <td>0.3000</td>
        <td>-1.4667</td>
        <td>-0.9111</td>
        <td>0.4756</td>
        <td>0.0000</td>
        <td>0.0000</td>
    </tr>
    <tr>
        <td>0.3000</td>
        <td>1.0000</td>
        <td>1.6444</td>
        <td>1.7037</td>
        <td>0.4913</td>
        <td>0.0000</td>
    </tr>
    <tr>
        <td>0.3000</td>
        <td>1.0000</td>
        <td>-0.2500</td>
        <td>-1.2630</td>
        <td>-1.9778</td>
        <td>-0.9876</td>
    </tr>
</table>

<p align="center">
   <b>Table 2: Interpolation Constraint Conditions</b>
</p>

# File Overview
* `hw3_newton.py`: This code is an interface for submitting and validating Python code on the Newton Online Judging platform at [http://moodle.numecode.com/](http://moodle.numecode.com/).
  * `inputdata ()`:
    * Functionality: This function inputdata implements the input of test data.
    * Return Values: `x` retrieves an array of nodes arranged in increasing order; `y` retrieves an array of constraint conditions corresponding to the nodes in `x`.
  * `outputdata (s)`:
    * Functionality: This function outputdata implements the formatted output of Newton's divided differences.
    * Parameter Description: The input parameter `s` is the matrix form of the Newton's divided difference table saved as Table 2.
  * `DividedDiffWithRepetitions (x, y)`:
    * Functionality: This function calculates the divided differences using the Newton's interpolation formula with repetitions.
    * Parameter Description: The input parameter `x` is an array of nodes arranged in increasing order, including repetitions; the input parameter `y` is an array of constraint conditions corresponding to the nodes in `x`, both arrays `x` and `y` have the same length.
    * Return Value: The return value `coeff` is the result of the divided differences saved in the matrix form as shown in Table 2.
* `DividedDiffWithRepetitions.py`: Code for Calculating the divided differences using the Newton's interpolation formula with repetitions.
