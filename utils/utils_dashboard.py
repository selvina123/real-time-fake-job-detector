import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import time

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import time

def plot_prediction_bar(label, confidence):
    """
    Sleek animated bar chart with soft neon colors and balanced layout.
    """
    confidence = round(confidence * 100, 2)
    fake_percent = confidence if label == 1 else 100 - confidence
    real_percent = 100 - fake_percent

    colors = ['#ff69b4', '#90ee90']  # Soft Pink & Light Green
    labels = ['Fake Job', 'Real Job']

    st.markdown("#### 🎯 Prediction Confidence")
    st.markdown(
        f"**Accessibility Note:** This bar shows a confidence of **{confidence:.1f}%** that the job is **{'Fake' if label == 1 else 'Real'}**."
    )

    plot_placeholder = st.empty()

    for pct in range(0, int(confidence) + 1, 5):
        current_fake = pct if label == 1 else 100 - pct
        current_real = 100 - current_fake

        fig, ax = plt.subplots(figsize=(6, 1.2))  # Balanced height
        ax.barh([''], [current_fake], color=colors[0], edgecolor='white')
        ax.barh([''], [current_real], left=[current_fake], color=colors[1], edgecolor='white')

        for i, v in enumerate([current_fake, current_real]):
            ax.text(
                sum([current_fake if i == 1 else 0]) + v / 2,
                0,
                f"{v:.1f}%",
                color='black',
                va='center',
                ha='center',
                fontweight='bold',
                fontsize=11,
                path_effects=[path_effects.withStroke(linewidth=2, foreground='white')]
            )

        ax.set_xlim(0, 100)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_frame_on(False)
        ax.set_facecolor('#0E1117')
        fig.patch.set_facecolor('#0E1117')

        # Legend with better spacing
        fig.legend(
            labels,
            loc="lower center",
            bbox_to_anchor=(0.5, -0.25),
            ncol=2,
            frameon=False,
            fontsize=9,
            labelcolor='white'
        )

        plot_placeholder.pyplot(fig)
        time.sleep(0.05)
