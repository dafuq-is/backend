from sources import Factory
from sources.Exceptions import SourceNotFound, NoResultException
#import pdb; pdb.set_trace()

def fetchMeanings(sourceList, term):
    meaning = {}

    for source in sourceList:
        try:
            meaning[source] = Factory.getSource(source).getMeaning(term)
        except NoResultException:
            pass # silent it

    return meaning


def fetchFirstMeaning(prioritySourceList, term):
    for source in prioritySourceList:
        try:
            return Factory.getSource(source).getMeaning(term)
        except NoResultException:
            pass #continue execution if result not found
            # Die if any other unexpected error occurs
    
    raise NoResultException("None of sources provided has the meaning for your term")