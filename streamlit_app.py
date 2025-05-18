import streamlit as st
import llm_interface as model


class StreamlitUIUpdater:
    def __init__(self):
        st.write("# Welcome!")
        self.model = model.Model()

    def mainloop(self):
        query = st.chat_input("What's on your mind? Drop it off in here :)")
        response = self.model.invoke(query)
        st.write(f"**User:**{query}")
        st.write(f"**Model:**{response}")

if __name__ == "__main__":
    app = StreamlitUIUpdater()
    try:
        while True:
            app.mainloop()
    except Exception as e:
        print(e)