import streamlit as st
from text_to_speech import speak_text

def show_learning_companion_page():
    st.title("📚 Learning Companion")

    # Initialize session state if not set
    if "learning_companion_action" not in st.session_state:
        st.session_state.learning_companion_action = None

    # Display three buttons with better layout
    col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])

    with col1:
        if st.button("🎙 Books to Speech", use_container_width=True):
            if st.session_state.learning_companion_action != "books_to_speech":
                st.session_state.learning_companion_action = "books_to_speech"
                st.rerun()

    with col3:
        if st.button("🃏 Flashcards", use_container_width=True):
            if st.session_state.learning_companion_action != "flashcards":
                st.session_state.learning_companion_action = "flashcards"
                st.rerun()

    with col5:
        if st.button("📖 Books Buddy", use_container_width=True):
            if st.session_state.learning_companion_action != "books_buddy":
                st.session_state.learning_companion_action = "books_buddy"
                st.rerun()

    # Handle button actions
    if st.session_state.learning_companion_action == "books_to_speech":
        # speak_text()
        print(True)

    elif st.session_state.learning_companion_action == "flashcards":
        st.subheader("🃏 Flashcards")
        st.write("Use flashcards to reinforce learning:")
        st.write("- Create custom flashcards for different subjects.")
        st.write("- Test yourself to improve memory retention.")
        st.write("- Use spaced repetition for better recall.")

    elif st.session_state.learning_companion_action == "books_buddy":
        st.subheader("📖 Books Buddy")
        st.write("Chat with an AI assistant for study help:")
        user_input = st.text_input("You:", key="chat_input")
        if st.button("Send", key="chat_send"):
            if user_input:
                st.write(f"**AI:** Here's a response to '{user_input}'.")
            else:
                st.warning("Please enter a message before sending.")

    # Back to Home Button (Always Visible)
    st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing before back button
    if st.button("⬅️ Back to Home", key="back_home"):
        st.session_state.page = "home"
        st.session_state.learning_companion_action = None  # Clear the action state
        st.rerun()
