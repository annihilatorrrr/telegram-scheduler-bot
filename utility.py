import ujson


def generate_event_text(event: dict) -> str:
    event_output = "<b>Name</b>: " + event["event_name"] + "\n"
    event_output += "<b>Time</b>: " + event["event_time"] + "\n"
    event_output += "<b>Day</b>: " + event["event_wday"] + "\n"
    event_output += "<b>Location</b>: " + event["event_location"] + "\n"
    event_output += "<b>Additional Information</b>: " + event["event_extra"] + "\n"
    return event_output


def load_data(user_id: int) -> dict:
    with open("users/" + str(user_id) + ".json", "r") as user_file:
        user_data = ujson.load(user_file)
    return user_data


def dump_data(user_data: dict):
    with open("users/" + str(user_data["user_id"]) + ".json", "w") as user_file:
        ujson.dump(user_data, user_file)
