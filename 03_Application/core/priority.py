# Calculating which topics the user should revise first
# Priority = (6-Confidence) + Difficulty + Exam urgency

def calc_priority(subject, topic):
    confidence = topic.confidence
    difficulty = topic.difficulty
    exam = subject.exam_urgency()

    if exam is None:
        return None
    priority = (6 - confidence) + difficulty + exam
    return priority

