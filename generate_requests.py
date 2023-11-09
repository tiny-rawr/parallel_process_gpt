import json

def generate_chat_completion_requests(filename, data, prompt, model_name="gpt-3.5-turbo"):
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