#!/usr/bin/env python3
"""Dash Callbacks for the Graph viewer app."""

from graphtest.nodes import update_element_from_list

import dash
from dash import Input, Output, State


def _get_property(id: int, data: list):
    """
    Return the Node Property of index id from data.

    @param data: The selectedNodeData from a Cytoscape object
    @param id: the property Id from the node custom data
    @return any The custom data for this property, or ""
    """
    if data and len(data) >= 1:
        return data[0]["properties"][id - 1]
    else:
        return ""


@dash.callback(
    Output("property-1-input", "value"), Input("graph-canvas", "selectedNodeData")
)
def update_prop1(clickData):
    """Update "Property 1" value."""
    return _get_property(1, clickData)


@dash.callback(
    Output("property-2-input", "value"), Input("graph-canvas", "selectedNodeData")
)
def update_prop2(clickData):
    """Update "Property 2" value."""
    return _get_property(2, clickData)


@dash.callback(
    Output("property-3-input", "value"), Input("graph-canvas", "selectedNodeData")
)
def update_prop3(clickData):
    """Update "Property 3" value."""
    return _get_property(3, clickData)


@dash.callback(
    Output("selected-node-input", "value"), Input("graph-canvas", "selectedNodeData")
)
def update_selected_node(clickData):
    """Update "Selected Node" value."""
    if clickData:
        return clickData[0]["label"]
    else:
        return ""


@dash.callback(
    Output("update-button", "disabled"), Input("graph-canvas", "selectedNodeData")
)
def enable_button(clickData):
    """
    Enable "Update Button" only if a node is selected.

    @note: the logic is reversed because we control the "disabled" property.
    @return bool: True if button should be disabled, False otherwise
    """
    # None is returned on app start-up. When deselected, an empty list is returned
    return clickData is None or len(clickData) == 0


@dash.callback(
    Output("graph-canvas", "elements"),
    Input("update-button", "n_clicks"),
    State("selected-node-input", "value"),
    State("property-1-input", "value"),
    State("property-2-input", "value"),
    State("property-3-input", "value"),
    State("graph-canvas", "selectedNodeData"),
    State("graph-canvas", "elements"),
)
def update_node_data(clicks, selected, prop1, prop2, prop3, node, el):
    """
    Update the selected node in the graph.

    This implements the Handler for Update button.
    @return list: a copy of the elements, where the selected element is updated by the input field values.
    """
    # None is returned on app start-up. When deselected, an empty list is returned
    if node is None or len(node) == 0:
        return el

    updated_node = {
        "data": {
            "id": node[0]["id"],
            "label": selected,
            "properties": [prop1, prop2, prop3],
        }
    }

    return update_element_from_list(el, updated_node)
