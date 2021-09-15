# lexicographic-permutations
Prints all permutations of n integers in lexicographic order


An algorithm for generating the permutations of {1, 2, . . . , n } can be based on a proce-
dure that constructs the next permutation in lexicographic order following a given permutation
a1a2 · · · an. We will show how this can be done. First, suppose that an−1 < a n. Interchange an−1
and an to obtain a larger permutation. No other permutation is both larger than the original per-
mutation and smaller than the permutation obtained by interchanging an−1 and an. For instance,
the next larger permutation after 234156 is 234165. On the other hand, if an−1 > a n, then a
larger permutation cannot be obtained by interchanging these last two terms in the permutation.
Look at the last three integers in the permutation. If an−2 < a n−1, then the last three integers in
the permutation can be rearranged to obtain the next largest permutation. Put the smaller of the
two integers an−1 and an that is greater than an−2 in position n − 2. Then, place the remaining
integer and an−2 into the last two positions in increasing order. For instance, the next larger
permutation after 234165 is 234516.
On the other hand, if an−2 > a n−1 (and an−1 > a n), then a larger permutation cannot be
obtained by permuting the last three terms in the permutation. Based on these observations, ageneral method can be described for producing the next larger permutation in increasing order
following a given permutation a1a2 · · · an. First, find the integers aj and aj +1 with aj < a j +1
and
aj +1 > a j +2 > · · ·  > a n,
that is, the last pair of adjacent integers in the permutation where the first integer in the pair is
smaller than the second. Then, the next larger permutation in lexicographic order is obtained
by putting in the j th position the least integer among aj +1, a j +2, . . . ,  and an that is greater
than aj and listing in increasing order the rest of the integers aj , a j +1, . . . , a n in positions j + 1
to n. It is easy to see that there is no other permutation larger than the permutation a1a2 · · · an but
smaller than the new permutation produced.  (Kenneth H. Rosen, Discrete Math and its Applications, 7th Edition)
