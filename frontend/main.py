import os

import requests
import streamlit as st

API_BASE_URL = os.getenv("API_ENDPOINT", "http://localhost:8000")
SEARCH_ENDPOINT = f"{API_BASE_URL}/search"

st.title("Movie Recommendation Search")

st.write("Enter your query and filter options below:")

with st.form("search_form"):
    query = st.text_input("Search Query", value="", placeholder="Type your search query here...")

    top_n = st.number_input("Number of Results", min_value=1, max_value=20, value=5, step=1)

    st.subheader("Filter Options")
    min_release_date = st.text_input("Minimum Release Date (YYYY-MM-DD)", value="1990-01-01")
    min_vote_average = st.number_input("Minimum Vote Average", min_value=0.0, value=0.0, step=0.1)
    min_vote_count = st.number_input("Minimum Vote Count", min_value=0, value=0, step=1)

    submit_button = st.form_submit_button(label="Search")

if submit_button:
    # Construct the request payload
    payload = {
        "query": query,
        "top_n": int(top_n),
        "filters": {
            "min_release_date": min_release_date,
            "min_vote_average": float(min_vote_average),
            "min_vote_count": int(min_vote_count)
        }
    }

    try:
        response = requests.post(SEARCH_ENDPOINT, json=payload)
        response.raise_for_status()

        results = response.json()

        if results:
            st.write("### Search Results")
            for movie in results:
                st.write(f"#### {movie.get('title', 'No Title')}")
                st.write(f"**Overview:** {movie.get('overview', 'No Overview')}")
                st.write(f"**Release Date:** {movie.get('release_date', 'N/A')}")
                st.write(f"**Popularity:** {movie.get('popularity', 'N/A')}")
                st.write(f"**Vote Average:** {movie.get('vote_average', 'N/A')}")
                st.write(f"**Vote Count:** {movie.get('vote_count', 'N/A')}")
                st.write(f"**Similarity:** {movie.get('similarity', 'N/A')}")
                st.markdown("---")
        else:
            st.write("No results found.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
