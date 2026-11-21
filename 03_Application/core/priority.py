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

#collects topics and ranks them 
def rank_topics(subjects):
    priority_topics = []
    for subject in subjects:
        for topic in subject.topics:
            priority = calc_priority(subject, topic)
            if priority is not None:
                priority_topics.append((subject, topic, priority))
    priority_topics.sort(key=lambda item: item[2], reverse=True)
    return priority_topics
