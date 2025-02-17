import streamlit as st
import pickle
import pandas as pd
import requests
import time

st.set_page_config(page_title="Movie Matrix", page_icon="🌌", layout="wide")

 
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Exo+2:wght@300;500;700&display=swap');
    
    /* Base styles */
    body {
        background: linear-gradient(135deg, #0a0a2e, #1a1a4a);
        color: #e0e0ff;
        font-family: 'Exo 2', sans-serif;
        overflow-x: hidden;
    }
    
    /* Cyberpunk title animation */
    .cyber-title {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        position: relative;
        font-size: 3.5rem;
        text-transform: uppercase;
        color: #0ff;
        text-shadow: 0 0 10px #0ff,
                     0 0 20px #0ff,
                     0 0 30px #0ff;
        animation: neonPulse 1.5s infinite alternate;
    }
    
    @keyframes neonPulse {
        from { text-shadow: 0 0 5px #0ff, 0 0 10px #0ff; }
        to { text-shadow: 0 0 20px #0ff, 0 0 30px #0ff; }
    }
    
    /* Holographic card effect */
    .holographic-card {
        background: rgba(16, 16, 64, 0.8);
        border: 1px solid #0ff;
        border-radius: 15px;
        position: relative;
        overflow: hidden;
        transition: transform 0.3s ease;
        padding: 15px;
        margin: 10px;
    }
    
    .holographic-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, 
            transparent, 
            rgba(0, 255, 255, 0.2),
            transparent);
        transform: rotate(45deg);
        animation: hologramFlow 6s linear infinite;
    }
    
    @keyframes hologramFlow {
        0% { transform: rotate(45deg) translate(-50%, -50%); }
        100% { transform: rotate(45deg) translate(50%, 50%); }
    }
    
    /* Matrix-style particles background */
    .particles::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 1000 1000' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        opacity: 0.05;
        z-index: -1;
    }
    
    /* Glowing button animation */
    .cyber-button {
        background: linear-gradient(45deg, #00ffff, #00b3b3);
        border: none;
        border-radius: 30px;
        color: #002626;
        font-family: 'Orbitron', sans-serif;
        padding: 15px 30px;
        position: relative;
        overflow: hidden;
        transition: 0.5s;
        cursor: pointer;
        width: 100%;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a4a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #0ff;
        border-radius: 4px;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

 
st.markdown('<div class="particles"></div>', unsafe_allow_html=True)

#  Function to fetch movie poster from TMDB
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=239eed3f0fdaa8e7d1afbabb50c19183&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

#  Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

#  Load the movie data
with open('movies_dict.pkl', 'rb') as file:
    movies_dict = pickle.load(file)

with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

movies = pd.DataFrame(movies_dict)

st.markdown('<h1 class="cyber-title">MOVIE MATRIX 2.0</h1>', unsafe_allow_html=True)
 
st.sidebar.markdown(
    """
    <div style="border: 2px solid #0ff; border-radius: 15px; padding: 20px; margin: 10px;">
        <h3 style="font-family: 'Orbitron', sans-serif; color: #0ff;">CONTROL PANEL</h3>
    </div>
    """,
    unsafe_allow_html=True
)

selected_movie_name = st.sidebar.selectbox(
    "SELECT MOVIE PROFILE",
    movies['title'].values,
    key="movie_select"
)

 
if st.sidebar.button("🚀 INITIATE MOVIE SCAN", key="recommend_btn"):
    with st.spinner("〰️ DECRYPTING CINEMATIC PATTERNS ..."):
       
        progress_bar = st.empty()
        progress_bar.markdown("""
        <div style="position: relative; height: 10px; background: #1a1a4a; border-radius: 5px; overflow: hidden;">
            <div style="position: absolute; height: 100%; width: 100%; background: linear-gradient(90deg, 
                transparent, 
                #0ff,
                transparent);
                animation: scanLine 2s infinite linear;">
            </div>
        </div>
        <style>
        @keyframes scanLine {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        </style>
        """, unsafe_allow_html=True)
        
        time.sleep(2)   
        names, posters = recommend(selected_movie_name)
        progress_bar.empty()

         
        st.subheader(f"🔍 CINEMATIC MATCHES FOR: {selected_movie_name}")
        cols = st.columns(5)
        
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.markdown(
                    f"""
                    <div class="holographic-card">
                        <img src="{poster}" alt="{name}" style="
                            border-radius: 15px;
                            width: 100%;
                            height: 300px;
                            object-fit: cover;
                            margin-bottom: 15px;">
                        <h4 style="
                            margin: 0;
                            font-family: 'Orbitron', sans-serif;
                            color: #0ff;
                            font-size: 1.2rem;">
                            {name}
                        </h4>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        
        st.toast('✅ CINEMATIC PROFILE MATCHES FOUND!', icon='🎉')