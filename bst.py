#!/usr/bin/python3.6

# Developed by : Wael Bahloul
# This is a binary search tree with some functions
# to insert, delete, traverse, find ... etc

class Node:
  def __init__(self, key=None):
    self.key = key
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.root = None

  def find0(self, key):
    x =  self.find(self.root, key)
    return x

  # Recusive
  def find(self, root, key):
    if root is None or key == root.key:
      return self.root
    elif key > root.key:
      return self.find(root.right, key)
    else:
      return self.find(root.left, key)

  def findMin0(self):
    FNode = self.findMin(self.root)
    return FNode

  # Recursive
  def findMin(self, root):
    if root.left is None:
      return root
    else:
      return self.findMin(root.left)

  def findMax0(self):
    FNode = self.findMax(self.root)
    return FNode

  # Recursive
  def findMax(self, root):
    if root.right is None:
      return root
    else:
      return self.findMax(root.right)

  def insert(self, data):
    self.root = self.insertInTree(self.root, data)

  def insertInTree(self, root, key):
    if root is None:
       root = Node(key)
       return root
    elif key < root.key:
       root.left = self.insertInTree(root.left, key)
    elif key > root.key:
       root.right = self.insertInTree(root.right, key)
    return root

  def delete0(self, key):
    self.root = self.delete(self.root, key)

  def delete(self, root, key):
    if root is None:
      return root

    if key < root.key:
      root.left = self.delete(root.left, key)

    elif key > root.key:
      root.right = self.delete(root.right, key)

    else:
      if root.left is None:
        return root.right

      elif root.right is None:
        return root.left

      root.key = self.MinValue(root.right)
      root.right = self.delete(root.right, root.key)

    return root


  def MinValue(self, root):
    minv = root.key
    while root.left is not None:
      minv = root.left.key
      root = root.left
    return minv

  def traverseInOrder0(self):
    self.traverseInOrder(self.root)

  def traverseInOrder(self, root):
    if root is not None:
      self.traverseInOrder(root.left)
      self.visit(root)
      self.traverseInOrder(root.right)

  def visit(self, node):
    print (node.key)

  def getRoot(self):
    return self.root

  def averageTree0(self):
    numofnodes = self.averageTree(self.root)
    average = self.sumNodes0() / numofnodes
    return average

  def averageTree(self, root):
    if root.left and root.right:
       return 1 + self.averageTree(root.left) + self.averageTree(root.right)
    elif root.left:
      return 1 + self.averageTree(root.left)
    elif root.right:
      return 1 + self.averageTree(root.right)
    else:
      return 1

  def sumNodes0(self):
    size = self.sumNodes(self.root)
    return size

  def sumNodes(self, root):
    if root is None:
      return 0
    return root.key + self.sumNodes(root.left) + self.sumNodes(root.right)


def main():

  print ("\n Inserting the following Numbers\n")
  print ("50, 30, 20, 40, 70, 60, 80")

  NewTree = BST()
  NewTree.insert(50)
  NewTree.insert(30)
  NewTree.insert(20)
  NewTree.insert(40)
  NewTree.insert(70)
  NewTree.insert(60)
  NewTree.insert(80)

  print ("Find the Min Value")
  min = NewTree.findMin0()
  print (min.key, "\n")

  print ("Find the Max Value")
  max = NewTree.findMax0()
  print (max.key, "\n")

  print ("Inorder traversal of the given tree")
  NewTree.traverseInOrder0()

  print ("\nDelete 20")
  NewTree.delete0(20)
  print ("Inorder traversal of the modified tree")
  NewTree.traverseInOrder0()

  print ("\nDelete 30")
  NewTree.delete0(30)
  print ("Inorder traversal of the modified tree")
  NewTree.traverseInOrder0()

  print ("\nDelete 50")
  NewTree.delete0(50)
  print ("Inorder traversal of the modified tree")
  NewTree.traverseInOrder0()

  print ("\n The sum is")
  sum = NewTree.sumNodes0()
  print (sum)

  print ("\nget the new root")
  gt = NewTree.getRoot()
  print (gt.key)

  print ("\n The sum of nodes is")
  sum = NewTree.averageTree0()
  print (sum)


  print ("\nThis is Task 1-C")
  print ("\n Inserting the Following Values")
  print ("\n 90, 21, 38, 50, 40, 45, 87")

  SecondTree = BST()
  SecondTree.insert(90)
  SecondTree.insert(21)
  SecondTree.insert(38)
  SecondTree.insert(50)
  SecondTree.insert(40)
  SecondTree.insert(45)
  SecondTree.insert(87)

  print ("\n All Values Inserted")

  print ("\n The sum is")
  sum = SecondTree.sumNodes0()
  print (sum)

  print ("\n The average is")
  sum = SecondTree.averageTree0()
  print (sum)

if __name__ == "__main__":
  main()

