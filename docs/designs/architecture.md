## Architecture: How to I frame the problem, what do I need to compute and how do I infer the final order.

#### Options

- Sequence reordering: 
    * input all of the cells as a time-series/hierarchical transformer, 
    and learn the correct order of cells.
    * Find the correct preceding cell(s) for each one - use viterby/beam search for inference.

- Matching: Match each comment cell to the following code cell, 
then reorder the preceding comment cells for each code cell

-  
