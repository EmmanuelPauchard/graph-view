#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides utility functions to handle nodes."""
from itertools import filterfalse


def update_element_from_list(input_list: list, e: dict) -> list:
    """
    Update element e from list l.

    @note: Key to identify the element is e["data"]["id"]

    @raises ValueError if e has invalid format

    @param l: the list of element
    @param e: the updated node value
    @return list: a copy of l where e is updated with the given value, or l directly if list is not modified
    """
    # sanity checks
    try:
        id = e["data"]["id"]
    except (KeyError, TypeError):
        raise ValueError("Invalid value: ", e)

    filtered_list = list(
        filterfalse(
            lambda x: "id" in x["data"] and x["data"]["id"] == id,
            input_list,
        )
    )

    if len(filtered_list) == len(input_list):
        # e is not in l: return original list
        return input_list
    else:
        return filtered_list + [e]
