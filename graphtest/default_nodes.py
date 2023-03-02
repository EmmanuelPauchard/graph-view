#!/usr/bin/env python3
"""
The sample and default set of nodes and edges used by the application
"""

nodes = [
    {
        "data": {"id": short, "label": label, "properties": props},
    }
    for short, label, props in (
        ("one", "1", [1, 2, 3]),
        ("two", "2", [11, 22, 33]),
        ("three", "3", [111, 222, 333]),
    )
]

edges = [
    {"data": {"source": source, "target": target}}
    for source, target in (
        ("one", "two"),
        ("three", "two"),
    )
]

default_elements = nodes + edges
