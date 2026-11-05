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
            print(topic)

# verifying adding and displaying topics
biology = Subject("Biology", "2027-01-25")
biology.add_topic("Genetics")
biology.add_topic("Evolution")
biology.show_topics()

comp_science = Subject("Computer Science", "2026-11-06")
print(comp_science.exam_date)
comp_science.add_topic("Hexadecimals")
comp_science.show_topics()

        
