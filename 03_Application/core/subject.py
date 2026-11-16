from datetime import datetime, date
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

# Calculating how many days left until an exam
    def days_until_exam(self):
        #Retrieving stored subject exam date and converting the string into an object
        exam = datetime.strptime(self.exam_date, "%d/%m/%Y").date()
        today = date.today()
        # days remaining = exam date - todays date
        difference = exam - today
        return difference.days

# Creating a method to provide an urgency score depending on how close the exam is
    def exam_urgency(self):
        # days remaining until exam
        days = self.days_until_exam()
        # exam has passed if negative
        if days < 0:
            return None
        # if theres 0-3 days left until an exam the urgency score is 5 
        elif 0 <= days <= 3:
            return 5
        # if theres 4-7 days remaining urgency score is 4
        elif 4 <= days <= 7:
            return 4
        # if theres 8-14 days remaining urgency score is 3
        elif 8 <= days <= 14:
            return 3
        # if theres 15-30 days remaining urgency score is 2
        elif 15 <= days <= 30:
            return 2
        # if theres 31 days or more remaining urgency score is 1
        else:
            return 1
        
        
        

if __name__ == "__main__":
    biology = Subject("Biology", "01/01/2027")
    print(biology.days_until_exam())
    print(biology.exam_urgency())



