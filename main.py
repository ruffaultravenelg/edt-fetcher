import json
import sys
import requests
from icalendar import Calendar
from datetime import datetime

# Path to the JSON file containing class links
LINKS = "links.json"

# Path to the JSON result file
OUTPUT = "data.json"

def parse_ics_to_json(ics_content):
    """
    Parses the ICS content and converts it into a list of dictionaries in JSON format.
    """
    events = []
    calendar = Calendar.from_ical(ics_content)
    
    for component in calendar.walk():
        if component.name == "VEVENT":
            # Normalize dates to remove timezone information
            dtstart = component.get("DTSTART").dt
            dtend = component.get("DTEND").dt
            
            if hasattr(dtstart, 'tzinfo') and dtstart.tzinfo:
                dtstart = dtstart.replace(tzinfo=None)
            if hasattr(dtend, 'tzinfo') and dtend.tzinfo:
                dtend = dtend.replace(tzinfo=None)
            
            # Build the event dictionary
            event = {
                "guid": component.get("UID").split("-")[-1] if component.get("UID") else None,
                "title": component.get("SUMMARY"),
                "date": dtstart.strftime('%d/%m/%Y'),
                "start_time": dtstart.strftime('%H:%M'),
                "end_time": dtend.strftime('%H:%M'),
                "group": component.get("DESCRIPTION").split("\n")[2].strip() if component.get("DESCRIPTION") else None,
                "professor": component.get("DESCRIPTION").split("\n")[1].strip() if component.get("DESCRIPTION") else None,
                "room": component.get("LOCATION"),
                "type": None  # Type of event (e.g., TDm, TD, TP, CM)
            }

            # Determine the event type (e.g., TDm, TD, TP, CM)
            event_types = ["TDm", "TD", "TP", "CM"]
            for event_type in event_types:
                if f" - {event_type} - " in event["title"]:
                    event["title"] = event["title"].replace(f" - {event_type} - ", " - ")
                    event["type"] = event_type
                    break

            events.append(event)
    return events


def fetch_schedule(classe, links_file):
    """
    Fetches the schedule for the specified class and converts it to JSON.
    """
    # Load class links from the JSON file
    with open(links_file, 'r', encoding='utf-8') as file:
        links_data = json.load(file)
    
    # Find the URL corresponding to the class
    url = None
    for element in links_data:
        if element["classe"] == classe:
            url = element["url"]
            break
    
    if not url:
        raise ValueError(f"TP group '{classe}' not found in the file {links_file}.")
    
    # Download the ICS file
    response = requests.get(url)
    response.raise_for_status()
    ics_content = response.content.decode('utf-8', errors='replace')  # Decode as UTF-8
    
    # Parse the ICS content into JSON
    data = parse_ics_to_json(ics_content)
    
    # Save the data to a JSON file
    output_file = OUTPUT
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    
    print(f"Schedule saved in {output_file}")


if __name__ == "__main__":
    # Check if the class name argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <tp_group>")
        sys.exit(1)

    classe = sys.argv[1]
    links_file = LINKS
    
    try:
        # Fetch and process the schedule
        fetch_schedule(classe, links_file)
    except Exception as e:
        print(f"Error: {e}")

