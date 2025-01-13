from collections import namedtuple


Graph = namedtuple(
    "Graph",
    (
        "positions",
        "edges",
        "nodes",
        "centers",
        "others",
        "total_charge",
        "num_unpaired_electrons",
        "edges_lr",
        "idx_i_lr",
        "idx_j_lr",
        "cell",
        "node_mask",
        "batch_segments",
        "graph_mask"
    )
)
