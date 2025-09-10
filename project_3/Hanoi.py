import timeit
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  if n == 0:
    # The base case : it's trivial to move a single disk from the source to the destination
    d.push(s.pop())
  else:
    # Move the n-1 disks to the auxillary peg using the destination peg as the auxillary. (getting them out of the way for the
    # last disk to move to the destination peg)
    Hanoi_rec(n-1, s, d, a)

    # The disk left over (the one at the bottom after removing n-1 disks) now needs to be moved to the destination peg
    d.push(s.pop())

    # Now move these same n-1 disks to the destination peg using the auxillary as the source (where the disks are now) and the
    # source peg (which is empty now) as the auxillary
    Hanoi_rec(n-1, a, s, d)

  print(n, s, a, d)
  print()

# A writeup was mentioned for the timing of this, so I decided to run this with multiple different n values and noted the runtime of each,
# plotting them on a graph. After plotting each n on the graph up to 20 n's, the trend that the runtime roughly doubled after each n was evident.
# This means that this function has a runtime of roughly O(2^n)

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=3
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")
