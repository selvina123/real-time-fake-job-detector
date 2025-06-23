import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import time

def plot_prediction_bar(label, confidence):
    """
    Thin neon-style bar with light animation and elegant sizing.
    """
    confidence = round(confidence * 100, 2)
    fake_percent = confidence if label == 1 else 100 - confidence
    real_percent = 100 - fake_percent

    colors = ['#ff69b4', '#90ee90']  # Soft Pink & Light Green
    labels = ['Fake Job', 'Real Job']

    st.markdown("#### 🎯 Prediction Confidence")
    st.markdown(
        f"<small style='color:#ccc;'>This bar shows model confidence of <b>{confidence:.1f}%</b> that the job is <b>{'Fake' if label == 1 else 'Real'}</b>.</small>",
        unsafe_allow_html=True
    )

    plot_placeholder = st.empty()

    for pct in range(0, int(confidence) + 1, 5):
        current_fake = pct if label == 1 else 100 - pct
        current_real = 100 - current_fake

        fig, ax = plt.subplots(figsize=(5.5, 0.3))  # 💡 Super thin bar height

        # Main bars
        ax.barh([0], [current_fake], color=colors[0], edgecolor='white', height=0.25)
        ax.barh([0], [current_real], left=[current_fake], color=colors[1], edgecolor='white', height=0.25)

        # Labels inside bars
        for i, v in enumerate([current_fake, current_real]):
            ax.text(
                sum([current_fake if i == 1 else 0]) + v / 2,
                0,
                f"{v:.1f}%",
                color='black',
                va='center',
                ha='center',
                fontweight='bold',
                fontsize=10,
                path_effects=[path_effects.withStroke(linewidth=2, foreground='white')]
            )

        ax.set_xlim(0, 100)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_frame_on(False)
        ax.set_facecolor('#0E1117')
        fig.patch.set_facecolor('#0E1117')

        # Legend
        fig.legend(
            labels,
            loc="lower center",
            bbox_to_anchor=(0.5, -1.1),
            ncol=2,
            frameon=False,
            fontsize=8,
            labelcolor='white'
        )

        plot_placeholder.pyplot(fig)
        time.sleep(0.04)


