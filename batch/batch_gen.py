from openai import OpenAI
client = OpenAI()

client.batches.create(
  input_file_id="to-do-with-txt-to-img-orimg-to-img",
  endpoint="/v1/chat/completions",
  completion_window="24h"
)

client = OpenAI()

client.batches.retrieve("batch_abc123")
