# 🎬 Movie Matrix 2.0 🌌

**A Cyberpunk-themed Movie Recommendation System**  
*Where Machine Learning Meets Cinematic Futurism*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.34.0-FF4B4B?logo=streamlit)](https://streamlit.io)
 

![Movie Matrix Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGZ1cXhqNDN4dWJ3ejB4Y2Rmb3J6aG0wZ2h5cWt4Z3F6dHd2cXJpbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ICOgUNjpvO0PC/giphy.gif)

## 🌟 Features

### 🤖 Core Engine
- **Content-Based Filtering** using movie metadata
- **NLP Processed** tags from genres, cast, crew, and overviews
- **Cosine Similarity** for recommendations
- **5000+ Movie Database** from TMDB
- **Porter Stemming** for text normalization

### 🖥 Streamlit UI
- **Cyberpunk Styling** with neon animations
- **Real-time TMDB Poster Integration**
- **Holographic Movie Cards**
- **Animated Loading Sequences**
- **Interactive Control Panel**
- **Responsive Layout**

## 🧠 System Architecture
```mermaid
graph TD
    A[TMDB Dataset] --> B[Data Preprocessing]
    B --> C[Feature Engineering]
    C --> D[NLP Pipeline]
    D --> E[Similarity Matrix]
    E --> F[Streamlit UI]
    F --> G[User Interaction]
    G --> H[Live Recommendations]
