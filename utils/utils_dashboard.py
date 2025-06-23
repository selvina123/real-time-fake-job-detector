import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def plot_prediction_bar(label, confidence):
    """
    Display a horizontal neon-style bar showing Real vs Fake confidence.
    """
    confidence = round(confidence * 100, 2)
    fake_percent = confidence if label == 1 else 100 - confidence
    real_percent = 100 - fake_percent

    # Neon colors: Fake = Pink, Real = Green
    colors = ['#FF1493', '#32CD32']
    values = [fake_percent, real_percent]
    labels = ['Fake Job', 'Real Job']

    fig, ax = plt.subplots(figsize=(7, 1.5))
    ax.barh([''], [values[0]], color=colors[0], edgecolor='white')
    ax.barh([''], [values[1]], left=[values[0]], color=colors[1], edgecolor='white')

    for i, v in enumerate(values):
        ax.text(
            sum(values[:i]) + v / 2,
            0,
            f"{v:.1f}%",
            color='white',
            va='center',
            ha='center',
            fontweight='bold',
            fontsize=12,
        )

    ax.set_xlim(0, 100)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_frame_on(False)
    ax.set_facecolor('#0E1117')
    fig.patch.set_facecolor('#0E1117')

    st.pyplot(fig)

def plot_confidence_gauge(confidence):
    """
    Display a semicircle gauge to visualize confidence.
    """
    fig, ax = plt.subplots(figsize=(5, 2.5), subplot_kw={'projection': 'polar'})
    theta = np.linspace(0, np.pi, 100)
    radii = np.ones_like(theta)
    colors = plt.cm.coolwarm(confidence)

    ax.plot(theta, radii, linewidth=15, color=colors)
    ax.fill_between(theta, 0, radii, color=colors, alpha=0.4)

    ax.set_rticks([])
    ax.set_xticks([])
    ax.set_yticklabels([])
    ax.set_thet_
