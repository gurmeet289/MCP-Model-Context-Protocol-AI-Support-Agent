import subprocess

def run_llm(prompt: str) -> str:
    """Call Mistral via Ollama and return the model's response safely."""
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode("utf-8"),  
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )

        if result.returncode != 0:
            return f"LLM Error:\n{result.stderr.decode('utf-8', errors='replace').strip()}"

        output = result.stdout.decode("utf-8", errors="replace").strip()
        return output or "No output from model."

    except subprocess.TimeoutExpired:
        return "Timeout: LLM took too long."

    except Exception as e:
        return f"Exception while calling LLM:\n{str(e)}"
