import streamlit as st
import llm_interface as model


class StreamlitUIUpdater:
    def __init__(self):
        st.write("# Welcome!")
        self.model = model.Model()

    def mainloop(self):
        query = st.text_input("What's on your mind? Drop it off in here :)")
        response = self.model.invoke(query)
        st.write(f"<p align = 'left'>User:{query}</p>")
        st.write(f"<p align = 'right'>Model:{response}</p>")

if __name__ == "__main__":
    app = StreamlitUIUpdater()
    try:
        while True:
            app.mainloop()
    except Exception as e:
        print(e)