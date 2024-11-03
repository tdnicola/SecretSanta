
# Secret Santa Matcher

## Overview
This Python script facilitates an annual Secret Santa event by matching participants listed in a `sample.json` file. It ensures that participants are not matched with someone they have gifted to in previous years, preventing duplicates and maintaining fairness. Once confirmed, the matches are recorded in the JSON file for future reference.

## File Structure

### `sample.json`
This JSON file contains participant information, including their names, phone numbers, and a record of previous matches with the year they were matched. The format looks like this:

```json
[
    {
        "name": "Tony",
        "phone": 1111111111,
        "previousMatches": [
            {
                "name": "Zach",
                "year": 2023
            }
        ]
    },
    {
        "name": "Zach",
        "phone": 2222222222,
        "previousMatches": [
            {
                "name": "Patrick",
                "year": 2023
            }
        ]
    },
    {
        "name": "Patrick",
        "phone": 3333333333,
        "previousMatches": [
            {
                "name": "Tony",
                "year": 2023
            }
        ]
    },
    {
        "name": "Deke",
        "phone": 4444444444,
        "previousMatches": [
            {
                "name": "Steve",
                "year": 2023
            }
        ]
    },
    {
        "name": "Steve",
        "phone": 5555555555,
        "previousMatches": [
            {
                "name": "Deke",
                "year": 2023
            }
        ]
    }
]
```

### Python Script
The script includes the following main functions:
- **`is_valid_match(gifter, recipient)`**: Checks if the recipient is valid for the gifter by ensuring the recipient is not in the `gifter`'s `previousMatches` and is not the `gifter` themselves.
- **`create_secret_santa(santa_data)`**: Generates a valid Secret Santa matching, ensuring each participant matches with a unique recipient and avoiding previous matches.
- **`update_previous_matches(santa_data, matches, year)`**: Updates the `previousMatches` field in `sample.json` with the current year's matches.

## How to Use

1. **Ensure `sample.json` is structured correctly** as shown above.
2. **Run the script** in your Python environment.
3. **Review the generated matches**:
   - The script will print the matches and prompt for confirmation.
   - Enter `yes` to confirm and update `sample.json`, or `no` to reshuffle and try again.
4. **Output Example**:
   ```
   Secret Santa Matching Results:
   Tony (Phone: 1111111111) is giving a gift to Zach
   Zach (Phone: 2222222222) is giving a gift to Patrick
   Patrick (Phone: 3333333333) is giving a gift to Deke
   Deke (Phone: 4444444444) is giving a gift to Steve
   Steve (Phone: 5555555555) is giving a gift to Tony

   Do you want to confirm this matching? (yes/no): yes
   Matches have been confirmed and updated in sample.json.
   ```

## Customization

- **Add New Participants**:
  - To add new participants, append them to `sample.json` with an empty `previousMatches` array.
- **Customize the JSON Structure**:
  - Ensure each `previousMatches` entry includes a `name` and `year` field for consistency.
- **Logging and Error Handling**:
  - Consider adding logging for better error tracking and debugging.

## Requirements

- **Python Libraries**:
  - `json` (standard library)
  - `random` (standard library)
  - `datetime` (standard library)

## Troubleshooting

- **No Valid Matches Found**:
  - If the script raises an error stating it couldn't find a valid match after 1000 attempts, review the `previousMatches` data to ensure there are enough possible matches.
- **Backup Data**:
  - It’s recommended to create a backup of `sample.json` before running the script to preserve the original data.

## Future Enhancements

- **Add GUI**:
  - Integrate a simple graphical user interface (GUI) for user interaction.
- **Track Multiple Years**:
  - Enhance the script to handle matches over multiple years more flexibly.


Could create more automation in sending emails but texts are just great. Running main.py will spit out the results and then used with a [google voice extension](https://github.com/brismuth/google-voice-bulk-texter).
