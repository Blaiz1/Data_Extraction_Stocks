import streamlit as st 
import yfinance as yf
import pandas as pd
import matplotlib.pylot as plt

#Set the pape title and layout 
st.asset_page_config(page_title = "Stock Data Extraction App", layout = "wide")

#Main title of the app
st.title("Stock Data Extraction App")

# Short description of the Subtitle 
st.write("Extract stock market prices from Yahoo Finance using a ticker symbol.")

#Sidebar Header 
st.sidebar.header("User Input")

# Input box for ticker 
ticker = st.sidebar.text_input("Enter Ticker", "AAPL")

# Input for start date 
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))

#Input for the end date
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

#download the data Button 
if st.sidebar.button("Get Data"):
  #create ticker object 
  stock = yf.Ticker(ticker)
  #download historical price data
df = stock.history(start=start_date, end=end_date)
#Check the data 
if df.empty:
  st.error("No data found. Please check the ticker symbol or date range")

else: 
  #show success message 
  st.success(f"Data successfully extracted for {ticker}") 
#Display company information 
st.subheader("Company Information")
info = stock.info

company_name = info.get("longName", "N/A")
sector = infor.get("sector", "N/A")
industry = info.get("industry", "N/A")
market_cap = info.get("market cap", "N/A")
website = info.get("website", "N/A")

st.write(f"**Company Name:** {company_name}")
st.write(f"**Sector:** {sector}")
st.write(f"**Industry:** {industry}")
st.write(f"**Market Cap:** {market_cap}")
st.write(f"**Website:** {website}")

st.subheader("Historical Stock Data")
st.dataframe(df)

st.subheader("Closing Price Chart") 
fig, ax = plt.subplots()
ax.plot(df.index, df["Close"]) 
ax.set_xlabel("Date")
ax.set_ylabel("Closing Price")
ax.set_title(f"{ticker} Closing Price")
st.pyplot(fig)

csv = df.to_csv().encode("utf-8")

st.dowload_button(
  label= "Download Dataas CSV",
  data=csv,
  file_name= f"{ticker}_stock_data.csv",
  mime="text/csv"
)






