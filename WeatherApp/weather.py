import streamlit as st
import pandas as pd
import plotly.express as px

# Lexo dataset-in
weather_df = pd.read_csv("weather.csv")

# Kthe Date në format date
weather_df["Date"] = pd.to_datetime(weather_df["Date"])

st.title("Weather Temperature Analysis - Prishtina")
st.write("Analiza e temperaturave ditore në Prishtinë.")

# --------------------------------
# 5 ditët më të nxehta
# --------------------------------

st.subheader("5 Ditët më të Nxehta në Prishtinë")

top_5_days = weather_df.nlargest(5, "Temperature")

st.dataframe(
    top_5_days[["Date", "Temperature"]],
    use_container_width=True
)

fig_hot = px.bar(
    top_5_days,
    x="Date",
    y="Temperature",
    title="5 Ditët më të Nxehta",
    color="Temperature"
)

st.plotly_chart(
    fig_hot,
    use_container_width=True
)


# --------------------------------
# 5 ditët më të ftohta
# --------------------------------

st.subheader("5 Ditët më të Ftohta në Prishtinë")

bottom_5_days = weather_df.nsmallest(5, "Temperature")

st.dataframe(
    bottom_5_days[["Date", "Temperature"]],
    use_container_width=True
)

fig_cold = px.bar(
    bottom_5_days,
    x="Date",
    y="Temperature",
    title="5 Ditët më të Ftohta",
    color="Temperature"
)

st.plotly_chart(
    fig_cold,
    use_container_width=True
)


# --------------------------------
# Statistikat
# --------------------------------

st.subheader("Statistikat e Temperaturës")

average_temperature = weather_df["Temperature"].mean()
highest_temperature = weather_df["Temperature"].max()
lowest_temperature = weather_df["Temperature"].min()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Temperatura Mesatare",
    f"{average_temperature:.2f} °C"
)

col2.metric(
    "Temperatura më e Lartë",
    f"{highest_temperature:.2f} °C"
)

col3.metric(
    "Temperatura më e Ulët",
    f"{lowest_temperature:.2f} °C"
)


# --------------------------------
# Dataset Preview
# --------------------------------

st.subheader("Dataset")

st.dataframe(
    weather_df,
    use_container_width=True
)
