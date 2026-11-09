# Importing my Topic class
from .topic import Topic
# Creating a Subject class
class Subject():
# Constructor method
    def __init__(self, name, exam_date):
        self.name = name
        self.exam_date = exam_date
        self.topics = []

# Adding topics
    def add_topic(self, topic):
        self.topics.append(topic)

# Shows users topics
    def show_topics(self):
        for topic in self.topics:
            print(topic.name)

# quick test
if __name__ == "__main__":
    biology = Subject("Biology", "2027-01-25")
    genetics = Topic("Genetics", 4, 2)
    biology.add_topic(genetics)

    biology.show_topics()
