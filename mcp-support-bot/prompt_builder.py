from typing import List, Dict

def build_prompt(latest_input: str, past_chunks: list) -> str:
    prompt = "You are a helpful AI support assistant.\n\n"
    if past_chunks:
        prompt += "Here is what the user previously said or asked :\n"
        for chunk in past_chunks:
            prompt += f"[{chunk['timestamp']}] {chunk['message']}\n"
    prompt += f"\nNow the user says: \"{latest_input}\"\n"
    prompt += "Respond in a helpful and relevant way."
    return prompt

