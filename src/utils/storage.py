"""Data storage utilities"""
import json

def save_to_json(data, filename):
    """Save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_from_json(filename):
    """Load data from JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
Update 0 on 2014-03-05 01:30:56
Update 2 on 2014-03-05 21:35:53
Update 4 on 2014-03-05 04:31:33
Update 10 on 2014-03-07 04:52:56
