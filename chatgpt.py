from decouple import config
from openai import OpenAI



def get_gpt_reply(prompt):
    client = OpenAI(
    api_key=config('OPENAI_API')
    )

    response = client.chat.completions.create(
        model= 'gpt-3.5-turbo',
        messages = [{"role":"user", 'content':prompt}],
        # max_tokens= max_tokens,
        )
    response_message = response.choices[0].message.content

    return response_message



