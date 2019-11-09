# Step 1. Import the necessary libraries
import numpy as np
import pandas as pd
import geonamescache
# Step 2. Import the dataset Euro_2012_stats_TEAM¶

# Step 3. Assign it to a variable called euro12.
euro12 = pd.read_csv('Euro_2012_stats_TEAM.csv')

# Step 4. Select only the Goal column.
goal_column = pd.read_csv('Euro_2012_stats_TEAM.csv', usecols=['Goals'])
print("Goal_Columns \n", goal_column)


# Step 5. How many team participated in the Euro2012?¶
team_participate = pd.read_csv('Euro_2012_stats_TEAM.csv', usecols=['Team'])
team_info = len(team_participate)
print("Team info \n", team_info)



# Step 6. What is the number of columns in the dataset?¶
total_col = len(euro12.axes[1])
print("Total_Num_Col \n", total_col)


# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
view_only = pd.read_csv('Euro_2012_stats_TEAM.csv', usecols = ['Team', 'Yellow Cards', 'Red Cards'])
pd_df_view_only = pd.DataFrame(view_only)
print("Team , Yellow Cards , Red Cards Columns \n",pd_df_view_only)


# Step 8. Sort the teams by Red Cards, then to Yellow Cards¶
sort_by_yellow_team = pd_df_view_only.sort_values(by = 'Yellow Cards')
sort_by_red_team = pd_df_view_only.sort_values(by = 'Red Cards')

print("Sort by Red Team \n",sort_by_red_team)
print("sort By Yellow Cards \n",sort_by_yellow_team)


# Step 9. Calculate the mean Yellow Cards given per Team¶

print("Yellow Cards mean per Team \n",euro12["Yellow Cards"].mean())

# Step 10. Filter teams that scored more than 6 goals

select_2_columns = euro12.iloc[:,0:2]
goal_6 = select_2_columns[select_2_columns["Goals"] >= 6]
print("Goals 6 \n" , goal_6)

# Step 11. Select the teams that start with G¶

np_array_team = np.array(team_participate)
for item in np_array_team:
      for g in item:
            if g.startswith("G"):
                  print(' Teams names that start with G \n',g)

# Step 12. Select the first 7 columns¶

first_7_columns = euro12.iloc[:,0:8]
print("First 7 Columns \n",first_7_columns)

# Step 13. Select all columns except the last 3.¶

last_3= euro12.iloc[:,0:32]
print("All Cloumns Except last 3 \n",last_3)

# Step 14. Present only the Shooting Accuracy from England, Italy and Russia¶

shooting_accuracy_data = euro12.loc[:,['Team','Shooting Accuracy']]
shooting_accuracy = shooting_accuracy_data.loc[[3,7,12],:]
print("Shooting Accuracy \n", shooting_accuracy)

# Step 15. Use apply method on Goal Column to make a new column called Performance, using following conditions¶

def f(row):
      if row['Goals'] <= 2:
            val = "Below Average"
      elif row['Goals'] > 2 and row['Goals'] <= 5:
            val = "Average"
      elif row['Goals'] > 5 and row['Goals'] <= 10:
            val = "Above Average"
      elif row['Goals'] > 10 :
            val = "Excellent"
      return val

new_column = euro12.loc[:,['Team','Goals']]
new_column_sort = new_column.sort_values(by = "Goals" )
new_column_sort['Performance'] = new_column_sort.apply(f, axis = 1)
print(new_column_sort)