#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""


def index_range(page, page_size):
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
