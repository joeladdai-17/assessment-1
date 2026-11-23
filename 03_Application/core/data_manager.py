import csv
from pathlib import Path

from core.subject import Subject
from core.topic import Topic

# fixed CSV file for both text and gui versions
DATA_FILE = Path(__file__).resolve().parent.parent / "revision_data.csv"

#saving data
def save_data(subjects):
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Exam Date", "Topic", "Difficulty", "Confidence"])

        for subject in subjects:
            #if a subject is being saved which consists of no topics
            if len(subject.topics) == 0:
                writer.writerow([subject.name, subject.exam_date, "", "", ""])
            for topic in subject.topics:
                writer.writerow([subject.name, subject.exam_date,
                                 topic.name,
                                 topic.difficulty,
                                 topic.confidence])

#loading saved subjects and topics
def load_data():
    subjects = []

    if not DATA_FILE.exists():
        return subjects

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            subject_name = row[0]
            exam_date = row[1]
            topic_name = row[2]
            difficulty = row[3]
            confidence = row[4]

#if an existing subject is already there
            existing_subject = None
            for subject in subjects:
                if subject.name == subject.name:
                    existing_subject = subject
                    break

            if existing_subject is None:
                existing_subject = Subject(subject_name, exam_date)
                subjects.append(existing_subject)

            if topic_name != "":
                topic = Topic(topic_name, int(difficulty), int(confidence))
                existing_subject.add_topic(topic)
                
    return subjects