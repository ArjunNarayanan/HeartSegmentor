import pandas as pd
import matplotlib.pyplot as plt
import os


def add_dataset(ax, df, start, step, color, width=1):
    ax.boxplot(
        df["Epi"],
        positions=[start],
        widths=[width],
        patch_artist=True,
        boxprops=dict(
            facecolor=color,
            alpha=1.0
        ),
        medianprops=dict(color="white"),
    )
    ax.boxplot(
        df["LV"],
        positions=[start + step],
        widths=[width],
        patch_artist=True,
        boxprops=dict(
            facecolor=color,
            alpha=1.0
        ),
        medianprops=dict(color="white")
    )
    ax.boxplot(
        df["RV"],
        positions=[start + 2 * step],
        widths=[width],
        patch_artist=True,
        boxprops=dict(
            facecolor=color,
            alpha=1.0
        ),
        medianprops=dict(color="white")
    )
    ax.boxplot(
        df["LA"],
        positions=[start + 3 * step],
        widths=[width],
        patch_artist=True,
        boxprops=dict(
            facecolor=color,
            alpha=1.0
        ),
        medianprops=dict(color="white")
    )
    ax.boxplot(
        df["RA"],
        positions=[start + 4 * step],
        widths=[width],
        patch_artist=True,
        boxprops=dict(
            facecolor=color,
            alpha=1.0
        ),
        medianprops=dict(color="white")
    )
    ax.boxplot(
        df["Ao"],
        positions=[start + 5 * step],
        widths=[width],
        patch_artist=True,
        boxprops=dict(
            facecolor=color,
            alpha=1.0
        ),
        medianprops=dict(color="white")
    )
    bp = ax.boxplot(
        df["PA"],
        positions=[start + 6 * step],
        widths=[width],
        patch_artist=True,
        boxprops=dict(
            facecolor=color,
            alpha=1.0
        ),
        medianprops=dict(color="white")
    )

    return bp


input_folder = "output/MMWHS-test/"
input_file = os.path.join(input_folder, "ct_dice_compiled.csv")
dice_data = pd.read_csv(input_file)

step = 1
fig, ax = plt.subplots(figsize=(12, 4))
ax.set_ylim([0, 1])
ax.set_xlim([0, 8])
ax.plot([0., 10], 2 * [0.9], "--", color="black")

dataset_bp = add_dataset(ax, dice_data, start=1, step=step, color="goldenrod", width=0.5)
xtick_positions = range(1,8)
ax.set_xticks(xtick_positions,
              ["Myocardium", "Left Ventricle", "Right Ventricle", "Left Atrium", "Right Atrium", "Aorta",
               "Pulmonary Artery"])
ax.set_ylabel("Test Dice Score", fontsize=12)
ax.grid()
fig.tight_layout()
fig.savefig(os.path.join(input_folder, "dice_comparison.png"))
