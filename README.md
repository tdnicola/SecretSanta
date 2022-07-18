Work in progress for texting friends secret santa recipients. No one will have to help hand out names (other than creator). Great for long distance.

Reworked it from Javascript, which required a Twilio account.

Python script that uses takes JSON file to give random secret santa. We've been doing it for some years so I wanted to also create an array of previously selected people so you do not get the same person twice in a row.

```
{
        "name": "Tony",
        "phone": 111,
        "previousMatches": [
            "Tony",
            "Monika",
            "Deke",
            "Patrick",
            "Haley"
        ]
    },
```

Could create more automation in sending emails but texts are just great. Running main.py will spit out the results and then used with a [google voice extension](https://github.com/brismuth/google-voice-bulk-texter).
