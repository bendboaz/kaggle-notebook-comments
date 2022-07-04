## Architecture: How to I frame the problem, what do I need to compute and how do I infer the final order.

#### Options

- Sequence reordering: 
    * input the cells as a time-series/hierarchical transformer, 
    and learn the correct order of cells.
    * Find the correct preceding cell(s) for each one - use Viterby/beam search for inference.
      Find some way to leverage BERT's NSP objective.

- Matching: Match each comment cell to the following code cell, 
then reorder the preceding comment cells for each code cell

- Merging: First order the comment cells separately, then attempt to merge the two sequences.
