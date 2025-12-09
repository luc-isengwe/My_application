import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit.components.v1 as components

#########################################################################################################################################################
#                                                             FIRST FUNCTION
#########################################################################################################################################################

def X1(n):
    df1 = pd.DataFrame()

    for index in range(1, n+1):
        url = f'https://dakar-auto.com/senegal/voitures-4?&page=1{index}'

        res = get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div', class_='listings-cards__list-item mb-md-3 mb-3')

        data1 = []
        for container1 in containers:
            try:
                info1 = container1.find('h2', 'listing-card__header__title mb-md-2 mb-0').text.strip().split()
                brand = info1[0]
                year = info1[-1]
                price = "".join(container1.find(
                    'h3', "listing-card__header__price font-weight-bold text-uppercase mb-0"
                ).text.strip().split()).replace('FCFA', '')

                adress1 = container1.find('div', 'col-12 entry-zone-address').text.strip().split()
                adress = ''
                for a in adress1:
                    adress = adress + a + ' '
                adress = adress.strip()

                gen_inf1 = container1.find_all('li', 'listing-card__attribute list-inline-item')
                gearbox = gen_inf1[2].text.strip()
                kilometerage = gen_inf1[1].text.replace(' km', '').strip()
                fuel = gen_inf1[3].text.strip()
                owner = container1.find('p', 'time-author m-0').text.strip().replace('Par ', '')

                dic1 = {
                    "brand": brand,
                    "year": year,
                    "price": price,
                    "adress": adress,
                    "gearbox": gearbox,
                    "kilometerage": kilometerage,
                    "fuel": fuel,
                    "owner": owner
                }

                data1.append(dic1)
            except:
                pass

        DF1 = pd.DataFrame(data1)
        df1 = pd.concat([df1, DF1], axis=0).reset_index(drop=True)

    string_cols = ["brand", "adress", "gearbox", "fuel", "owner"]
    for col in string_cols:
        df1[col] = df1[col].astype(str)
        df1[col] = df1[col].replace(["", " ", "nan", "None"], pd.NA)
        df1[col] = df1[col].fillna(df1[col].mode()[0])

    numeric_cols = ["year", "price", "kilometerage"]
    for col in numeric_cols:
        df1[col] = pd.to_numeric(df1[col], errors='coerce')
        df1[col] = df1[col].fillna(df1[col].mean())

    df1.drop_duplicates(inplace=True)
    return df1


##########################################################################################################################################################
#                                                               SECOND FUNCTION
##########################################################################################################################################################

def X2(n1):
    df2 = pd.DataFrame()

    for index in range(1, n1+1):
        url = f'https://dakar-auto.com/senegal/motos-and-scooters-3?&page={index}'
        res = get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div', class_='listings-cards__list-item mb-md-3 mb-3')

        data2 = []
        for container1 in containers:
            try:
                info1 = container1.find('h2', class_='listing-card__header__title mb-md-2 mb-0').text.strip().split()
                brand = info1[0]
                year = info1[-1]
                price = "".join(container1.find('h3', class_="listing-card__header__price font-weight-bold text-uppercase mb-0").text.strip().split()).replace('FCFA', '')

                adress1 = container1.find('div', class_='col-12 entry-zone-address').text.strip().split()
                adress = ''
                for a in adress1:
                    adress = adress + a + ' '
                adress = adress.strip()

                gen_inf1 = container1.find_all('li', class_='listing-card__attribute list-inline-item')
                kilometerage = gen_inf1[1].text.replace(' km','').strip()
                owner = container1.find('p', class_='time-author m-0').text.strip().replace('Par ', '')

                dic2 = {
                    "brand": brand,
                    "year": year,
                    "price": price,
                    "adress": adress,
                    "kilometerage": kilometerage,
                    "owner": owner
                }

                data2.append(dic2)
            except:
                pass

        DF2 = pd.DataFrame(data2)
        df2 = pd.concat([df2, DF2], axis=0).reset_index(drop=True)

    string_cols = ["brand", "adress", "owner"]
    for col in string_cols:
        df2[col] = df2[col].astype(str)
        df2[col] = df2[col].replace(["", " ", "nan", "None"], pd.NA)
        df2[col] = df2[col].fillna(df2[col].mode()[0])

    numeric_cols = ["year", "price", "kilometerage"]
    for col in numeric_cols:
        df2[col] = pd.to_numeric(df2[col], errors='coerce')
        df2[col] = df2[col].fillna(df2[col].mean())

    df2.drop_duplicates(inplace=True)
    return df2

#############################################################################################################################################################
#                                                                     THIRD FUNCTION
#############################################################################################################################################################

def X3(n2):
    df3 = pd.DataFrame()

    for index in range(1, n2+1):
        url = f'https://dakar-auto.com/senegal/location-de-voitures-19?&page={index}'
        res = get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div', class_='listings-cards__list-item mb-md-3 mb-3')

        data3 = []
        for container1 in containers:
            try:
                info1 = container1.find('h2', class_='listing-card__header__title mb-md-2 mb-0').text.strip().split()
                brand = info1[0]
                year = info1[-1]
                price = "".join(container1.find('h3', class_="listing-card__header__price font-weight-bold text-uppercase mb-0").text.strip().split()).replace('FCFA', '')

                adress1 = container1.find('div', class_='col-12 entry-zone-address').text.strip().split()
                adress = ''
                for a in adress1:
                    adress = adress + a + ' '
                adress = adress.strip()

                owner = container1.find('p', class_='time-author m-0').text.strip().replace('Par ', '')

                dic3 = {
                    "brand": brand,
                    "year": year,
                    "price": price,
                    "adress": adress,
                    "owner": owner
                }

                data3.append(dic3)

            except:
                pass

        DF3 = pd.DataFrame(data3)
        df3 = pd.concat([df3, DF3], axis=0).reset_index(drop=True)

    string_cols = ["brand", "adress", "owner"]
    for col in string_cols:
        df3[col] = df3[col].astype(str)
        df3[col] = df3[col].replace(["", " ", "nan", "None"], pd.NA)
        df3[col] = df3[col].fillna(df3[col].mode()[0])

    numeric_cols = ["year", "price"]
    for col in numeric_cols:
        df3[col] = pd.to_numeric(df3[col], errors='coerce')
        df3[col] = df3[col].fillna(df3[col].mean())

    df3.drop_duplicates(inplace=True)
    return df3


######################################################################################################################################################################
#                                                                CUSTOM STYLE (COLORS)
######################################################################################################################################################################

custom_style = """
<style>
    :root { --main-blue: #005CFF; }

    .centered { text-align: center !important; }

    .cta-card {
        border: 2px solid #005CFF;
        border-radius: 15px;
        padding: 10px;
        text-align: center;
        cursor: pointer;
        transition: 0.3s;
        background-color: #F8F9FA;
    }

    .cta-card:hover {
        transform: scale(1.03);
        background-color: #E6F0FF;
    }

    .cta-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 10px;
    }

    .cta-title {
        font-size: 20px;
        font-weight: bold;
        margin-top: 10px;
        color: #005CFF;
    }
</style>

"""
st.markdown(custom_style, unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("Menu")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Option"]
)


if page == "Option":
    choix = st.sidebar.selectbox(
        "Choose an option",
        ["Scrape data using BeautifulSoup", "Download scraped data", "Dashboard of data", "Evaluate the application"]
    )

# HOME PAGE
if page == "Home":
    st.markdown("<h1 class='centered'> APP_SCRAPE_DATA!</h1>", unsafe_allow_html=True)      # Name of application
    st.markdown("<p class='centered'>Look on your left if you want to start scraping.</p>", unsafe_allow_html=True)
    st.markdown("""
    ### How to use this application

    This application allows you to **scrape vehicle data** from the website *dakar-auto.com*,  
    analyse it, download it, and visualise it through interactive dashboards.

    #### Here we have different steps usage guide:

    **1. Scrape the data**
    - Go to **Option and clic to Scrape data using BeautifulSoup**
    - Choose a category:
        - Cars  
        - Motorcycles  
        - Car rentals  
    - Enter the number of pages you want to scrape  
    - Validate and wait until the scraping is complete  
    - Preview the collected data and download it if needed  

    **2. Download previously saved scraped data**
    - Go to **Option and then Download scraped data**
    - Click the button corresponding to the dataset you want  

    **3. Visualise the data**
    - Go to **Option and then Dashboard of data**
    - You will get:
        - Top 5 most frequent brands  
        - Price evolution by year  
        - Separate dashboards for cars, motorcycles, and rentals  

    **4. Evaluate the application**
    - Go to **Option and then Evaluate the application**
    - Choose the evaluation tool you want (Google Form or Kobo Collect)

    ---
    """, unsafe_allow_html=True)



# OPTION PAGE
if page == "Option":
    st.title("Options page")
    st.write(f"You have chosen : **{choix}**")

    # SCRAPING SECTION
    if choix == "Scrape data using BeautifulSoup":
        st.subheader("Select what you want to scrape:")

        col1, col2, col3 = st.columns(3)

        car_img = "https://cdn.pixabay.com/photo/2012/05/29/00/43/car-49278_1280.jpg"
        moto_img = "https://cdn.pixabay.com/photo/2016/11/29/02/08/biker-1867055_1280.jpg"
        loc_img = "https://cdn.pixabay.com/photo/2015/01/19/13/51/car-rental-604019_1280.jpg"

        with col1:
            st.markdown(
                f"""
                <div class='cta-card' onclick="window.location.href='?cars=true'">
                    <img src='{car_img}' class='cta-img'>
                    <div class='cta-title'>Cars</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class='cta-card' onclick="window.location.href='?moto=true'">
                    <img src='{moto_img}' class='cta-img'>
                    <div class='cta-title'>Motorcycles</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div class='cta-card' onclick="window.location.href='?loc=true'">
                    <img src='{loc_img}' class='cta-img'>
                    <div class='cta-title'>Car rentals</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ACTIONS FOR CARS
        if st.button:
            st.write("### Enter number of pages to scrape for **cars**:")
            number_pages = st.number_input("Number of pages:", min_value=1, step=1, key="num_pages_cars")

            if st.button("Validate number of pages", key="valider_cars"):
                with st.spinner("Scraping in progress..."):
                    try:
                        df_cars = X1(number_pages)
                        st.session_state['df_cars'] = df_cars
                        st.session_state['cars_scraped'] = True
                        st.success("Scraping completed!")
                    except Exception as e:
                        st.session_state['cars_scraped'] = False
                        st.error(f"Scraping error: {e}")

            if st.session_state.get('cars_scraped', False):
                df_cars = st.session_state.get('df_cars', pd.DataFrame())
                if not df_cars.empty:
                    st.subheader("Preview of retrieved data")
                    st.dataframe(df_cars)

                    csv = df_cars.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download data (CSV)",
                        data=csv,
                        file_name="cars_scraped.csv",
                        mime="text/csv",
                        key="download_cars"
                    )
                else:
                    st.warning("The DataFrame is empty — check the URL.")

        # MOTORCYCLE SCRAPING
        if 'moto_scraped' not in st.session_state:
            st.session_state['moto_scraped'] = False

        if st.button:
            st.write("### Enter number of pages to scrape for **motorcycles**:")

            number_pages_moto = st.number_input(
                "Number of pages:",
                min_value=1,
                step=1,
                key="num_pages_moto"
            )

            if st.button("Validate number of pages (motorcycles)", key="valider_moto"):
                with st.spinner("Motorcycle scraping in progress..."):
                    try:
                        df_moto = X2(number_pages_moto)
                        st.session_state['df_moto'] = df_moto
                        st.session_state['moto_scraped'] = True
                        st.success("Motorcycle scraping completed!")
                    except Exception as e:
                        st.session_state['moto_scraped'] = False
                        st.error(f"Motorcycle scraping error: {e}")

            if st.session_state.get('moto_scraped', False):
                df_moto = st.session_state.get('df_moto', pd.DataFrame())
                if not df_moto.empty:
                    st.subheader("Preview of motorcycle data")
                    st.dataframe(df_moto)

                    csv_moto = df_moto.to_csv(index=False).encode('utf-8')

                    st.download_button(
                        label="Download motorcycle data (CSV)",
                        data=csv_moto,
                        file_name="motorcycles_scraped.csv",
                        mime="text/csv",
                        key="download_moto"
                    )
                else:
                    st.warning("No data retrieved — verify the source.")

        # LOCATION SCRAPING
        if 'loc_scraped' not in st.session_state:
            st.session_state['loc_scraped'] = False

        if st.button:
            st.write("### Enter number of pages to scrape for **car rentals**:")

            number_pages_loc = st.number_input(
                "Number of pages:",
                min_value=1,
                step=1,
                key="num_pages_loc"
            )

            if st.button("Validate number of pages (rentals)", key="valider_loc"):
                with st.spinner("Car rental scraping in progress..."):
                    try:
                        df_loc = X3(number_pages_loc)
                        st.session_state['df_loc'] = df_loc
                        st.session_state['loc_scraped'] = True
                        st.success("Car rental scraping completed!")
                    except Exception as e:
                        st.session_state['loc_scraped'] = False
                        st.error(f"Car rental scraping error: {e}")

            if st.session_state.get('loc_scraped', False):
                df_loc = st.session_state.get('df_loc', pd.DataFrame())
                if not df_loc.empty:
                    st.subheader("Preview of car rental data")
                    st.dataframe(df_loc)

                    csv_loc = df_loc.to_csv(index=False).encode('utf-8')

                    st.download_button(
                        label="Download car rental data (CSV)",
                        data=csv_loc,
                        file_name="rentals_scraped.csv",
                        mime="text/csv",
                        key="download_loc"
                    )
                else:
                    st.warning("No data retrieved — verify the source.")

###################################################################################################################################################################
#                                                                   DOWNLOAD SCRAPED DATA
###################################################################################################################################################################

    elif choix == 'Download scraped data':

        st.subheader("Download your scraped data")

        if st.button("Download car data"):
            try:
                voitures = pd.read_csv('/home/luc-lintos/Documents/Homework&Assignment/Data Collection/My_first_app/Data/voitures.csv')
                csv_voitures = voitures.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Click to download car CSV",
                    data=csv_voitures,
                    file_name="voitures.csv",
                    mime="text/csv",
                    key="dl_voiture"
                )
            except:
                st.error("voitures.csv file not found.")

        if st.button("Download motorcycle data"):
            try:
                motos_and_scooters = pd.read_csv('/home/luc-lintos/Documents/Homework&Assignment/Data Collection/My_first_app/Data/motos-and-scooters.csv')
                csv_moto = motos_and_scooters.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Click to download motorcycle CSV",
                    data=csv_moto,
                    file_name="motos_and_scooters.csv",
                    mime="text/csv",
                    key="dl_moto"
                )
            except:
                st.error("motos-and-scooters.csv file not found.")

        if st.button("Download rental data"):
            try:
                location_de_voitures = pd.read_csv('/home/luc-lintos/Documents/Homework&Assignment/Data Collection/My_first_app/Data/location-de-voitures.csv')
                csv_loc = location_de_voitures.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Click to download rental CSV",
                    data=csv_loc,
                    file_name="location_de_voitures.csv",
                    mime="text/csv",
                    key="dl_location"
                )
            except:
                st.error("location-de-voitures.csv file not found.")

#####################################################################################################################################################
#                                                               THIRD PART OF THE CODE
#####################################################################################################################################################

                                            # ----------------------------------------------------------
                                            #                     DASHBOARD OF THE DATA
                                            # ----------------------------------------------------------

    elif choix == "Dashboard of data":

        st.title("Dashboard of the scraped data")

        # Verify which data is disponible
        cars_available = 'df_cars' in st.session_state and not st.session_state['df_cars'].empty
        moto_available = 'df_moto' in st.session_state and not st.session_state['df_moto'].empty
        loc_available  = 'df_loc'  in st.session_state and not st.session_state['df_loc'].empty

        if not (cars_available or moto_available or loc_available):
            st.warning("No scraped data found. Please scrape data first.")
            st.stop()

                                                # -------------------------------------------------------
                                                #               DASHBOARD VEHICLES (CARS)
                                                # -------------------------------------------------------
        if cars_available:
            st.subheader("Dashboard — Cars")

            df1 = st.session_state['df_cars']

            col1, col2 = st.columns(2)

            with col1:
                plot1 = plt.figure(figsize=(11,7))
                plt.bar(df1.brand.value_counts()[:5].index, df1.brand.value_counts()[:5].values)
                plt.title("Top 5 most frequent car brands")
                plt.xlabel("Brand")
                st.pyplot(plot1)

            with col2:
                plot2 = plt.figure(figsize=(11,7))
                sns.lineplot(data=df1, x="year", y="price")
                plt.title("Price variation of cars by year")
                st.pyplot(plot2)

        st.markdown("---")

                                            # -------------------------------------------------------
                                            #               DASHBOARD MOTORCYCLES
                                            # -------------------------------------------------------
        if moto_available:
            st.subheader("Dashboard — Motorcycles")

            df2 = st.session_state['df_moto']

            col3, col4 = st.columns(2)

            with col3:
                plot3 = plt.figure(figsize=(11,7))
                plt.bar(df2.brand.value_counts()[:5].index, df2.brand.value_counts()[:5].values)
                plt.title("Top 5 most frequent motorcycle brands")
                plt.xlabel("Brand")
                st.pyplot(plot3)

            with col4:
                plot4 = plt.figure(figsize=(11,7))
                sns.lineplot(data=df2, x="year", y="price")
                plt.title("Price variation of motorcycles by year")
                st.pyplot(plot4)

        st.markdown("---")

                                                # -------------------------------------------------------
                                                #               DASHBOARD CAR RENTALS
                                                # -------------------------------------------------------
        if loc_available:
            st.subheader("Dashboard — Car Rentals")

            df3 = st.session_state['df_loc']

            col5, col6 = st.columns(2)

            with col5:
                plot5 = plt.figure(figsize=(11,7))
                plt.bar(df3.brand.value_counts()[:5].index, df3.brand.value_counts()[:5].values)
                plt.title("Top 5 brands in car rentals")
                plt.xlabel("Brand")
                st.pyplot(plot5)

            with col6:
                plot6 = plt.figure(figsize=(11,7))
                sns.lineplot(data=df3, x="year", y="price")
                plt.title("Price variation in car rentals by year")
                st.pyplot(plot6)




#####################################################################################################################################################
#                                                               FEEDBACK SECTION
#####################################################################################################################################################

    if choix == "Evaluate the application":
        st.subheader("Give your feedback")

        col1, col2 = st.columns(2)

        with col1:
            st.link_button("Google Form", "https://forms.gle/haXcnQmxEhBheKXL8")

        with col2:
            st.link_button("Kobo Collect", "https://ee.kobotoolbox.org/x/fsZB531H")
