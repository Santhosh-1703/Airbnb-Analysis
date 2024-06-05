import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
import re
import plotly.express as px
import os
from PIL import Image


# Set the page configuration with the Airbnb icon
st.set_page_config(page_title='Airbnb Analysis', page_icon="D:\GUVI Class\Ab.png", layout="wide")

# Front Page Design
st.markdown("<h1 style='text-align: center; font-weight: bold; font-family: Comic Sans MS;'>Airbnb Analysis</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Hello Connections! 👋 Welcome to My Project Presentation 🙏</h3>", unsafe_allow_html=True)
selected_page = option_menu(
    menu_title='',
    options=["Home", "Dashboard", "Analysis Zone","About"],
    icons=["house", "clipboard2-data-fill","trophy","patch-question"],
    default_index=1,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "red","size":"cover", "width": "100"},
            "icon": {"color": "FF0000", "font-size": "25px"},
            "nav-link": {"font-size": "15px", "text-align": "center", "margin": "-2px", "--hover-color": "#FF0000"},
            "nav-link-selected": {"background-color": "#FF0000"}})

if selected_page == "About":
    st.header(" :Green[Project Conclusion]")
    tab1,tab2 = st.tabs(["Features","Connect with me on"])
    with tab1:
        st.header("This Streamlit application allows users to access and analyze data from MongoDB Sample dataset.", divider='rainbow')
        st.subheader("1.    Users can select specific criteria such as Country, Neighbourhood, Room Type, Bed Type, Host Response Time, and Availability to retrieve relevant data and analyze trends.")
        st.subheader("2.    Users can access slicers and filters to explore and visualize data in various chart types. They can customize the visualization based on their preferences.")
        st.subheader("3.    The analysis zone provides users with access to different chart types derived through Python scripting.")
        st.subheader("4.    They can explore advanced visualizations, including Scatter plots, and treemaps, to gain deeper insights into the Airbnb dataset.")
    with tab2:
             # Create buttons to direct to different website
            linkedin_button = st.button("LinkedIn")
            if linkedin_button:
                st.write("[Redirect to LinkedIn Profile > (https://www.linkedin.com/in/santhosh-r-42220519b/)](https://www.linkedin.com/in/santhosh-r-42220519b/)")

            email_button = st.button("Email")
            if email_button:
                st.write("[Redirect to Gmail > santhoshsrajendran@gmail.com](santhoshsrajendran@gmail.com)")

            github_button = st.button("GitHub")
            if github_button:
                st.write("[Redirect to Github Profile > https://github.com/Santhosh-1703](https://github.com/Santhosh-1703)")

elif selected_page == "Home":
    
    tab1,tab2 = st.tabs(["Airbnb Data Scrapping","  Applications and Libraries Used! "])
    with tab1:
        st.write(" Data scraping using a scraper tool helps organizations gather valuable insights about Total Performing Hotels, Customer Reviews, and Property details. By combining this data with information from social media, organizations can get a comprehensive view of their online presence and audience engagement. This approach enables data-driven decision-making and more effective content strategies.")
        st.write("[:open_book: Learn More  >](https://en.wikipedia.org/wiki/Airbnb)")
        if st.button("Click here to know about Airbnb"):
            col1, col2 = st.columns(2)
            col1.image(Image.open(r"D:\GUVI Class\abnb.jpg"), width=700)
            with col2:
                st.header(':white[Airbnb info]', divider='rainbow')
                st.subheader(":star: Airbnb, Inc. is an American company operating an online marketplace for short and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking.")
                st.subheader(":star: The Company was founded in **2008** by **Brian Chesky**, **Nathan Blecharczyk**, and **Joe Gebbia**. ")
                st.subheader(":star: Airbnb is a shortened version of its original name, AirBedandBreakfast.com. Airbnb is the most well-known company for short-term housing rentals. ")
                st.subheader(":star: In July 2014, Airbnb revealed design revisions to the site and mobile app and introduced a new logo. The logo, called the **Bélo**, is intended to serve as a symbol of belonging, and consists of four elements: a head which represents people, a location icon that represents place, a heart to symbolize love, and a letter 'A' to stand for the Company's name.")
    with tab2:
        st.subheader("  :bulb: MongoDB")
        st.subheader("  :bulb: Python")
        st.subheader("  :bulb: Numpy")
        st.subheader("  :bulb: PowerBI")

elif selected_page == "Dashboard":
    power_bi_report_url = "https://app.powerbi.com/reportEmbed?reportId=********************&autoAuth=true&ctid=00f9cda3-****-44e5-aa0b-aba3add6539f"
    st.markdown(f'<iframe title="Airbnb DashBoard" width="1600" height="700" src="{power_bi_report_url}" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)

elif selected_page == "Analysis Zone":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    uploaded_file = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])
    if uploaded_file is not None:
            file_extension = uploaded_file.name.split('.')[-1]
            try:
                if file_extension == 'csv':
                    df = pd.read_csv(uploaded_file, encoding='utf-8')
                elif file_extension in ['xlsx', 'xls']:
                    df = pd.read_excel(uploaded_file)
                elif file_extension == 'txt':
                    df = pd.read_csv(uploaded_file, delimiter='\t', encoding='utf-8')
                st.success("File uploaded successfully!")
            
                if st.button("Perform Data Wrangling Process"):
                    with st.spinner("Please wait for process completion..."):
                        df, success = data_wrangling(df)
                        if success:
                            st.success("Data wrangling process completed successfully!")
                        else:
                            st.error("Data wrangling process failed. Please check your file.")
        tab1, tab2,tab3,tab4,tab5 = st.tabs(['Property', 'Availability','Price','Host Reviews','Map'])
        with tab1:
            country_key = "country_multiselect_tab1"
            Country = st.sidebar.multiselect("Select Country", ["Select All"] + list(df["Country"].unique()), key=country_key)
            if "Select All" in Country:
                    Country = df["Country"].unique()

            # Filter neighborhoods based on the selected countries
            filtered_neighbourhoods = df[df["Country"].isin(Country)]["Neighbourhood"].unique()
            # Remove "Not Available" from the neighborhoods list
            filtered_neighbourhoods = [neighbourhood for neighbourhood in filtered_neighbourhoods if neighbourhood != "Not Available"]

            neighbourhood_key = "neighbourhood_multiselect_tab1"
            Neighbourhood = st.sidebar.multiselect("Select Neighbourhood", ["Select All"] + list(filtered_neighbourhoods), key=neighbourhood_key)
            if "Select All" in Neighbourhood:
                            Neighbourhood = filtered_neighbourhoods
                            
            # Filter the data based on selected countries and neighborhoods
            df_filtered = df[df["Country"].isin(Country) & df["Neighbourhood"].isin(Neighbourhood)]   

            # Plotting
            col1, col2 = st.columns(2)
            with col1:
                plt.figure(figsize=(10, 8))
                ax = sns.countplot(data=df_filtered, y='Property_type', order=df_filtered['Property_type'].value_counts().index[:10], palette='husl')
                # Annotate count values on bars
                for p in ax.patches:
                        ax.annotate(f'{int(p.get_width())}', (p.get_width() + 0.1, p.get_y() + p.get_height() / 2), ha='left', va='center')
                ax.set_title("Top 10 Property Types available")
                st.pyplot()
            
            with col2:
                # Group by 'Property_type' and count the occurrences
                 grouped_df = df_filtered['Property_type'].value_counts().reset_index(name='Number')

                 # Sort by Number in descending order and get the top 10
                top_property_types = grouped_df.sort_values(by='Number', ascending=False).head(10)

                # Set 'Property_type' as the index
                grouped_df.set_index('Property_type', inplace=True)

                # Create a pie chart using Plotly Express
                fig = px.pie(grouped_df,
                            names=grouped_df.index,  # Use the index as names (Property_type)
                            values='Number',
                            title='Top 10 Property Types by Number of Listings',
                            color_discrete_sequence=px.colors.qualitative.Bold)
                st.plotly_chart(fig)
            
            col3,col4 = st.columns(2)
            # Filter the data based on country and neighbourhood
            df_filtered = df[df["Country"].isin(Country) & df["Neighbourhood"].isin(Neighbourhood)]

            # Plotting
            col3, col4 = st.columns(2)
            with col3:
                # Total listings in each Roomtype
                plt.figure(figsize=(10, 8))
                ax = sns.countplot(data=df_filtered, x='Room_type', palette='pastel')
                for p in ax.patches:
                    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
                ax.set_title("Total Listings in each Room Type")
                st.pyplot()
            with col4:
                avg_price_df = df_filtered.groupby('Room_type')['Price'].mean().reset_index()
                avg_price_df['Price'] = avg_price_df['Price'].round(2)
                
                # Create a sunburst chart using Plotly Express
                fig = px.sunburst(avg_price_df,
                                path=['Room_type'],
                                values='Price',
                                title='Sunburst Chart for Room Type and Average Price')
                st.plotly_chart(fig)
        with tab2:
            col1,col2 = st.columns(2)
            with col1:
                df_filtered = df[df["Country"].isin(Country) & df["Neighbourhood"].isin(Neighbourhood)]

                # Calculate the availability percentage for each room type
                availability_percentage = df_filtered.groupby('Room_type')['Availability_30'].mean() * 100

                # Create a DataFrame for the pie chart
                availability_df = pd.DataFrame({'Room_type': availability_percentage.index, 'Availability_percentage': availability_percentage.values})

                # Plotting
                fig = px.pie(availability_df, 
                            names='Room_type', 
                            values='Availability_percentage', 
                            title='Rooms available for all 30 days',
                            labels={'Room_type': 'Room Type', 'Availability_percentage': 'Availability (%)'},
                            hole=0.1)

                st.plotly_chart(fig)
            with col2:
                df_filtered = df[df["Country"].isin(Country) & df["Neighbourhood"].isin(Neighbourhood)]

                # Calculate the availability percentage for each room type
                availability_percentage = df_filtered.groupby('Room_type')['Availability_60'].mean() * 100

                # Create a DataFrame for the pie chart
                availability_df = pd.DataFrame({'Room_type': availability_percentage.index, 'Availability_percentage': availability_percentage.values})

                # Plotting
                fig = px.pie(availability_df, 
                            names='Room_type', 
                            values='Availability_percentage', 
                            title='Rooms available for all 60 days',
                            labels={'Room_type': 'Room Type', 'Availability_percentage': 'Availability (%)'},
                            hole=0.1)

                st.plotly_chart(fig)
            col3,col4 = st.columns(2)
            with col3:
                df_filtered = df[df["Country"].isin(Country) & df["Neighbourhood"].isin(Neighbourhood)]

                # Calculate the availability percentage for each room type
                availability_percentage = df_filtered.groupby('Room_type')['Availability_90'].mean() * 100

                # Create a DataFrame for the pie chart
                availability_df = pd.DataFrame({'Room_type': availability_percentage.index, 'Availability_percentage': availability_percentage.values})

                # Plotting
                fig = px.pie(availability_df, 
                            names='Room_type', 
                            values='Availability_percentage', 
                            title='Rooms available for all 90 days',
                            labels={'Room_type': 'Room Type', 'Availability_percentage': 'Availability (%)'},
                            hole=0.1)

                st.plotly_chart(fig)
            with col4:
                df_filtered = df[df["Country"].isin(Country) & df["Neighbourhood"].isin(Neighbourhood)]

                # Calculate the availability percentage for each room type
                availability_percentage = df_filtered.groupby('Room_type')['Availability_365'].mean() * 100

                # Create a DataFrame for the pie chart
                availability_df = pd.DataFrame({'Room_type': availability_percentage.index, 'Availability_percentage': availability_percentage.values})

                # Plotting
                fig = px.pie(availability_df, 
                            names='Room_type', 
                            values='Availability_percentage', 
                            title='Rooms available for all 365 days',
                            labels={'Room_type': 'Room Type', 'Availability_percentage': 'Availability (%)'},
                            hole=0.1)

                st.plotly_chart(fig)
        with tab3:
            col11,col12 = st.columns(2)
            with col12:
                # Filter the data based on country and neighbourhood
                df_filtered = df[df["Country"].isin(Country) & df["Neighbourhood"].isin(Neighbourhood)]

                # Calculate the average price of room types in each country
                average_price = df.groupby(['Country', 'Room_type'])['Price'].mean().unstack()

                # Convert average_price to numeric (in case it's not already)
                average_price = average_price.apply(pd.to_numeric, errors='coerce')

                # Create a line plot using Plotly Express
                fig = px.line(average_price, 
                            x=average_price.index, 
                            y=average_price.columns, 
                            title='Average price of room types in each country',
                            labels={'index': 'Country', 'value': 'Price'})

                # Customize the layout
                fig.update_layout(xaxis_tickangle=-45)

                # Show the plot
                st.plotly_chart(fig)

            with col11:
                    country_df = df.groupby('Country', as_index=False)['Price'].mean()

                    # Create a scatter plot using Plotly Express
                    fig = px.scatter(data_frame=country_df,
                                    x='Country', y='Price',
                                    color='Country',
                                    size='Price',
                                    opacity=1,
                                    size_max=35,
                                    title='Average Listing Price in each Country')

                    # Customize the layout
                    fig.update_layout(xaxis_title='Country', yaxis_title='Average Price', xaxis_tickangle=-45)

                    # Show the plot
                    st.plotly_chart(fig)

                    from bokeh.plotting import figure
                    from bokeh.transform import dodge
                    from bokeh.models import Label

                    # Calculate the maximum price for each location (Top 30)
                    max_price_per_location = df.groupby('Country')['Price'].max().reset_index().sort_values(['Price'],ascending=False).rename(columns={'Price':'Max price'}).head(10)

                    # Calculate the minimum price for each location (Top 30)
                    min_price_per_location = df.groupby('Country')['Price'].min().reset_index().sort_values(['Price'],ascending=True).rename(columns={'Price':'Min price'}).head(10)

                    # Create a Bokeh figure
                    p = figure(x_range=max_price_per_location['Country'], title="Minimum and Maximum Price for each location",
                            toolbar_location=None, tools="")

                    # Add vertical bars for minimum price
                    min_bars = p.vbar(x=dodge('Country', -0.15, range=p.x_range), top='Min price', width=0.4, source=min_price_per_location,
                        color="red", legend_label="Minimum Price")

                    # Add vertical bars for maximum price
                    max_bars = p.vbar(x=dodge('Country',  0.15,  range=p.x_range), top='Max price', width=0.4, source=max_price_per_location,
                        color="green", legend_label="Maximum Price")

                    # Display the plot
                    st.bokeh_chart(p)
            with col12:
                avg_security_fee_per_location = df.groupby('Country')['Security_deposit'].mean().reset_index().sort_values(['Security_deposit'], ascending=False).rename(columns={'Security_deposit': 'Average Security Fee'}).head(10)

                # Calculate the average cleaning fee for each location (Top 10)
                avg_cleaning_fee_per_location = df.groupby('Country')['Cleaning_fee'].mean().reset_index().sort_values(['Cleaning_fee'], ascending=False).rename(columns={'Cleaning_fee': 'Average Cleaning Fee'}).head(10)

                # Create a Bokeh figure
                p = figure(x_range=avg_security_fee_per_location['Country'], title="Average Security & Cleaning Fees for each location",
                        toolbar_location=None, tools="")

                # Add vertical bars for average security fee
                avg_security_bars = p.vbar(x=dodge('Country', -0.15, range=p.x_range), top='Average Security Fee', width=0.4, source=avg_security_fee_per_location,
                                        color="blue", legend_label="Average Security Fee")

                # Add vertical bars for average cleaning fee
                avg_cleaning_bars = p.vbar(x=dodge('Country', 0.15, range=p.x_range), top='Average Cleaning Fee', width=0.4, source=avg_cleaning_fee_per_location,
                                        color="orange", legend_label="Average Cleaning Fee")

                # Display the plot
                st.bokeh_chart(p)
        with tab4:
            col1,col2 = st.columns(2)
            with col1:
                plt.figure(figsize=(10, 8))
                ax = sns.countplot(data=df, y=df.Host_name, order=df.Host_name.value_counts().index[:10], palette='pastel')
                # Annotate count values on bars
                for p in ax.patches:
                    ax.annotate(f'{int(p.get_width())}', (p.get_width() + 0.1, p.get_y() + p.get_height() / 2), ha='left',va='center')
                ax.set_title("Top 10 Hosts with Highest number of Listings")
                # Display the plot using Streamlit
                st.pyplot()
            with col2:
                # Group by 'Property_type' and count the occurrences
                grouped_df = df.groupby('Host_response_time').size().reset_index(name='Number')

                # Sort by Number in descending order and get the top 10
                top_property_types = grouped_df.sort_values(by='Number', ascending=False).head(10)

                # Create a pie chart using Plotly Express
                fig = px.pie(top_property_types,
                            names='Host_response_time',
                            values='Number',
                            title='Host Response Time by diff. Hosts',
                            color_discrete_sequence=px.colors.qualitative.Bold)
                st.plotly_chart(fig)
                # Group by 'Property_type' and count the occurrences
                grouped_df = df.groupby('Cancellation_policy').size().reset_index(name='Number')

                # Sort by Number in descending order and get the top 10
                top_property_types = grouped_df.sort_values(by='Number', ascending=False).head(10)

                # Create a pie chart using Plotly Express
                fig = px.pie(top_property_types,
                            names='Cancellation_policy',
                            values='Number',
                            title='Cancellation Policy for diff. hotels',
                            color_discrete_sequence=px.colors.qualitative.Safe)
                st.plotly_chart(fig)
            # BLANK SPACE
            st.markdown("#   ")
            st.markdown("#   ")
            with col1:
                top_neighborhoods = df.groupby('Neighbourhood')['Review_count'].sum().nlargest(10).index

                # Filter the DataFrame to include only the top neighborhoods
                df_top_neighborhoods = df[df['Neighbourhood'].isin(top_neighborhoods)]

                # Create a custom color palette
                custom_palette = sns.color_palette("coolwarm")[:len(top_neighborhoods)]

                # Create the count plot
                plt.figure(figsize=(10, 8))
                ax = sns.countplot(data=df_top_neighborhoods, y='Neighbourhood', order=top_neighborhoods, palette=custom_palette)
                for p in ax.patches:
                        ax.annotate(f'{int(p.get_width())}', (p.get_width() + 0.1, p.get_y() + p.get_height() / 2), ha='left',va='center')
                ax.set_title("Top 10 Neighbourhood with Highest Review Counts")

                # Display the plot using Streamlit
                st.pyplot()
        with tab5:
            # GETTING USER INPUTS
            prop = st.sidebar.multiselect('Select Property_type',sorted(df.Property_type.unique()),sorted(df.Property_type.unique()))
            room = st.sidebar.multiselect('Select Room_type',sorted(df.Room_type.unique()),sorted(df.Room_type.unique()))
            country = st.sidebar.multiselect('Select a Country',sorted(df.Country.unique()),sorted(df.Country.unique()))
            price = st.slider('Select Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))
    
            # CONVERTING THE USER INPUT INTO QUERY
            query = f'Country in {country} & Room_type in {room} & Property_type in {prop} & Price >= {price[0]} & Price <= {price[1]}'

            country_df = df.query(query).groupby('Country',as_index=False)['Price'].mean()
            fig = px.scatter_geo(data_frame=country_df,
                                        locations='Country',
                                        color= 'Price', 
                                        hover_data=['Price'],
                                        locationmode='country names',
                                        size='Price',
                                        title= 'Avg Price in each Country',
                                        color_continuous_scale='agsunset'
                                )
            st.plotly_chart(fig,use_container_width=True)

            # BLANK SPACE
            st.markdown("#   ")
            st.markdown("#   ")
            # AVG AVAILABILITY IN COUNTRIES SCATTERGEO
            country_df = df.query(query).groupby('Country',as_index=False)['Availability_365'].mean()
            country_df.Availability_365 = country_df.Availability_365.astype(int)
            fig = px.scatter_geo(data_frame=country_df,
                                            locations='Country',
                                            color= 'Availability_365', 
                                            hover_data=['Availability_365'],
                                            locationmode='country names',
                                            size='Availability_365',
                                            title= 'Avg Availability in each Country',
                                            color_continuous_scale='agsunset')
            st.plotly_chart(fig,use_container_width=True)
