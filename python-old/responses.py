responses = {
    "introduction": {
        "EXEC": "utter('greet'); utter('greet_question')",
        "well": "utter('celebrate'); change_state('invite')",
        "not_well": "utter('regret'); utter('console'); change_state('invite')",
        "DEFAULT": "change_state('invite')"
    },
    "invite": {
        "EXEC": "say('Would you like to play Who Wants To Be A Millionaire?')",
        "affirm": "say('Awesome! Then let us begin.'); change_state('ask_question')",
        "reject": "say('Too bad. Maybe next time then.'); change_state('goodbye')",
        "DEFAULT": "say(\"I'm sorry. I don't quite understand your answer. Was that a yes?\")"
    },
    "goodbye": {
        "EXEC": "say('Catch you later.')"
    },
    "ask_question": {
        "EXEC": "configure_question(); utter('ask_question')",
        "answer": "say('You are answering.'); change_state('seek_confirmation')",
        "suggest": "say('You are suggesting.'); change_state('seek_confirmation')",
        "exclude": "say('You are excluding.')",
        "DEFAULT": "say('Let me process what you just said.')"
    },
    "seek_confirmation": {
        "EXEC": "utter('seek_confirmation')",
        "affirm": "say('Let us check the answer then.'); change_state('lock_answer')",
        "reject": "say(\"I'll give you more time\"); change_state('repeat_question')",
        "DEFAULT": "say('Let me process what you just said.')"
    },
    "lock_answer": {
        "EXEC": "say('The result is...')",
        "DEFAULT": "say('Narley')"
    }
}
