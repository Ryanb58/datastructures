# Binary Search Tree

A BST consist of a root note with two branches, one on the left that is made up of nodes with lesser value, and one on the right that is made up of nodes with greater value. An example of a binary search tree is an Abstract Syntax Tree. These are used a lot with static code analysis tools. BST is also the basis for a lot of other tree like data structures such as red-black and AVL trees.

Here is an example from Wikipedia:

![Image of a BST](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/200px-Binary_search_tree.svg.png)


#### Use Cases:

Search for a specific item in an array.

As a database index(B-Tree).

etc...

#### Supported Operations:
 - Insert
 - Delete
 - Search
 - Pre-Order Traversal (node -> left subtree -> right subtree)
 - In-Order Traversal (left subtree -> node -> right subtree)
 - Post-Order Traversal (left subtree -> right subtree -> node)


#### Computational Complexities:

Average Complexities:
 - Insert - O(log(n))
 - Search - O(log(n))
 - Delete - O(log(n))
 - Any Print/Traversal - O(n)

Worst Complexities:
 - Insert - O(h)
 - Search - O(h)
 - Delete - O(h)
 - Any Print/Traversal - O(n)
 
 Where h is equal to the height of the tree.