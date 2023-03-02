#!/usr/bin/env python3
"""Factory functions to generate App control menu."""
from dash import html, dcc


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
            ),
        ],
        className="labelled-input",
    )


def Inputs(text: list[str]) -> list[html.Div]:
    """
    Generate a list of inputs and lables with given text.

    @note: All HTML Ids are created from the given element's text given to _text_to_id

    @param text: A list of str, for each element a pair (label, input) will be created. The label will be set to the
    element
    @return A list of Div elements, each containing (label, input)
    """
    return [_labelled_input(t) for t in text]


def Menu(input_text: list, button_text: str) -> list[html.Div]:
    """
    Generate the whole menu, made of labels, input fields, and a button.

    @note: All HTML Ids are created from the given element's text given to _text_to_id

    This is equivalent to a form.
    @param input_text: Text to populate the Inputs
    @param button_text: Text to display on the button
    @return: a list of HTML elements
    """
    return Inputs(input_text) + [
        html.Button(
            button_text,
            id=f"{_text_to_id(button_text)}-button",
            n_clicks=0,
        ),
    ]
