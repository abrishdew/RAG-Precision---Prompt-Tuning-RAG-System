import unittest
from unittest.mock import patch, MagicMock
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from ragas import evaluate

class TestEvaluation(unittest.TestCase):
    @patch('ragas.evaluate')
    def test_evaluation(self, mock_evaluate):
        # Mock the dataset and the evaluation result
        mock_dataset = MagicMock()
        mock_result = MagicMock()
        mock_result.to_pandas.return_value = "Mocked DataFrame"

        # Set the return value of the evaluate function
        mock_evaluate.return_value = mock_result

        # Call the evaluate function with the mocked dataset
        result = evaluate(
            dataset=mock_dataset,
            metrics=[
                'context_precision',
                'context_recall',
                'faithfulness',
                'answer_relevancy',
            ],
        )

        # Check if the evaluate function was called with the correct parameters
        mock_evaluate.assert_called_once_with(
            dataset=mock_dataset,
            metrics=[
                'context_precision',
                'context_recall',
                'faithfulness',
                'answer_relevancy',
            ],
        )

        # Check if the result is converted to a pandas DataFrame
        self.assertEqual(result.to_pandas(), "Mocked DataFrame")

if __name__ == '__main__':
    unittest.main()