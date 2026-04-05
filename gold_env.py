import gradio as gr
from gold_env import GoldDetectionEnv

env = GoldDetectionEnv()

def detect_gold(text):
    env.reset()
    result = env.step("scan")
    return result["result"]

iface = gr.Interface(
    fn=detect_gold,
    inputs="text",
    outputs="text",
    title="AI Gold Detection System",
    description="Prototype system to detect gold using AI analysis."
)

iface.launch()
