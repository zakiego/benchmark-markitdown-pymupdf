import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV files
github_df = pd.read_csv("result/github-action.csv")
mac_df = pd.read_csv("result/mac.csv")
coolify_df = pd.read_csv("result/coolify.csv")

# Set style
plt.style.use("seaborn-v0_8")
sns.set_palette("husl")

# Create figure with two subplots - increased width from 12 to 15
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))


# Function to extract benchmark name
def clean_benchmark_name(name):
    return name.replace("uv run src/", "").replace("/with_", "_").replace(".py", "")


# Process data for plotting
github_df["Clean_Name"] = github_df["Benchmark"].apply(clean_benchmark_name)
mac_df["Clean_Name"] = mac_df["Benchmark"].apply(clean_benchmark_name)
coolify_df["Clean_Name"] = coolify_df["Benchmark"].apply(clean_benchmark_name)

# Plot Serial Executions
serial_data = {
    "GitHub Actions (2 cores)": github_df[github_df["Type"] == "serial"][
        "Mean (s)"
    ].values,
    "Mac (8 cores)": mac_df[mac_df["Type"] == "serial"]["Mean (s)"].values,
    "Coolify (16 cores)": coolify_df[coolify_df["Type"] == "serial"]["Mean (s)"].values,
}

labels = [
    name.split("_")[1]
    for name in github_df[github_df["Type"] == "serial"]["Clean_Name"]
]
x = range(len(labels))
width = 0.2  # Reduced from 0.25 to create more space between bars

# Plot bars and add time labels for serial execution
rects1 = ax1.bar(
    [i - width * 1.2 for i in x],  # Increased spacing
    serial_data["GitHub Actions (2 cores)"],
    width,
    label="GitHub Actions (2 cores)",
)
rects2 = ax1.bar(
    [i for i in x],
    serial_data["Mac (8 cores)"],
    width,
    label="Mac (8 cores)",
)
rects3 = ax1.bar(
    [i + width * 1.2 for i in x],  # Increased spacing
    serial_data["Coolify (16 cores)"],
    width,
    label="Coolify (16 cores)",
)


# Add time labels on bars for serial execution
def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(
            f"{height:.1f}s",
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            rotation=0,
        )


autolabel(rects1, ax1)
autolabel(rects2, ax1)
autolabel(rects3, ax1)

ax1.set_ylabel("Time (seconds)")
ax1.set_title(
    "Serial Execution Performance Comparison\n(Test on 517 pages PDF)\n↓ Lower is better",
    pad=15,
)
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45)
ax1.legend()

# Plot Parallel Executions
parallel_data = {
    "GitHub Actions (2 cores)": github_df[github_df["Type"] == "parallel"][
        "Mean (s)"
    ].values,
    "Mac (8 cores)": mac_df[mac_df["Type"] == "parallel"]["Mean (s)"].values,
    "Coolify (16 cores)": coolify_df[coolify_df["Type"] == "parallel"][
        "Mean (s)"
    ].values,
}

labels = [
    name.split("_")[1]
    for name in github_df[github_df["Type"] == "parallel"]["Clean_Name"]
]
x = range(len(labels))

# Plot bars and add time labels for parallel execution
rects4 = ax2.bar(
    [i - width * 1.2 for i in x],  # Increased spacing
    parallel_data["GitHub Actions (2 cores)"],
    width,
    label="GitHub Actions (2 cores)",
)
rects5 = ax2.bar(
    [i for i in x],
    parallel_data["Mac (8 cores)"],
    width,
    label="Mac (8 cores)",
)
rects6 = ax2.bar(
    [i + width * 1.2 for i in x],  # Increased spacing
    parallel_data["Coolify (16 cores)"],
    width,
    label="Coolify (16 cores)",
)

# Add time labels on bars for parallel execution
autolabel(rects4, ax2)
autolabel(rects5, ax2)
autolabel(rects6, ax2)

ax2.set_ylabel("Time (seconds)")
ax2.set_title(
    "Parallel Execution Performance Comparison\n(Test on 517 pages PDF)\n↓ Lower is better",
    pad=15,
)
ax2.set_xticks(x)
ax2.set_xticklabels(labels, rotation=45)
ax2.legend()

# Adjust layout and save
plt.tight_layout()
plt.savefig("result/performance_comparison.png", dpi=300, bbox_inches="tight")
plt.close()
