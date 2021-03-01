import unittest
import sys
sys.path.append("D:/IT/Python/CodeSignal")
from assignments import feedback_review

class TestFeedback(unittest.TestCase):
    def test_feedback(self):
        self.assertEqual(feedback_review.feedbackReview("This is an example feedback",8),["This is", "an", "example","feedback"])
        self.assertEqual(feedback_review.feedbackReview("This is an example feedback",40),["This is an example feedback"])
        self.assertEqual(feedback_review.feedbackReview("",10),[])
        self.assertEqual(feedback_review.feedbackReview("Dude, do you even review these feedbacks?",16),["Dude, do you", "even review", "these feedbacks?"])

if __name__ == "__main__":
    unittest.main()