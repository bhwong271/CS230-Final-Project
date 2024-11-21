import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Fortune 500 Companies by State")
#initialize list of colors for the bar chart
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'pink', 'gray']

#read data file and pull out important columns
df=pd.read_csv("Fortune_500_Corporate_Headquarters.csv")
df_real=df[["NAME", "STATE", "EMPLOYEES", "REVENUES", "PROFIT"]]

#process and sort data
def process_data(df, state="NY", data_select="REVENUES"): #[PY1]
    state_data=df[df["STATE"] == state]#[DA4]
    top_data_companies=state_data.sort_values(by=data_select, ascending=False)#[DA2]
    title=f"Top Companies in {state} by {data_select}"
    return top_data_companies, title #[PY2]

#Collect inputs and write title
state = st.selectbox("Select a State:", df['STATE'].unique())  # [ST1]
data_select=st.radio("Select the Data you would like:", ('REVENUES', 'EMPLOYEES', 'PROFIT'))#[ST2]
top_data_companies, title = process_data(df_real, state, data_select)
st.header(title)

#plot data
st.write(top_data_companies[["NAME", data_select]])  # [VIZ2]
plt.bar(top_data_companies['NAME'],
        top_data_companies[data_select],
        color=colors[:len(top_data_companies)],
        label=top_data_companies["NAME"])  # [VIZ1]
plt.title(f"Top Companies in {data_select} in {state}")
plt.xlabel("COMPANIES")
plt.ylabel(data_select, fontsize="small")
plt.xticks(rotation=90)
plt.legend(title="COMPANIES", loc="upper right",bbox_to_anchor=(1.7, 1))
st.pyplot(plt)



