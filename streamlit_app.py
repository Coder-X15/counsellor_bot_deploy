import streamlit as st
import llm_interface as model
import random


class StreamlitUIUpdater:
    def __init__(self):
        st.write("# Welcome!")
        self.model = model.Model()

    def mainloop(self):
        # initialize session variable `messages``
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # print messages from chat history (i.e., the `messages` variable)
        for message in st.session_state.messages:
            with st.chat_message(message['role']):
                st.write(message['content'])

        # activates the query-response system upon user prompt
        if query := st.chat_input("What's on your mind? Drop it off in here :)", key = "Input"):

            # step 1: make markdown version of user query and add it to chat history
            st.chat_message("user").markdown(query)
            st.session_state.messages.append({"role": "user", "content":query})
            

            # step 2: generate response
            response = self.model.invoke(query)

            # step 3: add response to chat history
            st.chat_message("assistant").markdown(response)
            st.session_state.messages.append({"role":"assistant","content":response})

if __name__ == "__main__":
    app = StreamlitUIUpdater()
    try:
        app.mainloop()
    except Exception as e:
        st.write(e.args)