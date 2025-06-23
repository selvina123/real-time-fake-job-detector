import streamlit as st
from lime.lime_text import LimeTextExplainer
import numpy as np

def explain_prediction(model_pipeline, text_input):
    st.write("🔎 **LIME Explanation for the prediction:**")
    
    class_names = ["Real", "Fake"]
    explainer = LimeTextExplainer(class_names=class_names)

    explanation = explainer.explain_instance(
        text_instance=text_input,
        classifier_fn=model_pipeline.predict_proba,
        num_features=10
    )

    # Display as list of features & weights
    for word, weight in explanation.as_list():
        st.write(f"• **{word}** → {round(weight, 3)}")

    # Optional: Show HTML explanation
    # st.components.v1.html(explanation.as_html(), height=400)
