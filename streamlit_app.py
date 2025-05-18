import streamlit as st
import llm_interface as model
import random


class StreamlitUIUpdater:
    def __init__(self):
        st.write("# Welcome!")
        self.model = model.Model()

    def mainloop(self):
        query = st.chat_input("What's on your mind? Drop it off in here :)", key = "Input")
        response = self.model.invoke(query)
        if query is not None:
            with st.chat_message("user"):
                st.write(query)
        if response is not None:
            with st.chat_message("bot"):
                st.write(response)
        else:
            with st.chat_message("bot"):
                st.write("Error generating message.")

if __name__ == "__main__":
    app = StreamlitUIUpdater()
    try:
        app.mainloop()
    except Exception as e:
        st.write(e.args)