import asyncio
import os
from api_request_parallel_processor import process_api_requests_from_file
from generate_requests import generate_chat_completion_requests
from save_generated_data_to_csv import save_generated_data_to_csv
from csv_to_array import convert_csv_to_array
from prompts import specialist_bio_prompt, clinic_bio_prompt

if __name__ == "__main__":
    prompt = clinic_bio_prompt

    if not os.path.exists('data.py'):
        data = convert_csv_to_array("input.csv", "data.py")
        from data import data
    else:
        from data import data

    # data = data[:10] limit data for testing
    requests_filepath = "example_requests_to_chat_completion.jsonl"
    requests_output_filepath = "example_requests_to_chat_completion_results.jsonl"

    #generate_chat_completion_requests(requests_filepath, data, prompt, model_name="gpt-3.5-turbo-16k")

    # Process multiple api requests to ChatGPT
    asyncio.run(
        process_api_requests_from_file(
            requests_filepath=requests_filepath,
            save_filepath=requests_output_filepath,
            request_url="https://api.openai.com/v1/chat/completions",
            api_key=os.getenv("OPENAI_API_KEY"),
            max_requests_per_minute=float(90000),
            max_tokens_per_minute=float(170000),
            token_encoding_name="cl100k_base",
            max_attempts=int(5),
            logging_level=int(20),
        )
    )

    save_generated_data_to_csv(requests_output_filepath)