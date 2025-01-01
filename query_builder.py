import logging
import requests
import os
from dotenv import load_dotenv
import random
import cfg

randorg_key = os.getenv("random_org_key") # API key in the .env file for Random.org
load_dotenv()
def get_random_int(fortype="randint"):
    fortype = fortype.lower()

    if fortype == "randint":
        url = "https://random.org/integers/?num=1&min=1&max=100000&col=1&base=10&format=plain&rnd=new"
    elif fortype == "maxviewcount":
        url = "https://random.org/integers/?num=55000&min=120000&max=&col=1&base=10&format=plain&rnd=new"
    else:
        url = "https://random.org/integers/?num=1&min=1&max=1000&col=1&base=10&format=plain&rnd=new"

    response = requests.get(url)
    if response.status_code == 200:
        random_number = int(response.text)
        return random_number
    else:
        logging.error(f"Error. Response code: {response.status_code} -- Falling back to blank query ")
        return 90000


def get_random_sent():
    """ This function uses Metaphorpsum api to generate random sentences for the search query.  """

    url = "http://metaphorpsum.com/paragraphs/1/1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        logging.error(f"Error. Response code: {response.status_code} -- Falling back to blank query ")
        empty_query = ""
        return empty_query

def get_formed_search():
    """ Just for fun, I asked chatGPT to form a list of search terms it thinks will turn up in a video.
    I also had it provide a list of prefixes for each term. This function takes one prefix and pairs it with one term
    to form a search query."""
    terms = [
        "moment", "event", "occasion", "instance", "episode", "happening", "occurrence", "milestone",
        "turning point", "celebration", "announcement", "horizon", "landmark", "experience",
        "phase", "chapter", "crucial moment", "snapshot", "encounter", "breakthrough", "discovery", "opportunity",
        "trial", "adventure", "journey", "achievement", "transition", "climax", "gathering",
        "meeting", "reunion", "remembrance", "exploration", "arrival", "departure", "conclusion", "unveiling",
        "unfolding", "realization", "storm", "calm", "whirlwind", "transformation",
        "unpredictability", "revolution", "mystery", "serendipity", "reminder", "narrative",
        "retrospective", "vision", "shift", "suspense", "anticipation", "invention",
        "conflict", "resolution", "reconciliation", "conundrum", "descent", "ascent", "twilight", "dawn", "eclipse",
        "solar flare", "momentum", "gathering storm", "outburst",
        "recession", "revival", "resurgence", "accomplishment", "reflection", "separation",
        "success", "failure", "growth", "remorse", "regret", "joy", "loss", "recovery",
        "breakthrough", "momentous occasion", "high point", "culmination", "new beginning", "fresh start", "impasse",
        "transition", "instinct", "beginning", "end", "debut", "release", "purge", "renovation",
        "birth", "death", "explosion", "exploration", "departure", "arrival", "surprise",
        "shock", "disturbance", "calmness", "relief", "negotiation", "argument", "excitement",
        "anticipation", "incident", "tragedy", "comedy", "turnaround", "standoff", "confrontation",
        "flare-up", "rising action", "crisis", "falling action", "end of an era", "adventure",
        "rendezvous", "explosion", "revolution", "triumph", "defeat", "ceremony", "banquet", "exhibition",
        "evolution", "summit", "opening", "close", "invitation", "introduction", "showdown",
        "reality check", "consequence", "time lapse", "appreciation", "adjustment", "pivot", "pivot point",
        "turn", "interruption", "restoration", "paradox", "quandary", "escape", "escape route", "junction",
        "shift", "displacement", "unraveling", "critical moment", "uncertainty", "probability",
        "possibility", "future", "past", "present", "before", "after", "context", "moment of clarity",
        "setup", "repercussion", "reflection", "inception", "outcome",
        "retribution", "sacrifice", "admission", "surrender", "formation", "calibration",
        "contingency", "moment of truth", "confession", "time out", "remedy", "trial", "contest", "sport",
        "tournament", "convention", "clash", "destruction", "change", "anomaly", "echo", "resonance",
        "pattern", "coincidence", "intervention", "pathway", "alignment", "contingency", "pressing moment",
        "collision", "rescue", "cure", "resolution", "elation", "denouement", "recovery",
        "closure", "vindication", "evolution", "outcome", "endgame", "disruption", "integration",
        "synchronization", "pivot", "axis", "intersection", "continuum", "matrix", "tipping point",
        "finale", "reclamation", "confirmation", "break", "recuperation", "moment of decision",
        "affirmation", "assurance", "brink", "standstill", "intermission", "phase shift",
        "adjustment", "action point", "collision", "quicksand", "drift", "reconnection",
        "connection", "transit", "interlude", "paradox", "reversal", "turn", "reflection",
        "unveiling", "new chapter", "takeoff", "landing", "closure", "arrival", "new horizon",
        "path", "life cycle", "transformation", "revolution", "cycle", "twist", "echo", "loop",
        "grasp", "glimpse", "prediction", "alignment", "culmination", "refinement", "completion",
        "moment of choice", "perception", "illusion", "reflection", "incarnation", "passing",
        "penultimate"
    ]

    prefixes = [
        "I",
        "How to",
        "How I",
        "My first",
        "Trying to",
        "Learning to",
        "Watch me",
        "Follow me",
        "What happens when",
        "Day in the life of",
        "My journey",
        "Attempting to",
        "Unboxing",
        "Exploring",
        "Random",
        "I decided to",
        "No one asked for this but",
        "POV",
        "Can I",
        "Let’s try",
        "Behind the scenes of",
        "Everyday",
        "Homemade",
        "Testing",
        "Experimenting with",
        "My review of",
        "Unexpected",
        "When I tried",
        "So I thought",
        "Messing around with",
        "Here’s why",
        "Things you didn’t know",
        "DIY",
        "Guess what I",
        "A small",
        "A quick",
        "Reacting to",
        "My story",
        "Documenting",
        "Off the grid",
        "This happened when",
        "Just sharing",
        "Making my",
        "First attempt at",
        "Explained",
        "Doing this for the first time",
        "Random thoughts",
        "Why I",
        "The time I",
        "The story of",
        "What I",
        "Vlog about",
        "Trying something new",
        "My honest opinion on",
        "Behind the scenes",
        "My take on",
        "What’s it like to",
        "Does it work?",
        "Is it possible to",
        "A day with",
        "One week of",
        "A week in",
        "First impressions of",
        "What’s inside",
        "Just testing out",
        "Small project",
        "Experimenting with",
        "Thoughts on",
        "Random moment with"
    ]

    return f"{random.choice(prefixes)} {random.choice(terms)}"


def get_random_string():
    """ This function uses Random.org api to generate random strings for the search query.  """
    random_org_key = cfg.RANDOM_ORG_KEY
    url = f"https://api.random.org/json-rpc/4/invoke"
    body = {
        "jsonrpc": "2.0",
        "method": "generateStrings",
        "params": {
            "apiKey": random_org_key,
            "n": 1,
            "length": 12,
            "characters": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"
        },
        "id": 5215
    }
    response = requests.post(url,json=body)
    # If response okay, proceed.
    if response.status_code == 200:
        data = response.json()
        if "result" in data:
            random_string = data["result"]["random"]["data"][0]

            return random_string
    # else Return error and data info with logging
        else:
            logging.error("Error:", data["error"])
    else:
        print("Error:", response.status_code)
        print(response.text)

def get_query():
    """ Build a query based on a random number based decision. """
    the_decider = get_random_int()

    if the_decider in range(1,20000):
        query = get_random_string()
        return query
    if the_decider in range(20001, 40000):
        query = get_random_sent()
        return query
    if the_decider in range(40001, 80000):
        query = get_formed_search()
    else:
        query = " "
        return query