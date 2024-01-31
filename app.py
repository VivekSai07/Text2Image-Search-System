import streamlit as st
from Text2Image_search import MultimodalSearch

st.set_page_config(
    layout="wide",
    page_title="Text2Image Search App",
    page_icon="🔍"
)

# Add custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #89cff0; /* Set your desired background color */
        }
        .stMarkdown h1 {
            text-align: center;
            color: #cb4154;
        }
        .stTextInput {
            width: 50%; /* Adjust the width as needed */
            margin: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.markdown("<h1>Text2Image Search App</h1>", unsafe_allow_html=True)

    multimodal_search = MultimodalSearch()

    query = st.text_input("Enter your query:")
    C1, C2, C3 = st.columns([1, 1, 1])
    with C2:
        searchBtn = C2.button('Search')
        if searchBtn:
            if len(query) > 0:
                results = multimodal_search.search(query)
                st.warning("Your query was "+query)
                st.subheader("Search Results:")
                col1, col2, col3 = st.columns([1,1,1])
                with col1:
                    st.write(f"Score: {round(results[0].score*100, 2)}%")
                    st.image(results[0].content, use_column_width=True)
                with col2:
                    st.write(f"Score: {round(results[1].score*100, 2)}%")
                    st.image(results[1].content, use_column_width=True)
                with col3:
                    st.write(f"Score: {round(results[2].score*100, 2)}%")
                    st.image(results[2].content, use_column_width=True)
            else:
                st.warning("Please enter a query.")

if __name__ == "__main__":
    main()