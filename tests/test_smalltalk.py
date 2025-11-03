# Unit tests for smallTalk function in Conversations module

from src.conversations.smalltalk import smallTalk, questions, comments

def test_smallTalk_returns_string():
    actualQuestion = smallTalk(True)
    actualComment = smallTalk(False)
    
    assert isinstance(actualQuestion, str), f"Expected smallTalk(True) to return a string. It instead returned {actualQuestion}"
    assert isinstance(actualComment, str), f"Expected smallTalk(False) to return a string. It instead returned {actualComment}"

def test_questions(): 
    actual = smallTalk(True)
    assert actual in questions, f"Expected a question from the questions list, got {actual}"

def test_comments(): 
    actual = smallTalk(False)
    assert actual in comments, f"Expected a question from the questions list, got {actual}"

def test_smallTalk_randomness_questions(): 
    chosen = set(smallTalk(True) for i in range(50))
    assert len(chosen) > 1

def test_smallTalk_randomness_comments(): 
    chosen = set(smallTalk(False) for i in range(50))
    assert len(chosen) > 1