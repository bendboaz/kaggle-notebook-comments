## Architecture: How to I frame the problem, what do I need to compute and how do I infer the final order.

#### Options

- Sequence reordering:
    * Baseline: NSP on md-cells only, then infer (greedy/Viterby/beam).
    * Cluster md cells to code cells, then order the inner groups.

- Greedy placing: Take all code cells, add markdown cells one by one.

- Explicit position prediction: Put everything through the model, and learn to output 
  the absolute position of each cell in the sequence.
  
- Use existing reordering algorithms:
    * https://aclanthology.org/P19-1174.pdf
    * https://proceedings.neurips.cc/paper/2021/hash/6f46dd176364ccec308c2760189a4605-Abstract.html
    * https://aclanthology.org/W12-5906.pdf
