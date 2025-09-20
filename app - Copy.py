import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import google.generativeai as genai
import io # Needed to handle uploaded CSV as text

# --- Sidebar for Configuration ---
with st.sidebar:
    st.header("API Configuration")
    gemini_api_key = st.text_input("Gemini API Key", type="password", help="Get your API key from Google AI Studio")
    
    selected_model_name = None # Initialize outside the if block
    if gemini_api_key:
        genai.configure(api_key=gemini_api_key)
        
        st.subheader("Available Gemini Models")
        try:
            list_models_response = genai.list_models()
            available_models = []
            
            for m in list_models_response:
                # We need models that support TEXT generation
                if 'generateContent' in m.supported_generation_methods:
                    available_models.append(m.name)
            
            if available_models:
                # Prioritize 'gemini-pro' if available
                if 'gemini-pro' in available_models:
                    default_index = available_models.index('gemini-pro')
                elif 'models/gemini-pro' in available_models:
                    default_index = available_models.index('models/gemini-pro')
                else:
                    default_index = 0 # Fallback to the first available

                selected_model_name = st.selectbox(
                    "Select a model for suggestions", 
                    available_models,
                    index=default_index,
                    key="model_selector" # Add a key for consistent behavior
                )
                st.session_state['gemini_model_name'] = selected_model_name
                st.success(f"Using model: {selected_model_name}")
            else:
                st.warning("No models found that support 'generateContent' with this API key. Please check your API key.")
                st.session_state['gemini_model_name'] = None

        except Exception as e:
            st.error(f"Could not list models. Check API key and internet connection: {e}")
            st.session_state['gemini_model_name'] = None

    else:
        st.warning("Please enter your Gemini API Key!")
        st.session_state['gemini_model_name'] = None # Clear model if key is missing

    st.header("Navigation")
    page = st.radio("Go to", ["Upload Data", "Dashboards", "Suggestions"], key="page_navigator")

# --- Main Page Content ---
st.title("Student Performance Analyzer")

if page == "Upload Data":
    st.header("Upload Student Data")
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                # Use io.BytesIO to read directly from uploaded file buffer
                df = pd.read_csv(io.BytesIO(uploaded_file.getvalue()))
            else:
                df = pd.read_excel(io.BytesIO(uploaded_file.getvalue()))
            
            # Basic validation of expected columns
            expected_columns = ['Year', 'Semester', 'Subject', 'Grade', 'GPA']
            if not all(col in df.columns for col in expected_columns):
                st.error(f"Error: Missing one or more expected columns. Please ensure your file has these columns: {', '.join(expected_columns)}")
                st.session_state['student_data'] = pd.DataFrame() # Clear invalid data
            else:
                st.session_state['student_data'] = df
                st.success("Data uploaded successfully!")
                st.write("First 5 rows of your data:")
                st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.session_state['student_data'] = pd.DataFrame() # Clear invalid data

elif page == "Dashboards":
    st.header("Student Performance Dashboards")
    if 'student_data' in st.session_state and not st.session_state['student_data'].empty:
        df = st.session_state['student_data'].copy() # Use a copy to avoid SettingWithCopyWarning

        # Ensure GPA is numeric for calculations
        df['GPA'] = pd.to_numeric(df['GPA'], errors='coerce')
        df.dropna(subset=['GPA'], inplace=True) # Drop rows where GPA couldn't be converted

        if not df.empty:
            st.subheader("Overall Performance")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                overall_avg_gpa = df['GPA'].mean()
                st.metric(label="Overall Average GPA", value=f"{overall_avg_gpa:.2f}")
            with col2:
                total_subjects = df['Subject'].nunique()
                st.metric(label="Total Subjects Taken", value=total_subjects)
            with col3:
                # Assuming higher GPA is better for 'top' subject
                if not df.empty:
                    # Find the subject with the highest average GPA
                    subject_avg_gpa = df.groupby('Subject')['GPA'].mean()
                    top_subject = subject_avg_gpa.idxmax()
                    top_subject_gpa = subject_avg_gpa.max()
                    st.metric(label="Top Subject (Avg. GPA)", value=f"{top_subject} ({top_subject_gpa:.2f})")
                else:
                    st.metric(label="Top Subject (Avg. GPA)", value="N/A")


            st.subheader("GPA by Subject")
            subject_gpa = df.groupby('Subject')['GPA'].mean().sort_values(ascending=False).reset_index()
            fig_subject_gpa = px.bar(
                subject_gpa, 
                x='Subject', 
                y='GPA', 
                title='Average GPA per Subject',
                color='GPA', # Color bars based on GPA for visual impact
                color_continuous_scale=px.colors.sequential.Viridis
            )
            st.plotly_chart(fig_subject_gpa)

            st.subheader("Performance Trend by Semester")
            # Calculate average GPA per Semester (ordered by Year and Semester)
            semester_gpa = df.groupby(['Year', 'Semester'])['GPA'].mean().reset_index()
            semester_gpa['Year_Semester'] = semester_gpa['Year'].astype(str) + '-S' + semester_gpa['Semester'].astype(str)
            # Sort chronologically
            semester_gpa = semester_gpa.sort_values(by=['Year', 'Semester'])
            
            fig_trend = px.line(
                semester_gpa, 
                x='Year_Semester', 
                y='GPA', 
                title='Average GPA Over Semesters',
                markers=True,
                line_shape="linear" # Connect points with straight lines
            )
            fig_trend.update_xaxes(title_text="Year-Semester")
            fig_trend.update_yaxes(title_text="Average GPA")
            st.plotly_chart(fig_trend)

        else:
            st.info("No valid student data found to display dashboards.")

    else:
        st.warning("Please upload student data first on the 'Upload Data' page.")

elif page == "Suggestions":
    st.header("Personalized Study Suggestions")
    if 'student_data' in st.session_state and not st.session_state['student_data'].empty:
        if gemini_api_key and st.session_state.get('gemini_model_name'):
            df = st.session_state['student_data'].copy()
            
            # Ensure GPA is numeric for analysis by AI
            df['GPA'] = pd.to_numeric(df['GPA'], errors='coerce')
            df.dropna(subset=['GPA'], inplace=True)

            if df.empty:
                st.warning("No valid student data with GPA found to generate suggestions.")
            else:
                # Prepare data for Gemini - a more detailed summary
                student_performance_list = df[['Year', 'Semester', 'Subject', 'Grade', 'GPA']].to_dict(orient='records')
                
                # Get weaker subjects
                subject_avg_gpa = df.groupby('Subject')['GPA'].mean().sort_values()
                weaker_subjects = subject_avg_gpa.head(3).index.tolist() # Top 3 lowest GPA subjects

                # Get stronger subjects
                stronger_subjects = subject_avg_gpa.tail(3).index.tolist() # Top 3 highest GPA subjects

                prompt = f"""
                Analyze the following student's academic record:
                {student_performance_list}

                Based on this data, provide specific, actionable study suggestions focusing on two main areas:
                1.  **Improving performance in weaker subjects:** Specifically target these subjects: {', '.join(weaker_subjects)}. Provide strategies like specific study techniques, resource recommendations, or approaches to understanding the core concepts.
                2.  **Maintaining excellence and further developing in stronger subjects:** Specifically target these subjects: {', '.join(stronger_subjects)}. Suggest ways to go beyond the curriculum, explore advanced topics, or apply knowledge in practical projects.

                Also, provide general advice for overall academic improvement and exam preparation. The suggestions should be practical, encouraging, and easy for a student to understand and implement.
                """
                
                with st.spinner(f"Generating suggestions with {st.session_state['gemini_model_name']}..."):
                    try:
                        model = genai.GenerativeModel(st.session_state['gemini_model_name'])
                        response = model.generate_content(prompt)
                        st.success("Suggestions generated!")
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"Error calling Gemini API with {st.session_state['gemini_model_name']}: {e}")
                        st.info("Please ensure the selected model is suitable for text generation and your API key is valid. If the error persists, try selecting a different model from the sidebar.")
        else:
            st.warning("Please enter your Gemini API Key in the sidebar and ensure a suitable model is selected.")
    else:
        st.warning("Please upload student data first on the 'Upload Data' page.")