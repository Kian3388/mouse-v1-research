from pynwb import NWBHDF5IO
import pandas as pd

file_path = r"C:\Users\kianb\Projects\mouse-v1-research\data\session_757216464\session_757216464.nwb"
io=NWBHDF5IO(file_path, mode="r")
nwbfile = io.read()
#print(nwbfile.session_id)
#print(nwbfile.session_description)
#print(nwbfile.session_start_time)
#print(nwbfile.institution)

#print("Total units:", len(nwbfile.units))
#print("Unit columns:", nwbfile.units.colnames)
units_df = nwbfile.units.to_dataframe()
# KEEP THIS ONE                           print(units_df.head())

io.close()

channels=pd.read_csv("data/channels.csv")
#print(channels.head())
#print(channels.columns.to_list())

# KEEP THIS ONE                           print(channels["ecephys_structure_acronym"].value_counts())
# KEEP THIS ONE                           print(sum(channels["ecephys_structure_acronym"] == "VISp"))


merged_df = pd.merge(units_df, channels, left_on='peak_channel_id', right_on='id', how='left')
# KEEP THIS ONE                           print(len(merged_df))
# KEEP THIS ONE                           print(merged_df["ecephys_structure_acronym"].isna().sum())

# KEEP THIS ONE                           print(sum(merged_df["ecephys_structure_acronym"]=="VISp"))

visp_units = merged_df[merged_df["ecephys_structure_acronym"] == "VISp"]
print(visp_units["quality"].value_counts())

print(channels["id"].duplicated().sum())