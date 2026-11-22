
import sys
from pathlib import Path 
# importing the shared core classes
application_folder = Path(__file__).resolve().parent.parent / "03_Application"
sys.path.insert(0, str(application_folder))

#Testing revision generator
from core.subject import Subject
from core.topic import Topic
from core.revision_scheduler import generate_schedule

subject1 = Subject("Mathematics", "15/12/2026")
topic1 = Topic("Algebra", 4, 2)
topic2 = Topic("Matrices", 5, 1)
topic3 = Topic("Vectors", 2, 4)
subject1.add_topic(topic1)
subject1.add_topic(topic2)
subject1.add_topic(topic3)
subjects = [subject1]

sessions = generate_schedule(subjects, 3)
print("Sessions generated:", len(sessions))

for session in sessions:
    print(session.subject.name, session.topic.name, session.date)
    print("Empty subjects:", len(generate_schedule([], 3)))
    print("Zero days:", len(generate_schedule(subjects, 0)))