import unittest
import word_ladder

class TestWordLadder(unittest.TestCase):

        def test_load_file(self):
            self.assertTrue(word_ladder.load_file("dictionary.txt"))



        # tests the start word checker function
        def test_start_word_checker(self):
            self.assertEqual(word_ladder.start_word_checker("hide"), "hide")
            self.assertEqual(word_ladder.start_word_checker("lead"), "lead")

        # tests the target word checker function
        def test_target_word_checker(self):
            self.assertEqual(word_ladder.target_word_checker("seek"), "seek")
            self.assertEqual(word_ladder.target_word_checker("gold"), "gold")

        # tests the excluded words build function
        def test_excluded_words_build(self):
            result = word_ladder.excluded_words_build("deep, heap, beep")
            self.assertTrue(type(result) is list)

        def test_same(self):
            # checks if number of alphabets are same in item and target against the given value. In this case it is 3.
            self.assertTrue(word_ladder.same("fine", "mine") == 3)
            # in this case, "this" and "nice" have no alphabets in common at same place.
            self.assertTrue(word_ladder.same("this", "nice") == 0)
            # Checks the number of common alphabets in item and target against the given value. In this case it is 3.
            self.assertEqual(word_ladder.same("lead", "mead"), 3)

        # checks that list of words matches the pattern provided and word is not already in seen dictionary.
        def test_build(self):
            self.assertFalse(word_ladder.build(".ide", "side, site, sits, sies, sees, seek", {"seek": True}, []) == False)
            self.assertFalse(word_ladder.build(".ead", "load, goad, gold", {"gold": True}, []) == False)


        def test_find(self):
            self.assertTrue(word_ladder.find("dog", "dog, dot, cot, cat", {"dog": True}, "cat", ["dog"]) == False)
            self.assertTrue(word_ladder.find("hide", "hide, side, site, sits, sies, sees, seek", {"hide": True}, "seek", ["hide"]) == False)



if __name__ == '__main__':
    unittest.main()