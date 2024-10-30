# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:35:50 2024

@author: DELL
"""

import streamlit as st
import random



# Titre de l'application
st.title("ENSAE-ESMT Ultimate Treasure Hunt")

# Sélection de l'épreuve
step = st.selectbox("Sélectionnez l'épreuve :", ["Steve Jobs", "Colonel Sanders", "David Goggins", "Taj Mahal", "Giving Directions", "I, Robot"])

# Affichage conditionnel en fonction de l’épreuve choisie
if step == "Giving Directions":
    
    # Layout pour les 4 questions dans Step3, 2 lignes et 2 colonnes
    col1, col2 = st.columns(2)
    with col1:
        response1 = st.selectbox("Speaker A :",[
    "hospital",
    "police station",
    "supermarket",
    "book shop",
    "bus station",
    "cinema",
    "theatre",
    "underground station",
    "café",
    "Italian restaurant",
    "shop",
    "post office",
    "library",
    "museum",
    "factory"
]
)
        response3 = st.selectbox("Speaker C :",[
    "hospital",
    "police station",
    "supermarket",
    "book shop",
    "bus station",
    "cinema",
    "theatre",
    "underground station",
    "café",
    "Italian restaurant",
    "shop",
    "post office",
    "library",
    "museum",
    "factory"
])
    with col2:
        response2 = st.selectbox("Speaker B :", [
    "hospital",
    "police station",
    "supermarket",
    "book shop",
    "bus station",
    "cinema",
    "theatre",
    "underground station",
    "café",
    "Italian restaurant",
    "shop",
    "post office",
    "library",
    "museum",
    "factory"
])
        response4 = st.selectbox("Speaker D :", [
    "hospital",
    "police station",
    "supermarket",
    "book shop",
    "bus station",
    "cinema",
    "theatre",
    "underground station",
    "café",
    "Italian restaurant",
    "shop",
    "post office",
    "library",
    "museum",
    "factory"
])
else:
    # Pour les autres épreuves, seulement 2 questions sont affichées
    response1 = st.selectbox("Choisissez la réponse de la question 1 :", ["A", "B", "C", "D"])
    response2 = st.selectbox("Choisissez la réponse de la question 2 :", ["A", "B", "C", "D"])

# Bouton de confirmation et logique de lieu
if st.button("Confirmer"):
    if step == "Giving Directions":
        # Exemple de logique pour le Step3 avec les 4 questions
        if response1 == "post office" and response2 ==  "underground station" and response3 == "cinema" and response4 == "bus station":
            st.success("Lieu : Outside 1")
        else:
            random_place = random.choice(["FL1", "FL2", "FL3"])
            st.success(f"Lieu : {random_place}")


    if step == "Steve Jobs":
        # Exemple de logique pour le Step3 avec les 4 questions
        if response1 == "B" and response2 == "B":
            st.success("Lieu : Laser maze")
        else:
            random_place = random.choice(["FL1", "FL2", "FL3"])
            st.success(f"Lieu : {random_place}")


    if step == "Colonel Sanders":
        # Exemple de logique pour le Step3 avec les 4 questions
        if response1 == "B" and response2 == "C":
            st.success("Lieu : Outside 2")
        else:
            random_place = random.choice(["FL1", "FL2", "FL3"])
            st.success(f"Lieu : {random_place}")


    if step == "David Goggins":
        # Exemple de logique pour le Step3 avec les 4 questions
        if response1 == "C" and response2 == "D":
            st.success("Lieu : The floor is lava")
        else:
            random_place = random.choice(["FL1", "FL2", "FL3"])
            st.success(f"Lieu : {random_place}")
 

    if step == "Taj Mahal":
        # Exemple de logique pour le Step3 avec les 4 questions
        if response1 == "C" and response2 == "B":
            st.success("Lieu : Twister")
        else:
            random_place = random.choice(["FL1", "FL2", "FL3"])
            st.success(f"Lieu : {random_place}")

    if step == "I, Robot":
        # Exemple de logique pour le Step3 avec les 4 questions
        if response1 == "C" and response2 == "C":
            st.success("Lieu : Outside 3")
        else:
            random_place = random.choice(["FL1", "FL2", "FL3"])
            st.success(f"Lieu : {random_place}")
 
 
            
