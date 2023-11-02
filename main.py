import asyncio
import os
from api_request_parallel_processor import process_api_requests_from_file
from generate_requests import generate_chat_completion_requests
from save_generated_data_to_csv import save_generated_data_to_csv
from data import data

if __name__ == "__main__":
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
    requests_filepath = "example_requests_to_chat_completion.jsonl"
    requests_output_filepath = "example_requests_to_chat_completion_results.jsonl"
    openai_endpoint = "https://api.openai.com/v1/chat/completions"
    max_requests_per_minute = 90000
    max_tokens_per_minute = 170000
    max_attempts = 5
    logging_level = 20
    data = data[:10]

    generate_chat_completion_requests(requests_filepath, data, prompt, model_name="gpt-3.5-turbo-16k")

    # Process multiple api requests to ChatGPT
    asyncio.run(
        process_api_requests_from_file(
            requests_filepath=requests_filepath,
            save_filepath=requests_output_filepath,
            request_url=openai_endpoint,
            api_key=os.getenv("OPENAI_API_KEY"),
            max_requests_per_minute=float(max_requests_per_minute),
            max_tokens_per_minute=float(max_tokens_per_minute),
            token_encoding_name="cl100k_base",
            max_attempts=int(max_attempts),
            logging_level=int(logging_level),
        )
    )

    save_generated_data_to_csv(requests_output_filepath)