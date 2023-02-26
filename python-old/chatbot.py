import spacy
import re
from random import randint
from spacy.matcher import Matcher

from constants import *
from actions import actions
from intents import intents
from responses import responses

from questions import QUESTION_SET

def extract_options_mentioned(user_speech):

    print(COLOUR_GREEN, end = "")

    doc = nlp(user_speech)
    matches = matcher(doc)

    options_mentioned = []

    index = 1

    for match_id, start, end in matches:
        span = doc[start:end]
        text = span.text
        options_mentioned.append(match_id_answers[str(match_id)])
        user_speech = user_speech.replace(text, "SLOT_" + str(index))
        index += 1

    print(COLOUR_NONE, end = "")

    return options_mentioned, user_speech


def chatbot(statement):

    if convo["question_number"] > 0:
        mentions, statement_for_comparison = extract_options_mentioned(statement)
    else:
        mentions, statement_for_comparison = [], statement

    statement = nlp(statement)

    intent_name, intent_args = get_intent(statement, mentions, debug_mode = True)

    chatbot_respond(intent_name, intent_args)


def chatbot_respond(intent_name, intent_args):

    if intents[intent_name]["call_function"]:
        intent_command = intent_name + "(\"" + "\", \"".join(intent_args) + "\")"
        evaluate(intent_command)

    q = convo["q"]
    response_spec = responses[q]

    if intent_name in response_spec.keys():
        chosen_response = response_spec[intent_name]
    else:
        chosen_response = response_spec["DEFAULT"]

    evaluate(chosen_response)


def print_sims(sims):
    print(COLOUR_YELLOW, end = "")
    for key in sims.keys():
        print("{:.2f}\t{}".format(sims[key], key))
    print(COLOUR_NONE)
    

def get_intent_similarities(statement, mentions, weights = {}, debug_mode = False):

    chosen_intent = ""
    maximum_similarity = 0
    sims = {}

    for intent_name in intents:
        intent = intents[intent_name]

        acc = 0
        closest_example = { "similarity": 0, "statement": "" }
        for comp_statement in intent["examples"]:
            comp_statement = nlp(comp_statement)
            similarity = comp_statement.similarity(statement)
            acc += similarity
            if similarity >= closest_example["similarity"]:
                closest_example["similarity"] = similarity
                closest_example["statement"] = comp_statement

        similarity_score = acc / len(intent["examples"])
        similarity_score *= closest_example["similarity"] ** 3

        if intent_name in weights.keys():
            similarity_score *= weights[intent_name]
        else:
            similarity_score *= 0.5

        sims[intent_name] = similarity_score

        if similarity_score >= maximum_similarity:
            chosen_intent = intent_name
            maximum_similarity = similarity_score

    return chosen_intent, sims


def get_intent(statement, mentions, weights = {}, debug_mode = False):

    intent_name, sims = get_intent_similarities(statement, mentions, weights, debug_mode)

    intent_args = mentions

    if DEBUG_PRINT_SIMS:
        print_sims(sims)


    if intents[intent_name]["call_function"]:
        display("User intent: " + intent_name + "(\"" + "\", \"".join(intent_args) + "\")")
    else:
        display("User intent: " + intent_name)

    return intent_name, intent_args


def utter(utterance):
    examples = actions[utterance]["examples"]
    speech = examples[randint(0, len(examples) - 1)]
    x = re.search("#\[.*?\]", speech)
    while x != None:
        span = x.span()
        text = speech[span[0]:span[1]]
        inner_value = text[2:-1]
        print("Inner Value:")
        print(inner_value)
        eval_value = "convo[\"" + inner_value + "\"]"
        speech = speech.replace(text, str(eval(eval_value)))
        x = re.search("#\[.*?\]", speech)
    say(speech)


def change_state(new_state):
    prev_state = convo["q"]
    convo["q"] = new_state
    display("State change: " + prev_state + " -> " + new_state)
    response_spec = responses[new_state]
    if "EXEC" in response_spec.keys():
        evaluate(response_spec["EXEC"])


def say(string):
    print(COLOUR_CYAN, end = "")
    print(string)
    print(COLOUR_NONE, end = "")


def evaluate(string):
    string = string.split(";")
    for command in string:
        eval(command)

def configure_question():
    # CUSTOM ACTION
    convo["question_number"] += 1
    convo["question_reward"] = QUESTION_REWARDS[convo["question_number"]]
    question = get_question()
    for key in question.keys():
        convo[key] = question[key]
    #say(question["text"])

def get_question():
    global matcher, match_id_answers

    i = randint(0, len(QUESTION_SET) - 1)
    question = QUESTION_SET[i]

    # specify answer options to be matched in user statements
    matcher = Matcher(nlp.vocab)

    match_id_answers = {}

    for i in range(4):

        letter = chr(65 + i)
        synonyms = question["synonyms"][letter]
        patterns = [pattern_format(question[letter])]
        for synonym in synonyms:
            patterns.append(pattern_format(synonym))

        matcher.add("OPTION_" + letter, patterns)

    for letter in ["A", "B", "C", "D"]:
        # determine match IDs 
        match_name = question[letter]
        doc = nlp(match_name.lower())
        match = matcher(doc)
        match_id_answers[str(match[0][0])] = letter
    
    return question

def display(string):
    print(COLOUR_YELLOW, end = "")
    print(string)
    print(COLOUR_NONE, end = "")

def suggest(letter):
    for l in "ABCD":
        convo["leanings"][l] /= 2
    convo["leanings"][letter] = (1 + convo["leanings"][letter]) / 2
    convo["last_suggestion"] = convo[letter]

def exclude(letter):
    convo["leanings"][letter] = 0

def pattern_format(string):
    string = string.lower().split()
    pattern = []
    for word in string:
        pattern.append({ "LOWER": word })
    return pattern

def get_user_speech():
    # TODO
    user_speech = input("> ")
    return user_speech

# load model
nlp = spacy.load("en_core_web_md")

matcher = Matcher(nlp.vocab)

convo = {
    "q": "",
    "question_number": 0,
    "leanings": {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
    },
    "last_suggestion": "BLANK",
    "urgency": 12
}

change_state("introduction")

# main loop
while True:
    statement = ""
    while statement == "":
        statement = get_user_speech()
    if statement == "exit":
        break
    chatbot(statement)

say("Goodbye!")
