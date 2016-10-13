""" Unit tests for stomp.py 


this assumes you execute this program in the local directory 
and that there is a subdirectory called "test_files" with
a valid STOMP file (must be called "input")


"""
import os
import unittest
from stomp import *

STOMP_FILE = os.path.join("test_files", "input")
if not os.path.exists(STOMP_FILE):
    msg = " ".join(
        ["Could not run the unit tests; file '{0}' missing",
        "- are you sure you are in the right directory?"])
    raise Exception(msg.format(STOMP_FILE))


class TestExampleUnitTest(unittest.TestCase):
    def test_nothing(self):
        self.assertTrue(True)

@unittest.skip
class TestCleanLines(unittest.TestCase):
    """ tests clean_lines """
    def test_no_pounds(self):
        msg = """ better be no "#" as first characters """
        self.assertTrue(
            all([item[0] != "#" for item in clean_lines(
              STOMP_FILE)]), msg)

    def test_no_empty(self):
        msg = """ better not be empty lines """
        self.assertTrue(
            all([item.strip() !="" for item in clean_lines(STOMP_FILE)])
             , msg)

def get_number_of_cards():
    """ helper function to read the number of cards in
    the input file.  I should do this by hand, but I'm lazy
    
    Note this is not one of the unittests.
    """
    N_cards = 0
    with open(STOMP_FILE, 'r') as f:
        for line in f.readlines():
            try:
                if "~" in line[0]:
                    N_cards+=1
            except Exception:
                pass
    return N_cards

@unittest.skip
class TestGetCardsFromFile(unittest.TestCase):
    """ test get_cards_from_file """
    def test_all_cards_read(self):
        msg = "Did we get all the cards in the file?"
        cards = [item for item in get_cards_from_file(STOMP_FILE)]
        self.assertEqual(len(cards), get_number_of_cards(), msg)

@unittest.skip
class TestInputFile(unittest.TestCase):
    """ test InputFile """
    def test_init(self):
        msg = "init method should get all the cards from the input file """
        stmp = InputFile(STOMP_FILE)
        self.assertEqual(len(stmp.cards), get_number_of_cards(),
                msg)

@unittest.skip
class TestCardAPI(unittest.TestCase):
    """ test that the Card class has the appropriate API """

    def test_init(self):
        self.assertIsInstance(
                Card("hello world"),
                Card)

    def test_name_property(self):
        """ there should be a name property """
        name = "hello world"
        c = Card(name)
        self.assertEqual(c.name, name, msg)

    def test_init_name_with_tilde(self):
        msg = "the ~ character should be stripped during init"
        name = "~hello world"
        c = Card(name)
        self.assertEqual(c.name, name[1:], msg)
        
        
if __name__=="__main__":
    unittest.main()
