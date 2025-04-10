
import streamlit as st
import wikipedia
from PIL import Image

# Load logo
logo = Image.open("A_digital_vector_graphic_logo_features_a_stylized_.png")
st.image(logo, width=120)

# Agent functions with real API

def agent_1_research(topic):
    try:
        summary = wikipedia.summary(topic, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"The topic is ambiguous. Please be more specific. Options: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return "No page found for this topic. Try another one."

def agent_2_verify(content):
    # Simulated verification
    return f"[Verified]: {content}"

def agent_3_write(verified_content):
    return f"Final article draft:\n\n{verified_content}\n\nThe article has been revised for clarity and readability."

# Streamlit UI
st.title("Multi-Agent AI Workflow Demo")
st.write("This demo uses real Wikipedia content to simulate a multi-agent AI article generation pipeline.")

topic = st.text_input("Enter a topic for the article:")

if st.button("Run Workflow") and topic:
    st.subheader("Step 1: Agent 1 - Research")
    research_output = agent_1_research(topic)
    st.write(research_output)

    st.subheader("Step 2: Agent 2 - Verification")
    verified_output = agent_2_verify(research_output)
    st.write(verified_output)

    st.subheader("Step 3: Agent 3 - Writing")
    final_article = agent_3_write(verified_output)
    st.success("Final Output:")
    st.write(final_article)

    with st.expander("Show Logs"):
        st.json({
            "input_topic": topic,
            "agent_1_output": research_output,
            "agent_2_output": verified_output,
            "agent_3_output": final_article
        })
