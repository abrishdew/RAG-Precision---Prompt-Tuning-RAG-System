import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration,RagSequenceForGeneration



class TestCases(unittest.TestCase):
    def test_unit_test(Self):
       if __name__ == '__main__':
           unittest.main()
       try:
           tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
           print(tokenizer)
       except NameError as e:
           print(f"Error: {e}")
