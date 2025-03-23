import streamlit as st
from pdfsearchengine import PDFSearchEngine
from flashcards import Flashcards




def main():
    # Initialize the PDFSearchApp
    
    
    # Set up the Streamlit app layout
    st.title("Neural_Navigator")
    # st.markdown(
    #     "This demo showcases how to use [Colpali](https://github.com/illuin-tech/colpali) embeddings with [Milvus](https://milvus.io/) "
    #     "and utilizing Gemini/OpenAI multimodal RAG for PDF search and Q&A."
    # )

    # Create tabs for Upload PDF and Query
    tab1, tab2, tab3 = st.tabs(["Upload PDF", "Query", "Flashcards"])

    with tab1:
        pdfsearchengine = PDFSearchEngine()
        # Upload PDF section
        st.header("Upload PDF")
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf", key="pdf_uploader_1")
        max_pages = st.slider(
            "Max pages to extract and index",
            min_value=1,
            max_value=50,
            value=20,
            step=10,
        )

        if uploaded_file is not None:
            # Process the uploaded file
            status = pdfsearchengine.process_pdf_upload(
                # session_state={"user_uuid": None},  # Replace with your state logic
                uploaded_file=uploaded_file,
                max_pages=max_pages,
            )
            st.text_area("Indexing Status", value=status, height=100, disabled=True)

    with tab2:
        # Query section
        st.header("Query")
        query = st.text_input("Enter your query")
        if st.button("Query"):
            if query:
                # Perform the search
                image_paths, rag_response = pdfsearchengine.query_pdf(
                    # session_state=,  # Replace with your state logic
                    search_query=query,
                )

                # Display the RAG response
                st.text_area("RAG Response", value=rag_response, height=100, disabled=True)

                # Display the top matching images
                if image_paths:
                    st.header("Top pages matching query")
                    for image_path in image_paths:
                        st.image(image_path, caption=image_path, use_column_width=True)
            else:
                st.warning("Please enter a query.")
    with tab3:
        flashcards = Flashcards()
        gemini_model = flashcards.setup_gemini()

        st.title("Flashcard Generator from PDF")
        st.write("Upload a PDF, and we'll generate flashcards for you!")

        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

        if 'flashcards_list' not in st.session_state:
            st.session_state.flashcards_list = []
        if 'current_index' not in st.session_state:
            st.session_state.current_index = 0
        if 'show_popup' not in st.session_state:
            st.session_state.show_popup = False

        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            text = flashcards.extract_text_from_pdf(uploaded_file)
            # st.subheader("Extracted Text Preview")
            # st.write(text[:1000] + "...")
            
            if st.button("Generate Flashcards"):
                with st.spinner("Generating flashcards..."):
                    flashcards_text = flashcards.generate_flashcards(text, gemini_model)
                    st.session_state.flashcards_list = [card.strip() for card in flashcards_text.strip().split("\n") if card]
                    st.session_state.current_index = 0
                    st.session_state.show_popup = True

        if st.session_state.show_popup and st.session_state.flashcards_list:
            with st.expander("📖 View Flashcards", expanded=True):
                index = st.session_state.current_index
                flashcards = st.session_state.flashcards_list
                
                q_card = flashcards[index] if index < len(flashcards) else "End of flashcards"
                a_card = flashcards[index + 1] if index + 1 < len(flashcards) else ""
                
                st.markdown(f"""<div style='border: 2px solid #4CAF50; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                            <strong>Q:</strong> {q_card}
                            </div>""", unsafe_allow_html=True)
                
                if a_card:
                    st.markdown(f"""<div style='border: 2px solid #2196F3; padding: 15px; border-radius: 10px;'>
                                <strong>A:</strong> {a_card}
                                </div>""", unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns([1, 2, 1])
                
                with col1:
                    if st.button("⬅️ Previous") and index > 0:
                        st.session_state.current_index -= 2
                        st.rerun()
                
                with col2:
                    if st.button("❌ Close"):
                        st.session_state.show_popup = False
                        st.rerun()
                
                with col3:
                    if st.button("Next ➡️") and index + 2 < len(flashcards):
                        st.session_state.current_index += 2
                        st.rerun()

if __name__ == "__main__":
    main()