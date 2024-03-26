import pandas as pd

# homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018. The 'individuals' column 
# is the number of homeless individuals not part of a family with children. The 'family_members' column is the number 
# of homeless individuals part of a family with children. The 'state_pop' column is the state's total population.

homelessness = {'region': ['East South Central', 'Pacific', 'Mountain', 'West South Central', 'Pacific', 'Mountain', 'New England',
                   'South Atlantic', 'South Atlantic', 'South Atlantic', 'South Atlantic', 'Pacific', 'Mountain',
                   'East North Central', 'East North Central', 'West North Central', 'West North Central', 'East South Central',
                   'West South Central', 'New England', 'South Atlantic', 'New England', 'East North Central',
                   'West North Central', 'East South Central', 'West North Central', 'Mountain', 'West North Central',
                   'Mountain', 'New England', 'Mid-Atlantic', 'Mountain', 'Mid-Atlantic', 'South Atlantic', 'West North Central',
                   'East North Central', 'West South Central', 'Pacific', 'Mid-Atlantic', 'New England', 'South Atlantic',
                   'West North Central', 'East South Central', 'West South Central', 'Mountain', 'New England', 'South Atlantic',
                   'Pacific', 'South Atlantic', 'East North Central', 'Mountain'],
        'state': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                  'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
                  'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 
                  'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
                  'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
                  'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                  'West Virginia', 'Wisconsin', 'Wyoming'],
        'individuals': [2570.0, 1434.0, 7259.0, 2280.0, 109008.0, 7607.0, 2280.0, 708.0, 3770.0, 21443.0, 6943.0, 4131.0,
                        1297.0, 6752.0, 3776.0, 1711.0, 1443.0, 2735.0, 2540.0, 1450.0, 4914.0, 6811.0, 5209.0, 3993.0,
                        1024.0, 3776.0, 983.0, 1745.0, 7058.0, 835.0, 6048.0, 1949.0, 39827.0, 6451.0, 467.0, 6929.0,
                        2823.0, 11139.0, 8163.0, 747.0, 3082.0, 836.0, 6139.0, 19199.0, 1904.0, 780.0, 3928.0, 16424.0,
                        1021.0, 2740.0, 434.0],
        'family_members': [864.0, 582.0, 2606.0, 432.0, 20964.0, 3250.0, 1696.0, 374.0, 3134.0, 9587.0, 2556.0, 2399.0,
                           715.0, 3891.0, 1482.0, 1038.0, 773.0, 953.0, 519.0, 1066.0, 2230.0, 13257.0, 3142.0, 3250.0,
                           328.0, 2107.0, 422.0, 676.0, 486.0, 615.0, 3350.0, 602.0, 52070.0, 2817.0, 75.0, 3320.0,
                           1048.0, 3337.0, 5349.0, 354.0, 851.0, 323.0, 1744.0, 6111.0, 972.0, 511.0, 2047.0, 5880.0,
                           222.0, 2167.0, 205.0],
        'state_pop': [4887681, 735139, 7158024, 3009733, 39461588, 5691287, 3571520, 965479, 701547, 21244317, 10511131,
                      1420593, 1750536, 12723071, 6695497, 3148618, 2911359, 4461153, 4659690, 1339057, 6035802, 6882635, 
                      9984072, 5606249, 2981020, 6121623, 1060665, 1925614, 3027341, 1353465, 8886025, 2092741, 19530351,
                      10381615, 758080, 11676341, 3940235, 4181886, 12800922, 1058287, 5084156, 878698, 6771631, 28628666,
                      3153550, 624358, 8501286, 7523869, 1804291, 5807406, 577601]}

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
print(ind_gt_10k)

# Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg
mountain_reg = df[df["region"] == "Mountain"]
print(mountain_reg)

# Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific",
# assigning to fam_lt_1k_pac
fam_lt_1k_pac = df[(df["family_members"] < 1000) & (df["region"] == "Pacific")]
print(fam_lt_1k_pac)

# --- Subsetting rows by categorical variables ---
# Filter homelessness for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic", assigning to south_mid_atlantic
regions = ["South Atlantic", "Mid-Atlantic"]
south_mid_atlantic = df[df["region"].isin(regions)]
print(south_mid_atlantic)

# Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness
canu = ["California", "Arizona", "Nevada", "Utah"]
mojave_homelessness = df[df["state"].isin(canu)]
print(mojave_homelessness)

# --- Adding columns ---
# Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
df["total"] = df["individuals"] + df["family_members"]

# Add p_individuals col as proportion of total that are individuals
df["p_individuals"] = df["individuals"]/df["total"]
print(df)

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

# See the result
print(result)
print('District of Columbia has the highest number of homeless individuals - almost 54 per ten thousand people.')
print('This is almost double the number of the next-highest state, Hawaii')