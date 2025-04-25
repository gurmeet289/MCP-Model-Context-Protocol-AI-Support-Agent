import streamlit as st
from mcp_memory import store_memory, retrieve_relevant_chunks
from prompt_builder import build_prompt
from llm_runner import run_llm

st.set_page_config(page_title=" MCP AI Support Agent", layout="centered")
st.title("MCP AI Support Agent")

# UI Inputs
user_id = st.text_input("Enter your user ID:", "")
issue_type = st.selectbox("Select issue type:", ["billing", "technical", "general"])
plan = st.selectbox("Your current plan:", ["Free", "Pro", "Enterprise"])
user_message = st.text_area("Your message:")

if st.button("Submit Message"):
    if user_id and user_message:
        store_memory(user_id, issue_type, plan, user_message)
        past_chunks = retrieve_relevant_chunks(user_id, issue_type)

        st.subheader("Past Memory Retrieved:")
        for i, chunk in enumerate(past_chunks):
            st.markdown(f"**[{i+1}]** {chunk['message']} *(Plan: {chunk['plan']}, Time: {chunk['timestamp']})*")

        prompt = build_prompt(user_message, past_chunks)

        st.subheader("Final Prompt Sent to LLM:")
        st.code(prompt, language="markdown")

        response = run_llm(prompt)

        st.subheader("🤖 AI Support Bot Response:")
        st.write(response)
    else:
        st.warning("Please enter both your user ID and a message.")
