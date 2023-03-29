# Extract all GADM regions that are present in the mining data
gid = facilities.loc[:, facilities.columns.str.startswith('GID')].drop_duplicates()
print(len(gid))

# split the ";"-separated values and explode the resulting lists for all columns
# do this to every row
for row in range(len(gid)):
    temp_df = gid.iloc[[row],:]
    display(temp_df)

    df_clean = temp_df.assign(GID_1=df_clean['GID_1'].str.split(';')).explode('GID_1').reset_index(drop=True)
    df_clean = df_clean.assign(GID_2=df_clean['GID_2'].str.split(';')).explode('GID_2').reset_index(drop=True)
    df_clean = df_clean.assign(GID_3=df_clean['GID_3'].str.split(';')).explode('GID_3').reset_index(drop=True)
    df_clean = df_clean.assign(GID_4=df_clean['GID_4'].str.split(';')).explode('GID_4').reset_index(drop=True)

    display(df_clean)
    if row == 0:
        unique_gadm = temp_df

    else: 
        pd.concat([unique_gadm, temp_df]).reset_index(drop=True)

unique_gadm.drop_duplicates(inplace = True)

###############################


# Extract all GADM regions that are present in the mining data
gid = facilities.loc[:, facilities.columns.str.startswith('GID')].drop_duplicates()

# split strings by ";"
for GID in ["GID_0", "GID_1", "GID_2", "GID_3", "GID_4"]:
    
    # split column
    gid_cols = gid[GID].str.split(";", expand=True)

    # rename columns
    ncols = gid_cols.shape[1]
    col_names = [GID + "_"] * ncols
    idx = list(range(ncols))
    idx = [str(i) for i in idx]
    col_names = [str1 + str2 for str1, str2 in zip(col_names, idx)]
    gid_cols.columns = col_names

    # combine again with the rest of the dataframe
    gid = pd.concat([gid.drop(GID, axis = 1), gid_cols], axis = 1)

# split the ";"-separated values and explode the resulting lists
df_clean = df.assign(Col1=df['Col1'].str.split(';')).explode('Col1').reset_index(drop=True)
df_clean = df_clean.assign(Col2=df_clean['Col2'].str.split(';')).explode('Col2').reset_index(drop=True)
