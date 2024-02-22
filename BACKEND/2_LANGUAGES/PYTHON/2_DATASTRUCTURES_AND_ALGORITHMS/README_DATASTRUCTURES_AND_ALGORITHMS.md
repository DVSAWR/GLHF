## ALGORITHMS AND NOTATION

| **BIG O NOTATION (order of growth)** | **COMPLEXITY** | **Description**                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| O(1)                                 | CONSTANT       | The complexity of an algorithm is said to be constant if the steps required to complete the execution of an algorithm remain constant, irrespective of the number of inputs. The constant complexity is denoted by O(c) where c can be any constant number.                                                                                                                       |
| O(log(n))                            | LOGARITHMIC    | A logarithmic algorithm halves the list every time it’s run.                                                                                                                                                                                                                                                                                                                      |
| O(n)                                 | LINEAR         | Linear time algorithms mean that every single element from the input is visited exactly once, O(n) times. As the size of the input, N, grows our algorithm’s run time scales exactly with the size of the input.                                                                                                                                                                  |
| O(nlog(n))                           | LOG LINEAR     | It falls between O(n) and O(n2). This is the fastest time possible for a comparison sort. We cannot get any faster unless we use some special property, like Radix sort. O(n log n) is the fastest comparison sort time.                                                                                                                                                          |
| O(n²)                                | QUADRATIC      | The complexity of an algorithm is said to be quadratic when the steps required to execute an algorithm are a quadratic function of the number of items in the input. Quadratic complexity is denoted as O(n²):                                                                                                                                                                    |
| O(n³)                                | CUBIC          | A triple nested loop is O(n3).                                                                                                                                                                                                                                                                                                                                                    |
| O(nˣ)                                | POLYNOMIAL     | O(n²), O(n³), ..., O(nⁿ⁺¹) Notice how polynomial time dwarfs the others? Polynomial time is a polynomial function of the input. A polynomial function looks like n2 or n3 and so on. If one loop through a list is O(n), 2 loops must be O(n2). For each loop, we go over the list once. For each item in that list, we go over the entire list once. Resulting in n2 operations. |
| O(2ⁿ)                                | EXPONENTIAL    | Exponential time is 2n, where 2 depends on the permutations involved.                                                                                                                                                                                                                                                                                                             |
| O(n!)                                | FACTORIAL      | This time complexity is often used as a joke, referring to Bogo Sort. I have yet to find a real-life (not-a-joke) algorithm that runs in O(n!) that isn’t an algorithm calculating O(6!) or the likes.                                                                                                                                                                            |



## DATASTRUCTURES

arrays
linked lists
stacks
queues
hash tables
trees
graphs

