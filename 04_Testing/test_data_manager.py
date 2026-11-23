import sys
from pathlib import Path 
# importing the shared core classes
application_folder = Path(__file__).resolve().parent.parent / "03_Application"
sys.path.insert(0, str(application_folder))

from core.subject import Subject
from core.topic import Topic
from core.data_manager import save_data, load_data


subject1 = Subject("Mathematics", "15/12/2026")
topic1 = Topic("Algebra", 4, 2)
subject1.add_topic(topic1)
topic2 = Topic("Calculus", 3, 4)
subject1.add_topic(topic2)
subjects = [subject1]

save_data(subjects)
print("Data saved successfully")

print("\nTesting CSV loading:")
load_data()

loaded_subjects = load_data()

for subject in loaded_subjects:
    print(subject.name, subject.exam_date)

    for topic in subject.topics:
        print(topic.name, topic.difficulty, topic.confidence)