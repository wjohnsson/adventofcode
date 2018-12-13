from datetime import datetime


class Event:
    def __init__(self, datetime_object, note):
        self.datetime_object = datetime_object
        self.note = note


class Guard:
    def __init__(self, guard_id):
        self.time_slept = 0
        self.guard_id = guard_id
        self.minutes_asleep_list = []

    def mark_period_asleep(self, asleep_time, wakeup_time):
        for i in range(asleep_time.minute, wakeup_time.minute):
            self.minutes_asleep_list.append(i)

    def sleepiest_minute(self):
        return max(set(self.minutes_asleep_list),
                   key=self.minutes_asleep_list.count)

    def __str__(self):
        return "Guard #" + str(self.guard_id) + ", time slept: " + \
            str(self.time_slept)


def most_slept(guards):
    """Returns the guard that slept the most in a list of guards."""
    sleepiest_guard = guards[0]
    for guard in guards[1:]:
        if sleepiest_guard.time_slept < guard.time_slept:
            sleepiest_guard = guard

    return sleepiest_guard


def parse_scribble(scribble):
    """Parses a scribble and returns an event."""
    date_string = scribble.split("]")[0].replace("[", "")
    datetime_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M")

    note = scribble.split("]")[1].lstrip()

    return Event(datetime_object, note)


def get_guard_id(event):
    return int(event.note.split("#")[1].split(" ")[0])


def main():
    with open("scribbles.txt") as f:

        lines = sorted(f.readlines())

        event = parse_scribble(lines[0])
        current_guard_id = get_guard_id(event)
        guards = {
            current_guard_id: Guard(current_guard_id)
        }

        time_slept_known = False
        wakeup_time = None
        asleep_time = None

        for line in lines[1:]:
            event = parse_scribble(line)

            # When we know both wakeup time and when the guard fell asleep, we
            # know time slept.
            if time_slept_known:
                if current_guard_id not in guards.keys():
                    guards[current_guard_id] = Guard(current_guard_id)

                time_slept = wakeup_time - asleep_time
                guards[current_guard_id].time_slept += \
                    int(time_slept.total_seconds()) // 60
                guards[current_guard_id].mark_period_asleep(asleep_time,
                                                            wakeup_time)

                time_slept_known = False

            # Parse the note written after the time.
            if "Guard #" in event.note:
                current_guard_id = get_guard_id(event)
            elif "falls asleep" in event.note:
                asleep_time = event.datetime_object
            elif "wakes up" in event.note:
                wakeup_time = event.datetime_object
                time_slept_known = True

        for g_id, g in guards.items():
            print(str(g_id) + " " + str(g))

        sleepiest_guard = most_slept(list(guards.values()))
        print("Sleepiest guard: " + str(sleepiest_guard))
        print("His sleepiest minute: " +
              str(sleepiest_guard.sleepiest_minute()))

        print("Guard most frequently asleep on the same minute: ...")

        f.close()


main()
