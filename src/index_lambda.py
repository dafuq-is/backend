#!/usr/bin/env python3

import random
import os

from sources.Exceptions import NoResultException, SourceNotFound
from fetcher import fetchFirstMeaning

from sources import Factory


def lambda_handler(event, context):
    stuff = get_meaning(event["word"])
    if (stuff is False):
        return "Oops! No sources could find meaning of <b>" + event["word"] + "</b>"
    
    return stuff["meaning"] + "<br><br> As described by: <b>" + stuff["source"] + "</b>"


def get_meaning(word):
    _prioritizedSources = Factory.getAllSources()
  
    try:
        meaning = fetchFirstMeaning(_prioritizedSources, word)
    except NoResultException:
        return False

    return meaning
