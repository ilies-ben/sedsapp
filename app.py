import streamlit as st

def main():
    st.title("Application Streamlit avec Présentations")

    # Barre latérale
    st.sidebar.title("Menu")
    selected_option = st.sidebar.radio("Sélectionnez une option :", ["Présentation PowerPoint", "ML Training and Evaluation", "Autre"])

    # Affichage en fonction de l'option sélectionnée
    if selected_option == "ML Training and Evaluation":
        display_ml_slides()
    else:
        st.write("Sélectionnez une option valide dans la barre latérale.")

def display_ml_slides():
    st.header("ML Training and Evaluation")
    # Insérez ici le code pour afficher les slides sur MLOPS
    google_docs_link = "https://docs.google.com/presentation/d/e/2PACX-1vRdv6HySHTapEJOom0PL5kpZbh1qeqhqPm5A2TqydH3qEXdaEdXxp3jwikTs9qkGQ/pub?start=false&loop=false&delayms=10000"

    # Afficher l'iframe intégré pour afficher directement les slides
    st.components.v1.iframe(google_docs_link, height=600, scrolling=True)

if __name__ == "__main__":
    main()
