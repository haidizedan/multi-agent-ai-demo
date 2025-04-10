
import streamlit as st

# Simulated agent functions
def agent_1_research(topic):
    return f"Collected recent and relevant information about '{topic}' from reliable sources."

def agent_2_verify(content):
    return f"Verified facts and corrected inaccuracies in the following content: {content}"

def agent_3_write(verified_content):
    return f"Final article draft: Based on {verified_content}. Written in a clear, user-friendly style."

# Page UI
st.title("Multi-Agent AI Workflow Demo")
st.write("This demo simulates a system where multiple AI agents collaborate to generate an article.")

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
