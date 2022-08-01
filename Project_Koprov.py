import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt


data = {}
for file in os.listdir("NIH_2021-2006_Funding_Dataset"):
    print(file)
    with open('NIH_2021-2006_Funding_Dataset/%s' % file, 'r',encoding="utf8") as csv:
        df = pd.read_csv(csv,low_memory=False)
        data[file[-9:-4]] = df


# Question 1
total_cost_IC = {}
for inst, df in data.items():
    print(inst)
    total_cost_IC[inst] = df["Total Cost IC"][df["Total Cost IC"] >= "1"].astype(int).sum()

plt.pie(total_cost_IC.values(), labels=total_cost_IC.keys(),explode = np.full(len(total_cost_IC), 0.1), autopct='%1.1f%%')
plt.title("Total Cost IC")

# Question 2
top10_PI_per_inst = {}
top10_PI_overall = pd.DataFrame()
for inst, df in data.items():
    tcIC_df = df[['Contact PI / Project Leader', "Total Cost IC"]][df["Total Cost IC"] >= "1"]
    tcIC_df["Total Cost IC"] = tcIC_df["Total Cost IC"].astype(int)
    top10_PI_per_inst[inst] = tcIC_df.groupby('Contact PI / Project Leader').sum().sort_values(by='Total Cost IC', ascending=False).head(10)
    top10_PI_overall = pd.concat([top10_PI_overall, top10_PI_per_inst[inst]])
    print("*"*50)
    print(f"Top 10 PI in {inst} are:\n {top10_PI_per_inst[inst]}")

top10_PI_overall = top10_PI_overall.groupby('Contact PI / Project Leader').sum()\
    .sort_values(by='Total Cost IC', ascending=False).head(10)
print(f"Top 10 PI overall: \n{top10_PI_overall}")

# Question 3
from wordcloud import WordCloud


pt_per_inst = {}
for inst, df in data.items():
    rows = df['Project Terms'].loc[df['Project Terms'] != " "]
    pt_per_inst[inst] = [word for lst in rows for word in lst.split(";")]
    pt_per_inst[inst] = pd.DataFrame(pt_per_inst[inst]).value_counts()
    wordcloud = WordCloud(background_color="white").generate(pt_per_inst[inst][:20].to_string())
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title(f"Top 20 Project Terms for {inst}")

pt_df = pd.DataFrame()
for inst, pt in pt_per_inst.items():
    pass
    pt.name = "Count"
    pt = pt.to_frame()
    pt.reset_index(inplace=True)
    pt.columns = ["Project Terms", "Count"]
    pt_df = pd.concat([pt_df, pt], axis=0)

top20_overall = pt_df.groupby("Project Terms").sum().sort_values(by="Count", ascending=False).head(20)
top20_overall.reset_index(inplace=True)
wordcloud = WordCloud(background_color="white").generate(top20_overall['Project Terms'].to_string())
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.title(f"Top 20 Project Terms overall")

# Question 4
from  datetime import datetime


uni_names = ["UNIV OF NORTH CAROLINA CHAPEL HILL", "NORTH CAROLINA STATE UNIVERSITY RALEIGH", "DUKE UNIVERSITY",
             "NORTH CAROLINA AGRI & TECH ST UNIV"]

TCsum = {}
awards_count = {}
for inst, df in data.items():
    triangle_df = df[['Organization Name', 'Project Start Date', "Total Cost IC"]][df['Organization Name'].isin(uni_names)]
    triangle_df = triangle_df[pd.to_datetime(triangle_df['Project Start Date']) >= pd.to_datetime("2010-01-01")]
    TCsum[inst] = triangle_df["Total Cost IC"][triangle_df["Total Cost IC"] >="1"].astype("int").sum()
    awards_count[inst] = triangle_df.shape[0]

plt.figure(figsize=(16, 16))
plt.pie(TCsum.values(), labels=TCsum.keys(),explode = np.full(len(TCsum), 0.1), autopct='%1.1f%%')
plt.title(f"Total Cost IC for Triangle Institutions per Institute,\n total {sum(TCsum.values())}")

plt.figure(figsize=(16, 16))
plt.pie(awards_count.values(), labels=awards_count.keys(),explode = np.full(len(awards_count), 0.1), autopct='%1.1f%%')
plt.title(f"Awards count for Triangle Institutions per Institute,\n total {sum(awards_count.values())}")

print(f"Awards count for Triangle Institutions per Institute:\n{pd.Series(awards_count, index=awards_count.keys())}")
print(f"Total Cost IC for Triangle Institutions per Institute:\n{pd.Series(TCsum, index=TCsum.keys())}")
print(f"Total awards count and cost are:\n{pd.Series(awards_count, index=awards_count.keys()).sum()}, {sum(TCsum.values())}")
