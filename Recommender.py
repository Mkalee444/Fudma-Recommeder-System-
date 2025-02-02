import streamlit as st  
   from recommender_engine import Recommender  

   recommender = Recommender()  
   st.title("FUDMA Course Recommender")  
   applicant_id = st.number_input("Enter Applicant ID (1-100):", min_value=1, max_value=100)  

   if st.button("Recommend Courses"):  
       recommendations = recommender.recommend(applicant_id)  
       if isinstance(recommendations, str):  
           st.error(recommendations)  
       else:  
           st.subheader("Top Recommendations:")  
           st.dataframe(recommendations[['Course', 'Interest_Match', 'Employability']])  


