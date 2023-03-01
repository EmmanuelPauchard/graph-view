#!/usr/bin/env python3
"""
Dash Demonstration Project.

Create a graph and some fields to update the nodes.
"""

from dash import Dash, html, dcc, Input, Output, State
import dash_cytoscape as cyto
from itertools import filterfalse

from default_nodes import default_elements


app = Dash(__name__)


def _text_to_id(text: str) -> str:
    """Quick way to generate a deterministic id from text."""
    return text.lower().replace(" ", "-")


def _labelled_input(text: str) -> html.Div:
    """
    Return a Div made of a label and an input field.

    @note: Id of HTML elements is the text transformed by text_to_id
    @param: text: the label text
    @return: html.Div, column layout
    """
    return html.Div(
        [
            html.Label(text, id=_text_to_id(text) + "-label"),
            dcc.Input(
                type="text",
                value="",
                id=_text_to_id(text) + "-input",
                style={"marginTop": "1em"},
            ),
        ],
        style={"display": "flex", "flexDirection": "column"},
    )


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


app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="graph-canvas",
            layout={"name": "cose"},
            style={"width": 500, "height": 500, "border": "solid black"},
            elements=default_elements,
        ),
        html.Div(
            [
                _labelled_input(i)
                for i in ["Selected Node", "Property 1", "Property 2", "Property 3"]
            ]
            + [html.Button("Update", id="update-button", n_clicks=0)],
            style={
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "space-between",
            },
        ),
    ],
    style={
        "display": "flex",
        "justifyContent": "space-evenly",
        "border": "solid black",
        "padding": "2em",
    },
)


@app.callback(
    Output("property-1-input", "value"), Input("graph-canvas", "selectedNodeData")
)
def update_prop1(clickData):
    """Update "Property 1" value."""
    return _get_property(1, clickData)


@app.callback(
    Output("property-2-input", "value"), Input("graph-canvas", "selectedNodeData")
)
def update_prop2(clickData):
    """Update "Property 2" value."""
    return _get_property(2, clickData)


@app.callback(
    Output("property-3-input", "value"), Input("graph-canvas", "selectedNodeData")
)
def update_prop3(clickData):
    """Update "Property 3" value."""
    return _get_property(3, clickData)


@app.callback(
    Output("selected-node-input", "value"), Input("graph-canvas", "selectedNodeData")
)
def update_selected_node(clickData):
    """Update "Selected Node" value."""
    if clickData:
        return clickData[0]["label"]
    else:
        return ""


@app.callback(
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


@app.callback(
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

    return list(
        filterfalse(
            lambda x: "id" in x["data"] and x["data"]["id"] == node[0]["id"], el
        )
    ) + [updated_node]


if __name__ == "__main__":
    app.run_server(debug=True)
