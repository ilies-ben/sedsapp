import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import psutil
import time
def get_process_list():
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        process_info = proc.info
        process_list.append(process_info)
        if len(process_list) == 10:  # Limite à 10 processus
            break
    return process_list

def display_simulation():
    st.header("Simulation en temps réel")
    progress_bar = st.progress(0)
    st.header("Liste gestionnaire des taches")
    process_list = get_process_list()


    # Fonction pour obtenir l'utilisation des ressources par processus
    def get_process_resource_usage(process_name):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                return 1  # Utilisation de la ressource détectée
        return 0  # Aucune utilisation de la ressource détectée

    # Fonction pour obtenir la plus haute utilisation des ressources
    def get_highest_resource_usage():
        
        high_usage_processes = ['X.exe', 'photoshop.exe', 'CuraEngine.exe']
        medium_usage_processes = ['designer.exe', 'Chrome.exe']
        low_usage_processes = ['WINWORD.EXE', 'EXCEL.EXE', 'Code.exe']

        highest_usage = 'a'  # Par défaut, aucune ressource en cours d'utilisation

        for process in high_usage_processes:
            if get_process_resource_usage(process) > 0:
                highest_usage = 'e'
                break

        if highest_usage == 'a':
            for process in medium_usage_processes:
                if get_process_resource_usage(process) > 0:
                    highest_usage = 'd'
                    break

        if highest_usage == 'a':
            for process in low_usage_processes:
                if get_process_resource_usage(process) > 0:
                    highest_usage = 'b'
                    break

        return highest_usage

    # Simulation du mode Smart
    if st.button("Démarrer la simulation"):
        with st.empty():
            for _ in range(10):  # Simule 10 cycles
                resource_usage = get_highest_resource_usage()
                if resource_usage == 'b':
                    progress_value = 30
                elif resource_usage == 'd':
                    progress_value = 60
                elif resource_usage == 'e':
                    progress_value = 90
                progress_bar.progress(progress_value)
                time.sleep(2)  # Pause de 2 secondes entre chaque cycle
    for process in process_list:
       st.write(process)
    st.title("Evaluation:")
    st.write("Polynomial regression: R²= 0.817 , RMSE=8.947 ")
    st.write("Simple regression R²= 0.731 ,RMSE=9.739")
    st.write("K-means : Davies-Bouldin = 0.741 ")
def main():
    st.title("SEDS Project Application Streamlit")

    # Barre latérale
    st.sidebar.title("Menu")
    selected_option = st.sidebar.radio("Sélectionnez une option :", ["Présentation de théme", "Présentation MLOPS" ,"Data Pre-processing", "Simulation en temp reél"])

    # Affichage en fonction de l'option sélectionnée
    if selected_option == "Présentation de théme":
        display_ml_slides()
    elif selected_option == "Data Pre-processing":
        display_data_preprocessing()
    elif selected_option =="Présentation MLOPS":
        display_mlops_slides()
    elif selected_option == "Simulation en temp reél":
        display_simulation()
    else:
        st.write("Sélectionnez une option valide dans la barre latérale.")


def display_ml_slides():
    st.header("Présentation de théme")
    # Insérez ici le code pour afficher les slides sur MLOPS
    google_docs_link = "https://docs.google.com/presentation/d/e/2PACX-1vRdv6HySHTapEJOom0PL5kpZbh1qeqhqPm5A2TqydH3qEXdaEdXxp3jwikTs9qkGQ/embed?start=false&loop=false&delayms=3000"
    st.components.v1.iframe(google_docs_link, height=800, scrolling=True)
def display_mlops_slides():
    st.header("MLOPS Introduction:")
    # Insérez ici le code pour afficher les slides sur MLOPS
    google_docs_link = "https://docs.google.com/presentation/d/e/2PACX-1vQJ6huLehiVsR3FhWBpRixDgvh9s2ZGINE9E2jkdJKAdqDa12LKkQ5VfAf6h9MouRBGt2sZH_THxfj6/embed?start=false&loop=false&delayms=3000"
    st.components.v1.iframe(google_docs_link, height=800, scrolling=True)

def display_data_preprocessing():
    st.header("Data Pre-processing")
    # Read the CSV file into a DataFrame
    df = pd.read_csv("dataset1.csv")
    st.subheader("Before Pre-processing")
    st.write("Head of the DataFrame:")
    st.write(df.head())
    st.write("Info about the DataFrame:")
    st.write(df.info())

    # Boxplot for "Consommation RAM lancement"
    st.subheader("Boxplot for Consommation RAM lancement")
    fig, ax = plt.subplots()
    ax.boxplot(df["Consommation RAM lancement"])
    plt.title("Consommation RAM lancement")
    st.pyplot(fig)

# Scatter plot pour "Consommation RAM lancement" vs "Consommation processeur lancement"
    st.subheader("Scatter Plot : Consommation RAM lancement vs Consommation processeur lancement")
    fig, ax = plt.subplots()
    ax.scatter(df["Consommation RAM lancement"], df["Consommation processeur lancement"])
    plt.title("Consommation RAM lancement vs Consommation processeur lancement")
    st.pyplot(fig)


    # Read the CSV file into a DataFrame
    df = pd.read_csv("dataset.csv")
    st.subheader("After Pre-processing")
    st.write(" suppression des valeurs manquantes:df = df.dropna() ")
    st.write(" Supprimez les doublons")
    st.write(" df = df.drop_duplicates()")
    st.write("  remove outliers")
    st.write(" for col in Consommation RAM lancement, Consommation processeur lancement: df = df[~is_outlier(df, col)]  # Filter out rows with outliers ")
    st.write("Head of the DataFrame:")
    st.write(df.head())
    st.write("Info about the DataFrame:")
    st.write(df.info())

    # Boxplot for "Consommation RAM lancement"
    st.subheader("Boxplot for Consommation RAM lancement")
    fig, ax = plt.subplots()
    ax.boxplot(df["Consommation RAM lancement"])
    plt.title("Consommation RAM lancement")
    st.pyplot(fig)

# Scatter plot pour "Consommation RAM lancement" vs "Consommation processeur lancement"
    st.subheader("Scatter Plot : Consommation RAM lancement vs Consommation processeur lancement")
    fig, ax = plt.subplots()
    ax.scatter(df["Consommation RAM lancement"], df["Consommation processeur lancement"])
    plt.title("Consommation RAM lancement vs Consommation processeur lancement")
    st.pyplot(fig)


if __name__ == "__main__":
    main()


