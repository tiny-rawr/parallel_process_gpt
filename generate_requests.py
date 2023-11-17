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

# In progress: This is to generate more complex requests.
# Pushing to main to share as example, but not used in rest of prog rn.
def generate_gpt_request(prompt, data, functions=[]):
    model = "gpt-3.5-turbo"
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": str(data)}
    ]
    if functions:
        return json.dumps({"model": model, "messages": messages, "tools": functions})
    else:
        return json.dumps({"model": model, "messages": messages})

if __name__ == "__main__":
    # Generate simple request for summarising text
    prompt = "Please summarise the following text."
    text = "Chat Completions API: Chat models take a list of messages as input and return a model-generated message as output. Although the chat format is designed to make multi-turn conversations easy, it’s just as useful for single-turn tasks without any conversation."
    summarise_text = generate_gpt_request(prompt, text)
    print(summarise_text)

    # Generate complex request for extracting podcast details
    prompt = "Please extract the requested key details from this podcast."
    text = "Hello this is Tim Ferris and in this podcast we will be chatting with Harry Potter about his time at Hogwarts and his journey to vanquishing voldemort."
    functions = [{
        "type": "function",
        "function": {
            "name": "get_guest_name",
            "description": "Get the name of the guest speaker",
            "parameters": {
                "type": "object",
                "properties": {
                    "interviewer": {
                        "type": "string",
                        "description": "The name of the interviewer",
                    },
                    "guest": {
                        "type": "string",
                        "description": "The name of the guest speaker",
                    },
                    "topics": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "What topics are discussed?"
                        }
                    }
                },
                "required": ["interviewer", "guest", "topics"],
            },
        },
    }]

    podcast_deets = generate_gpt_request(prompt, text, functions)
    print(podcast_deets)

