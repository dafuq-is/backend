#!/usr/bin/env python3

import random
import os

from sources.Exceptions import NoResultException, SourceNotFound
from fetcher import fetchFirstMeaning

from sources import Factory


def lambda_handler(event, context):
    return get_meaning(event.word)


def get_meaning(word):
    _prioritizedSources = Factory.getAllSources()
  
    try:
        meaning = fetchFirstMeaning(_prioritizedSources, word)
    except NoResultException:
        return false

    return meaning
