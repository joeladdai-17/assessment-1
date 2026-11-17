# quick test for the priority calculations
from core.subject import Subject
from core.topic import Topic
from core.priority import calc_priority

# Test 1: A future exam

subject = Subject("Biology", "01/01/2027")
topic = Topic("Evolution", 4, 2)

score = calc_priority(subject, topic)
print(score)

# Test 2: Exam has passed 
subject = Subject("Maths", "01/01/2026")
topic = Topic("Algebra", 4, 2)

score = calc_priority(subject, topic)
print(score)

