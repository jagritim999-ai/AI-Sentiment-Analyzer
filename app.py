import streamlit as st
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


st.set_page_config(page_title="AI Sentiment Analyzer",page_icon="😊",layout="wide")

st.title("😊 AI Sentiment Analyzer")
if "history" not in st.session_state:
    st.session_state.history = []
st.markdown(
    """
    <h4 style='color:gray;'>
    Analyze customer reviews, feedback and comments using AI
    </h4>
    """,
    unsafe_allow_html=True
)
st.subheader("📝 Example Reviews")

st.code("I love this product. It is amazing!")
st.code("This service is terrible and very bad.")
st.code("This is a normal product.")
st.sidebar.title("AI Sentiment Analyzer")

st.sidebar.info(
    "Analyze reviews, comments and feedback using AI."
)
st.sidebar.subheader("Statistics")
st.sidebar.subheader("📌 Project Info")
st.sidebar.write("Model: TextBlob")
st.sidebar.write("Version: 1.0")
st.write("Analyze customer reviews, feedback and comments using AI.")

text = st.text_area("Enter your review or text")

if st.button("Analyze Sentiment"):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity
    st.session_state.history.append(polarity)   
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Sentiment Score", round(polarity, 2))

    with col2:
        st.metric("Text Length", len(text))
        st.info(f"Sentiment Score: {round(polarity, 2)}")
        st.progress((polarity + 1)/2)

    if polarity > 0:
        st.success("😊 Positive Sentiment")
        st.balloons()

    elif polarity < 0:
        st.error("😞 Negative Sentiment")

    else:
        st.warning("😐 Neutral Sentiment")
    result = f"Sentiment Score: {round(polarity,2)}"
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    st.info(f"Detected Sentiment: {sentiment}")
    st.subheader("🧠 AI Analysis Summary")

    if polarity > 0:
        st.write("The review expresses a positive opinion and satisfaction.")
    elif polarity < 0:
        st.write("The review expresses dissatisfaction or a negative opinion.")
    else:
        st.write("The review is neutral without strong emotions.")
    st.download_button(
        "📥 Download Result",
         data=result,
        file_name="sentiment_result.txt"
    )
    st.subheader("Analysis Result")
    st.subheader(sentiment)
    st.subheader("Sentiment Strength")
    st.progress(min(abs(polarity), 1.0))
    confidence = round(abs(polarity) * 100, 2)
    st.metric("🎯 Confidence", f"{confidence}%")
    rating = round(((polarity + 1) / 2) * 5, 1)
    st.metric("⭐ Review Rating", f"{rating}/5")
    chart_data = pd.DataFrame(
      {
        "Metric": ["Sentiment Score"],
        "Value": [polarity]
      }
    )

   
    st.subheader("📊 Sentiment Score Chart")
    st.bar_chart(chart_data.set_index("Metric"))
    st.subheader("📊 Sentiment Distribution")

    if polarity > 0:
        labels = ["Positive"]
        values = [100]
    elif polarity < 0:
        labels = ["Negative"]
        values = [100]
    else:
        labels = ["Neutral"]
        values = [100]

    fig, ax = plt.subplots(figsize=(4,4))
    ax.pie(values, labels=labels, autopct="%1.0f%%")
    st.pyplot(fig)
    word_count = len(text.split())
    char_count = len(text)
    st.info(f"Entered Text: {text[:100]}")

    col1, col2 = st.columns(2)

    with col1:
       st.metric("📝 Word Count", word_count)

    with col2:
      st.metric("🔤 Character Count", char_count)

    st.subheader("📈 Sentiment History")

    history_df = pd.DataFrame(
       st.session_state.history,
       columns=["Sentiment Score"]
    )

    st.line_chart(history_df)

    st.subheader("📋 Analysis History")

    history_table = pd.DataFrame({
         "Analysis No": range(1, len(st.session_state.history) + 1),
         "Score": st.session_state.history
    })

    st.dataframe(history_table)
    
    

    st.markdown("---")
    st.caption("Developed by Jagriti Mandal")