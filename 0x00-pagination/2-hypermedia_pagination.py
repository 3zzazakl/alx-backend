#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import csv
import math
from typing import List


class Server:
    """summary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    DATA_FILE = 'Popular_Baby_Names.csv'

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """summary_line
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """summary_line
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        assert (isinstance(page, int) and isinstance(
            page_size, int) and page > 0 and page_size > 0)
        range = index_range(page, page_size)
        self.dataset()
        return self.__dataset[range[0]:range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """summary_line
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        data = self.get_page(page, page_size)
        total = math.ceil(len(self.dataset()) / page_size)
        next = page + 1 if page < total else None
        prev = page - 1 if page > 1 else None
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next,
            'prev_page': prev,
            'total_pages': total
        }


def index_range(page, page_size):
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
