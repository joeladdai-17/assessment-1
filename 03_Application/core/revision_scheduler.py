from datetime import date, timedelta
#from core.priority import calc_priority
from core.priority import rank_topics
from core.revision_session import RevisionSession

def generate_schedule(subjects, number_of_days):
    sessions = []
    priority_topics = rank_topics(subjects)
    if len(priority_topics) == 0:
        return sessions
    if number_of_days <= 0:
        return sessions
    topics_per_day = len(priority_topics) // number_of_days
    extra_topics = len(priority_topics) % number_of_days
    start_date = date.today()

    topic_index = 0
    #distributing the topics across requested days
    for day in range(number_of_days):
        session_date = start_date + timedelta(days=day)
        session_date =session_date.strftime("%d/%m/%Y")
        daily_topics = topics_per_day
        
        if day < extra_topics:
            daily_topics += 1
        
        for i in range(daily_topics):
            selected = priority_topics[topic_index]
            subject = selected[0]
            topic = selected[1]
            session = RevisionSession(subject, topic, session_date, 45)
            sessions.append(session)
            topic_index += 1
    return sessions



    