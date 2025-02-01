import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px

#streamlit Part

st.set_page_config(page_title="Airbnb | Holiday rentals, cabins, beach houses & more", page_icon="D:\Air_bnb\Airbnb Logo.png",layout='wide')

# Set background image URL (you can replace this with your image URL)
background_image_url = "https://skift.com/wp-content/uploads/2023/10/1200x800-Airbnb-v2.png"  

# Custom CSS to set background image for the entire page
st.markdown(f"""
    <style>
        /* Background and page styling */
        body {{
            background-image: url("{background_image_url}");
            background-size: cover;  /* Ensures the image covers the entire page */
            background-repeat: no-repeat;  /* Ensures the image does not repeat */
            background-attachment: fixed;  /* Makes the background fixed when scrolling */
            color: white;  /* Text color set to white for contrast */
        }}
        .stApp {{
            background-color: transparent;
        }}
        
        /* Option Menu Styling */
        .css-1v0mbp5 {{
            background-color: rgba(255, 255, 255, 0.7);  /* Semi-transparent background for option menu */
            border-radius: 10px;  /* Optional: round the corners */
        }}
        
        /* Tab Styling */
        /* Target the tab buttons using Streamlit's dynamically generated class names */
        .stTabs > div > div > div > button {{
            color: white !important;  /* Set the tab text color to white */
            background-color: transparent !important;  /* Make tabs transparent initially */
            border: none !important;  /* Remove border from tabs */
            padding: 10px 20px;  /* Adjust tab padding */
            border-radius: 8px;  /* Optional: round the corners of the tabs */
            font-weight: normal;  /* Regular font weight for non-selected tabs */
        }}

        /* Hover effect on tabs */
        .stTabs > div > div > div > button:hover {{
            background-color: #7f7823 !important;  /* light green for hover effect */
        }}

        /* The selected tab (active tab) */
        .stTabs > div > div > div > button[aria-selected="true"] {{
            background-color: #7f7823 !important;  /* Active tab background (Airbnb background green) */
            color: white !important;  /* Ensures the active tab text remains white */
            font-weight: bold;  /* Make selected tab text bold */
            border-bottom: 3px solid #7f7823 !important;  /* Active tab underline (orange-red) */
        }}

        /* Set tab container's background to blur */
        .stTabs {{
            background: rgba(0, 0, 0, 0.3);  /* Semi-transparent black background */
            backdrop-filter: blur(10px);  /* Apply blur effect to the background */
            border-radius: 10px;  /* Optional: round the corners of the tab container */
        }}

        .header {{
            color: white;
            font-size: 28px;  /* Increased font size */
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  /* Text shadow effect */
        }}

        /* Styling for content text with text-shadow and increased font size */
        .content-text {{
            color: white;
            font-size: 18px;  /* Increased font size */
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);  /* Light text shadow effect */
        }}
        
        .stColumn {{
            background: rgba(0, 0, 0, 0.3);  /* Semi-transparent black background */
            backdrop-filter: blur(10px);  /* Apply blur effect */
            border-radius: 10px;  /* Optional: round the corners */
            padding: 10px;
        }}
    </style>
""", unsafe_allow_html=True)

# Title for the app

col1,col2= st.columns([3,9])
with col1:
    st.image(r"D:\Air_bnb\airbnb-logo-white.png", width=300)
with col2:
    st.markdown("<h1 style='text-align:center;text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); color:#ffffff; font-size:50px;'>AirBnb Data Analysis</h1>", unsafe_allow_html=True)

# Create the option menu

#option menu

selected = option_menu(
    menu_title=None,
    options=["Home","Data Exploration","About"],
    icons=["house", "bar-chart", "info-circle"],
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link-selected": {
            "background-color": "#7f7823",  # Highlighted option with Airbnb background green
            "color": "white",  # White text when selected
        },
        "nav-link": {
            "color": "#ffffff",  # white for unselected options
        }
    }
)

def datafr():
    df= pd.read_csv("D:\Air_bnb\Airbnb.csv")
    return df

df = datafr()


if selected == 'Home':

    col1,col2=st.columns(2)

    with col1:

        image2= Image.open(r"D:\Air_bnb\Airbnb Home About_2.webp")
        st.image(image2,width=650)
        image1= Image.open(r"D:\Air_bnb\Airbnb Home About.webp")
        st.image(image1,width=650)

    with col2:

        st.write("")
        st.write("")
        # Content in the second column (styled)
        st.markdown('<h2 class="header">About Airbnb</h2>', unsafe_allow_html=True)
        st.markdown('<p class="content-text">Airbnb is an online marketplace that connects people who want to rent out '
                    'their property with people who are looking for accommodations, '
                    'typically for short stays. Airbnb offers hosts a relatively easy way to '
                    'earn some income from their property. Guests often find that Airbnb rentals '
                    'are cheaper and homier than hotels.</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="content-text">Airbnb Inc (Airbnb) operates an online platform for hospitality services. '
                    'The company provides a mobile application (app) that enables users to list, '
                    'discover, and book unique accommodations across the world. '
                    'The app allows hosts to list their properties for lease, '
                    'and enables guests to rent or lease on a short-term basis, '
                    'which includes vacation rentals, apartment rentals, homestays, castles, '
                    'tree houses and hotel rooms. The company has presence in China, India, Japan, '
                    'Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy, '
                    'Norway, Portugal, Russia, Spain, Sweden, the UK, and others. '
                    'Airbnb is headquartered in San Francisco, California, the US.</p>', unsafe_allow_html=True)

        # Section for background info with different header
        st.markdown('<h2 class="header">Background of Airbnb</h2>', unsafe_allow_html=True)
        st.markdown('<p class="content-text">Airbnb was born in 2007 when two Hosts welcomed three guests to their '
                    'San Francisco home, and has since grown to over 4 million Hosts who have '
                    'welcomed over 1.5 billion guest arrivals in almost every country across the globe.</p>', unsafe_allow_html=True)


if selected == 'Data Exploration':
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Price Analysis','Availability Analysis','Location Based','Geospatial Visualization','Top Charts'])
    with tab1:
        st.title("**PRICE DIFFERENCE**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country= st.selectbox("Select the Country",df["country"].unique(),key="selectbox_1")

            df1= df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

            room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique(),key="selectbox_2")
            
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)
        
        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            
     
            proper_ty= st.selectbox("Select the Property_type",df2["property_type"].unique(),key="selectbox_3")

            df4= df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.BuPu_r,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600, height= 500)
            st.plotly_chart(fig_pi)

        col1,col2= st.columns(2)

        with col1:

            
            hostresponsetime= st.selectbox("Select the host_response_time",df4["host_response_time"].unique(),key="selectbox_4")

            df5= df4[df4["host_response_time"] == hostresponsetime]

            df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace= True)

            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
            

            st.plotly_chart(fig_do_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace= True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)
           
            st.plotly_chart(fig_do_bar_2)

    with tab2:

        def datafr():
            df_a= pd.read_csv("D:\Air_bnb\Airbnb.csv")
            return df_a

        df_a= datafr()

        st.title("**AVAILABILITY ANALYSIS**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country_a= st.selectbox("Select the Country",df_a["country"].unique(),key="selectbox_5")

            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique(),key="selectbox_6")
            
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_30)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col1,col2= st.columns(2)

        with col1:
            
            df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(df_a_sunb_365)
        
        
        roomtype_a= st.selectbox("Select the Room Type", df2_a["room_type"].unique(),key="selectbox_7")

        df3_a= df2_a[df2_a["room_type"] == roomtype_a]

        df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_mul_bar_a.reset_index(inplace= True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)

        st.plotly_chart(fig_df_mul_bar_a)

    with tab3:

        st.title("LOCATION ANALYSIS")
        st.write("")

        def datafr():
            df= pd.read_csv("D:\Air_bnb\Airbnb.csv")
            return df

        df_l= datafr()

        country_l= st.selectbox("Select the Country",df_l["country"].unique(),key="selectbox_8")

        df1_l= df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        proper_ty_l= st.selectbox("Select the Property_type",df1_l["property_type"].unique(),key="selectbox_9")

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("") 

        def select_the_df(sel_val):
            if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
        
        differ_max_min= df2_l['price'].max()-df2_l['price'].min()

        val_sel= st.radio("Select the Price Range",[str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)
        
        # checking the correlation

        df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()
        
        st.dataframe(df_val_sel_corr)

        df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace= True)

        fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                    hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_1)
        
        
        room_ty_l= st.selectbox("Select the Room_Type", df_val_sel["room_type"].unique(),key="selectbox_10")

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_2)

        fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_3)

    with tab4:

        st.title("GEOSPATIAL VISUALIZATION")
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                        color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        fig_4.update_layout(width=1200,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4)  
    
    with tab5:

        country_t= st.selectbox("Select the Country",df["country"].unique(),key="selectbox_12")

        df1_t= df[df["country"] == country_t]

        property_ty_t= st.selectbox("Select the Property_type",df1_t["property_type"].unique(),key="selectbox_13")

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                            title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)
        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room_Type",df2_t_sorted["room_type"].unique(),key="selectbox_14")

        df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

        df3_t_sorted_price= df3_t.sort_values(by= "price")
        df3_t_sorted_price.reset_index(drop= True, inplace = True)

        df3_top_50_price= df3_t_sorted_price.head(100)

        fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,df3_top_50_price["price"].max()),
                                title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "greens",
                                 title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                range_color=(0,df3_top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)

if selected == 'About':
    col1,col2=st.columns(2)

    with col1:
        image1= Image.open(r"Airbnb About Green.webp")
        st.image(image1)   
    with col2:

        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        
        st.markdown('<h2 class="header">ABOUT THIS PROJECT</h2>', unsafe_allow_html=True)

        # Project steps with subheaders and content
        st.markdown('<h3 class="subheader">1. Data Collection:</h3>', unsafe_allow_html=True)
        st.markdown('<p class="content-text"><span class="italic-text"></span>Gather data from Airbnb\'s public API or other available sources. '
                    'Collect information on listings, hosts, reviews, pricing, and location data.<span class="italic-text"></span></p>', unsafe_allow_html=True)

        st.markdown('<h3 class="subheader">2. Data Cleaning and Preprocessing:</h3>', unsafe_allow_html=True)
        st.markdown('<p class="content-text"><span class="italic-text"></span>Clean and preprocess the data to handle missing values, outliers, '
                    'and ensure data quality. Convert data types, handle duplicates, and standardize formats.<span class="italic-text"></span></p>', unsafe_allow_html=True)

        st.markdown('<h3 class="subheader">3. Exploratory Data Analysis (EDA):</h3>', unsafe_allow_html=True)
        st.markdown('<p class="content-text"><span class="italic-text"></span>Conduct exploratory data analysis to understand the distribution and patterns in the data. '
                    'Explore relationships between variables and identify potential insights.<span class="italic-text"></span></p>', unsafe_allow_html=True)

        st.markdown('<h3 class="subheader">4. Visualization:</h3>', unsafe_allow_html=True)
        st.markdown('<p class="content-text"><span class="italic-text"></span>Create visualizations to represent key metrics and trends. '
                    'Use charts, graphs, and maps to convey information effectively. Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.<span class="italic-text"></span></p>', unsafe_allow_html=True)

        st.markdown('<h3 class="subheader">5. Geospatial Analysis:</h3>', unsafe_allow_html=True)
        st.markdown('<p class="content-text"><span class="italic-text"></span>Utilize geospatial analysis to understand the geographical distribution of listings. '
                    'Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.<span class="italic-text"></span></p>', unsafe_allow_html=True)
