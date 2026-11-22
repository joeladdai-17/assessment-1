import sys
from pathlib import Path 
# importing the shared core classes
application_folder = Path(__file__).resolve().parent.parent / "03_Application"
sys.path.insert(0, str(application_folder))

from core.subject import Subject
from core.topic import Topic
from core.revision_session import RevisionSession

subject = Subject("Mathematics", "10/12/2026")
topic = Topic("Matrices", 4, 2)

maths = RevisionSession(subject, topic, "25/11/2026", 45)
print(maths.subject.name)
print(maths.topic.name)
print(maths.date)
print(maths.duration)