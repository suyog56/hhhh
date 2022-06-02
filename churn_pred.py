import pandas as pd
import numpy as np
import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")
model = pickle.load(open("model.pkl","rb")) #loading the created model




#'AGE', 'CUS_Month_Income', 'YEARS_WITH_US', 'total_debit_amount',
       #'total_debit_transactions', 'total_credit_amount',
       #'total_credit_transactions', 'total_transactions', 'CUS_Gender_MALE',
       #'CUS_Target'

st.set_page_config(page_title="Churn Application") #tab title

#prediction function
def predict_status(AGE, CUS_Month_Income, YEARS_WITH_US, total_debit_amount,
total_debit_transactions,total_credit_amount,total_credit_transactions, total_transactions,CUS_Gender_MALE,CUS_Target):
    
    input_data = np.asarray([AGE, CUS_Month_Income, YEARS_WITH_US, total_debit_amount,
    total_debit_transactions, total_credit_amount,total_credit_transactions, total_transactions,
    CUS_Gender_MALE, CUS_Target])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():

    # titling your page
    st.title("Churn Prediction App")
    st.write("A quick ML app to predict Churn ")

    #getting the input
    AGE = st.numeric_input("Enter your AGE")
    CUS_Month_Income = st.number_input("Enter your CUS_Month_Income")
    YEARS_WITH_US = st.number_input("Enter your YEARS_WITH_US")
    total_debit_amount = st.number_input("Enter your area_mean")
    total_debit_transactions = st.number_input("Enter your total debit transactions")
    total_credit_amount = st.number_input("Enter your total credit amount")
    total_credit_transactions = st.number_input("Enter your total credit transactions")
    total_transactions = st.number_input("Enter your total transactions")
    CUS_Gender_MALE = st.number_input("Enter your CUS_Gender_MALE  , 0 == Male , 1 == Female")
    CUS_Target = st.number_input("Enter your CUS_Target ")




    #predict value
    Status = None

    if st.button("Predict"):
        Status = predict_status(AGE, CUS_Month_Income, YEARS_WITH_US,total_debit_amount,total_debit_transactions, 
        total_credit_amount,total_credit_transactions, total_transactions,CUS_Gender_MALE, CUS_Target)
        if Status=="1":
            st.info("You Re Churn Customer")
            
        elif Status=="0":
                st.info(" Active Customer")
        
        else:
            st.error("noooo")

            
        st.subheader("what next? Recommending You a New Product")
        
        
        
        
        st.write("## Thank you for Visiting \nProject by Suyog H")
        #st.markdown("<h1 style='text-align: right; color: blue; font-size: small;'><a href='https://github.com/suyog56/CANCER'>Looking for Source Code?</a></h1>", unsafe_allow_html=True)
        # st.markdown("<h1 style='text-align: right; color: white; font-size: small'>you can find it on my GitHub</h1>", unsafe_allow_html=True)

    


if __name__=="__main__":
    main()