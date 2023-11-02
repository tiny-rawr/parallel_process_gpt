import json
from data import data

prompt = """
Write me a comprehensive and professional medical profile in 3rd person that is factual and starts with the professionals name and title without headings:
- The bio should be a minimum of 200 words.
- Use British spelling only, not American spelling.
- Never say [name] is a [gender].
- Use simple to the point language.
- Never say 'highly skilled' or 'highly experienced'.
- Never say 'as an...'
- Only mention the APHRA number briefly when you do mention it, and not at the start of the bio.
- The fields below have information you can use to create the content.
- Where the field answer is empty, do not include and do not include missing fields.
- Do not include information that is not completed.
"""

def generate_chat_completion_requests(filename, data, prompt, model_name="gpt-3.5-turbo-16k"):
    with open(filename, "w") as f:
        for x in data:
            # Create a list of messages for each request
            messages = [
                {"role": "system", "content": prompt},
                {"role": "user", "content": str(x)}
            ]

            # Write the messages to the JSONL file
            json_string = json.dumps({"model": model_name, "messages": messages})
            f.write(json_string + "\n")