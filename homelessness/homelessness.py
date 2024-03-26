import pandas as pd

# homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018. The 'individuals' column 
# is the number of homeless individuals not part of a family with children. The 'family_members' column is the number 
# of homeless individuals part of a family with children. The 'state_pop' column is the state's total population.

homelessness = pd.read_csv("homelessness.csv")

df = pd.DataFrame(homelessness)

#print(df)

# --- Basic methods ---
# Print the head of the homelessness data
#print(df.head())

# Print information about homelessness
#print(df.info())

# Print the shape of homelessness
#print(df.shape)

# Print a description of homelessness
#print(df.describe())

# Print the values of homelessness
#print(df.values)

# Print the column index of homelessness
#print(df.columns)

# Print the row index of homelessness
#print(df.index)

# --- Sorting ----
# Sort homelessness by the number of homeless individuals, from smallest to largest, and save this as homelessness_ind.
# Print the head of the sorted DataFrame.
#homelessness_ind = df.sort_values("individuals")
#print(homelessness_ind.head())

# Sort homelessness by the number of homeless family_members in descending order, and save this as homelessness_fam.
# Print the head of the sorted DataFrame.
#homelessness_fam = df.sort_values("family_members", ascending = False)
#print(homelessness_fam.head())

# Sort homelessness first by region (ascending), and then by number of family members (descending). Save this as homelessness_reg_fam.
# Print the head of the sorted DataFrame.
#homelessness_reg_fam = df.sort_values(["region", "family_members"], ascending = [True, False])
#print(homelessness_reg_fam.head())

# --- Columns ---
# Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
# Print the head of the result.

#state_fam = df[["state", "family_members"]]
#print(state_fam.head())

# --- Rows ---
# Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. 
ind_gt_10k = df[df["individuals"] > 10000]

# Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg
mountain_reg = df[df["region"] == "Mountain"]

# Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific",
# assigning to fam_lt_1k_pac
fam_lt_1k_pac = df[(df["family_members"] < 1000) & (df["region"] == "Pacific")]
#print(fam_lt_1k_pac)

# --- Subsetting rows by categorical variables ---
# Filter homelessness for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic", assigning to south_mid_atlantic
regions = ["South Atlantic", "Mid-Atlantic"]
south_mid_atlantic = df[df["region"].isin(regions)]
#print(south_mid_atlantic)

# Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness
canu = ["California", "Arizona", "Nevada", "Utah"]
mojave_homelessness = df[df["state"].isin(canu)]
#print(mojave_homelessness)

# --- Adding columns ---
# Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
df["total"] = df["individuals"] + df["family_members"]

# Add p_individuals col as proportion of total that are individuals
df["p_individuals"] = df["individuals"]/df["total"]
#print(df)

# --- Combo attack! ---
# In this exercise, you'll answer the question, "Which state has the highest number of homeless individuals per 10,000 people in the state?"

# Create indiv_per_10k col as homeless individuals per 10k state pop
df["indiv_per_10k"] = 10000 * df["individuals"] / df["state_pop"] 

# Subset rows for indiv_per_10k greater than 20
high_homelessness = df[df["indiv_per_10k"] > 20] 

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending = False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

state_with_highest_homelessness = high_homelessness_srt.iloc[0]["state"]
state_with_2nd_highest_homelessness = high_homelessness_srt.iloc[1]["state"]

# See the result
print(result)
print(state_with_highest_homelessness, 'has the highest number of homeless individuals - almost 54 per ten thousand people.')
print('This is almost double the number of the next-highest state,', state_with_2nd_highest_homelessness)