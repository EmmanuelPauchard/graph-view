#!/usr/bin/env python3
"""
Dash Demonstration Project.

Create a graph and some fields to update the nodes.
"""

from graphtest.default_nodes import default_elements
from graphtest.graph_viewer import GraphView
from graphtest.inputs import Menu

# Import the callbacks module so that the callbacks themselves be registered
import graphtest.callbacks

from dash import Dash, html


class App:
    """The Main Application."""

    def __init__(
        self,
        elements: dict = default_elements,
        port: int = 8050,
        hostname: str = "localhost",
    ):
        """
        Create the application.

        @param elements: Elements to populate the graph.
        @param port: Port the server should bind to
        @param hostname: Hostname the server should bind to
        """
        self.app = Dash(__name__, title="Graph Visualisation App")
        self.hostname = hostname
        self.port = port

        self.app.layout = html.Div(
            [
                GraphView(elements),
                html.Div(
                    Menu(
                        input_text=[
                            "Selected Node",
                            "Property 1",
                            "Property 2",
                            "Property 3",
                        ],
                        button_text="Update",
                    ),
                    className="form-menu",
                ),
            ],
            className="main-container",
        )

    def run(self, debug=False):
        """
        Run the server.

        @param debug: If true, Start server in debug mode
        """
        self.app.run(debug=debug)

    def get_server(self):
        return self.app.server
