import lime
import lime.lime_text
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline

def explain_with_lime(model, vectorizer, text_input):
    # Create pipeline
    c = make_pipeline(vectorizer, model)

    # Initialize explainer
    explainer = lime.lime_text.LimeTextExplainer(class_names=['Real', 'Fake'])

    # Generate explanation
    exp = explainer.explain_instance(text_input, c.predict_proba, num_features=10)

    # Plot explanation
    fig = exp.as_pyplot_figure()
    plt.tight_layout()
    st.pyplot(fig)
