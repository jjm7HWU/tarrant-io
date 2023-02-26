intents = {
    "greet": {
        "call_function": False,
        "examples": [
            "hello",
            "hi",
            "good morning",
            "good evening",
            "howdy",
            "hiya",
            "nice to see you",
            "hey",
            "hey there",
            "hello there",
            "hey mate",
            "yo"
        ]
    },
    "greet_question": {
        "call_function": False,
        "examples": [
            "how are you",
            "how's it going",
            "how are you doing",
            "what's up",
            "wassup",
            "what's rolling",
            "how you doing"
        ]
    },
    "goodbye": {
        "call_function": False,
        "examples": [
            "goodbye",
            "bye",
            "i got to go",
            "i need to head"
        ]
    },
    "affirm": {
        "call_function": False,
        "examples": [
            "yes",
            "sure",
            "okay",
            "alright okay",
            "let's go with that",
            "yeah",
            "will do",
            "fine",
            "of course",
            "absolutely",
            "definitely",
            "one hundred percent",
            "a hundred percent"
        ]
    },
    "reject": {
        "call_function": False,
        "examples": [
            "no",
            "no way",
            "nope",
            "no thank you",
            "hell no",
            "not at all",
            "never",
            "i disagree",
            "definitely not",
            "absolutely not",
            "probably not",
            "no chance",
            "not happening",
            "there's no way",
            "it can't be",
            "i don't think so",
            "i don't think it could be"
        ]
    },
    "well": {
        "call_function": False,
        "examples": [
            "i'm doing great",
            "absolutely fantastic",
            "great",
            "i'm doing very well",
            "i feel great",
            "very good thank you",
            "good thanks",
            "happy",
            "awesome",
            "i'm doing great",
            "pretty good thanks"
        ]
    },
    "not_well": {
        "call_function": False,
        "examples": [
            "i'm not doing great",
            "absolutely awful",
            "not great",
            "i'm not doing very well",
            "i feel shit",
            "not very well to be honest",
            "crap",
            "rubbish",
            "i don't feel well",
            "really bad",
            "miserable",
            "not so good",
            "not so well",
            "pretty bad",
            "not great",
            "not the best",
            "rather poorly",
            "not at all",
            "not at all well"
        ]
    },
    "suggest": {
        "call_function": True,
        "examples": [
            "is it SLOT_1",
            "it could be SLOT_1",
            "should i go with SLOT_1",
            "is it maybe SLOT_1",
            "it could be SLOT_1",
            "the answer might be SLOT_1",
            "will SLOT_1 be correct",
            "is SLOT_1 the answer",
            "it's quite likely SLOT_1",
            "i wonder if SLOT_1 is it",
            "i have a nagging feeling it's SLOT_1",
            "i'm thinking SLOT_1",
            "i think it could be SLOT_1",
            "SLOT_1 perhaps",
            "SLOT_1 maybe",
            "maybe SLOT_1",
            "it is possible that it's SLOT_1",
            "it could in fact be SLOT_1",
            "SLOT_1 is possible",
            "probably SLOT_1",
            "SLOT_1 might be it",
            "i'm not sure maybe SLOT_1",
            "how about SLOT_1",
            "should we go with SLOT_1",
            "what about SLOT_1",
            "and SLOT_1 what about that"
        ]
    },
    "exclude": {
        "call_function": True,
        "examples": [
            "it isn't SLOT_1",
            "it is not SLOT_1",
            "it couldn't be SLOT_1",
            "i'm not going with SLOT_1",
            "it couldn't be SLOT_1",
            "the answer is not SLOT_1",
            "well SLOT_1 isn't correct",
            "SLOT_1 isn't the answer",
            "i know SLOT_1 isn't the answer",
            "it's definitely not SLOT_1",
            "i know it's not SLOT_1",
            "i can reject SLOT_1",
            "i can rule out SLOT_1",
            "it definitely isn't SLOT_1",
            "probably not SLOT_1",
            "it simply cannot be SLOT_1",
            "there's no way that SLOT_1 is the right answer",
            "we can rule out SLOT_1",
            "obviously it's not SLOT_1",
            "SLOT_1 is not the answer",
            "SLOT_1 couldn't be right",
            "it's definitely not going to be SLOT_1 that's wrong",
            "no not SLOT_1",
            "not SLOT_1",
            "no way it's SLOT_1",
            "not SLOT_1 no way",
            "there's no way it's SLOT_1",
            "i'm confident it's not SLOT_1",
            "it's not SLOT_1 i know that without a doubt",
            "definitely not SLOT_1"
        ]
    },
    "answer": {
        "call_function": True,
        "examples": [
            "SLOT_1",
            "SLOT_1 most likely",
            "SLOT_1",
            "it's SLOT_1",
            "it is SLOT_1",
            "it's definitely SLOT_1",
            "i think it's SLOT_1",
            "it's got to be probably SLOT_1",
            "i'm going to go with SLOT_1",
            "has to be SLOT_1",
            "gotta be SLOT_1",
            "the answer's SLOT_1",
            "let's go with SLOT_1",
            "definitely an SLOT_1",
            "definitely SLOT_1",
            "it's almost certainly SLOT_1",
            "i wonder if it's SLOT_1 yeah it is",
            "definitely SLOT_1",
            "let's say SLOT_1",
            "i'm gonna pick SLOT_1",
            "i'm guessing SLOT_1",
            "SLOT_1 is my best guess",
            "SLOT_1 i think",
            "SLOT_1 is definitely the answer",
            "SLOT_1 is it",
            "it has to be SLOT_1",
            "i'm confident it's SLOT_1",
            "i'm going to say SLOT_1",
            "SLOT_1 that's what i think",
            "SLOT_1 without a doubt"
        ]
    }
}
