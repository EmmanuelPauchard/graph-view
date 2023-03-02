#!/usr/bin/env python3
"""Factory Graph Viewer."""
import dash_cytoscape as cyto


def GraphView(elements: dict, id="graph-canvas") -> cyto.Cytoscape:
    """
    Create a Graph viewer.

    @param id: The HTML id of the graph element
    @param elements: initial elements of the Graph
    @return graph Element
    """
    return cyto.Cytoscape(
        id=id,
        layout={"name": "cose"},
        elements=elements,
        responsive=True,
    )
