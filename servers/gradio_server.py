import gradio as gr
import random


programming_facts = [
    "The first computer programmer was Ada Lovelace.",
    "Python is named after the British comedy group Monty Python.",
    "The first ever computer virus was created in 1971 and was called the 'Creeper' program."
]


def get_programming_fact() -> str:
    """Get a random programming fact."""
    return random.choice(programming_facts)


demo = gr.Interface(
    fn=get_programming_fact,
    inputs=["text", "text"],
    outputs="number",
    title="Letter Counter",
    description="Count how many times a letter appears in a word"
)

demo.launch(
    mcp_server=True,
    strict_cors=False
)
