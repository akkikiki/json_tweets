def clean_escapes(tweet):
    ESCAPES = ["\n", "\r\n"]
    for escape in ESCAPES:
        tweet = tweet.replace(escape, "")
    return tweet

def clean_puncts(tweet):
    ESCAPES = [".", ":", ","]
    for escape in ESCAPES:
        tweet = tweet.replace(escape, " " + escape )
    return tweet
