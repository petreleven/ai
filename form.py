from collections import defaultdict
class Attendee:
    def __init__(self,emailsent, eventid):
        self.emailsent=emailsent
        self.eventid=eventid


attendee1 = Attendee(False,1)
attendee2 = Attendee(False,2)
attendee3 = Attendee(True,1)
allattendees = [attendee1, attendee2, attendee3]

filtered_attendees = defaultdict(list)
for att in allattendees:
    if att.emailsent == False:
        filtered_attendees[att.eventid].append(att)
