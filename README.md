# Parallel process GPT requests

This program can process 1000 requests to ChatGPT in 2m. It uses the `gpt-3.5-turbo` model by default, which you can update in the file `generate_requests.py`.

I adapted the [parallel processing cookbook example written by OpenAI](https://github.com/openai/openai-cookbook/blob/main/examples/api_request_parallel_processor.py), which was written for the embeddings model. I adapted it to work for the Chat Completion models, which has a different request structure.

## Get the program up and running

1. Clone the repo: `git clone https://github.com/tiny-rawr/ZH_008_parallel_chatgpt_processing.git parallel_process_gpt_requests`
2. Replace 'input.csv' with your own data. Column A should contain data for each separate request you want to make to ChatGPT. In this case, I have an input file containing details for 10 different medical specialists, one in each cell in the column. Alternatively, you can just replace the data in `data.py` with an array of the data you want to send in each request (not including the prompt).
3. Replace the prompt in `main.py` with your own prompt instructions.
4. Set your API key with `export OPENAI_API_KEY="YOUR API KEY"`
5. Install dependencies with `pip install -r requirements.txt`
6. Run the program with `python3 main.py`

## What happens when you run the program

When you run the program, four files are generated:
- `data.py` turns the values in the first column of the `input.csv` into an array. It's saved to a file so you don't have to generate them all each time.
- `example_requests_to_chat_completion.jsonl`, is a list of requests that will be send to ChatGPT.
- `example_requests_to_chat_completion_results.jsonl`, the entire request including input and output (same as previous file but with output included).
- `output.csv` is a spreadsheet containing the original values passed into chatgpt in column A, and the processed by ChatGPT values in column B.