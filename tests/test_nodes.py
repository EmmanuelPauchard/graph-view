#!/usr/bin/env python3
from nodes import update_element_from_list

import pytest


initial_nodes = [
    {
        "data": {"id": "one", "label": "1", "properties": [1, 2, 3]},
    },
    {
        "data": {"id": "two", "label": "2", "properties": [0, 0, 0]},
    },
    {
        "data": {"id": "three", "label": "3", "properties": [3, 3, 3]},
    },
]
updated_nodes = [
    (
        updated_node := {
            "data": {"id": "three", "label": "", "properties": ["", "", ""]},
        },
        "Empty data",
        [
            {
                "data": {"id": "one", "label": "1", "properties": [1, 2, 3]},
            },
            {
                "data": {"id": "two", "label": "2", "properties": [0, 0, 0]},
            },
            updated_node,
        ],
    ),
    (
        {
            "data": {"id": "Foo", "label": "", "properties": ["", "", ""]},
        },
        "Unknown Id",
        initial_nodes,
    ),
]


@pytest.mark.parametrize(
    "initial_list, updated_node, validation_list",
    [(initial_nodes, val[0], val[2]) for val in updated_nodes],
    ids=[val[1] for val in updated_nodes],
)
def test_update_nodes(initial_list, updated_node, validation_list):
    assert update_element_from_list(initial_list, updated_node) == validation_list


def test_empty_list():
    assert update_element_from_list([], initial_nodes[0]) == []


@pytest.mark.parametrize("val", ["Hello", 1, {}, {"data": 1}])
def test_invalid_type(val):
    with pytest.raises(ValueError):
        update_element_from_list(initial_nodes, val)
