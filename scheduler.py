import datetime

def schedule_interview(name,email,date):

    return f"""
Interview Scheduled

Candidate: {name}
Date: {date}

A meeting invitation will be sent to {email}.
"""