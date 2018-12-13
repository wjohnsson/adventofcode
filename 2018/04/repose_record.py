from datetime import datetime


class Event:
    def __init__(self, datetime_object):
        self.datetime_object = datetime_object

    def __str__(self):
        return str(self.datetime_object)


class Guard:
    def __init__(self, guard_id):
        self.time_slept = 0
        self.guard_id = guard_id


def most_slept(guards):
    """Returns the guard that slept the most in a list of guards."""

    # TODO: Implement method
    return guards[0]


def parse_scribble(scribble):
    """Parses a scribble and returns an event."""
    date_string = scribble.split("]")[0].replace("[", "")
    datetime_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
    return Event(datetime_object)


def part_one():
    with open("scribbles.txt") as f:
        s = "[1518-03-09 00:02] Guard #1123 begins shift"

        lines = sorted(f.readlines())

        f.close()


part_one()
