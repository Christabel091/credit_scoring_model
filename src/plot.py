import matplotlib.pyplot as plt
import pandas as pd
def main():
    df = pd.read_csv("patients.csv")
    print(df.head())
    #drop colunms with missing values
    df = df[["Age", "Sex","Na_to_K"]].dropna()
    #assign each colunm to their appropriate data type
    df["Age"] = df["Age"].astype(int)
    df["Na_to_K"] = df["Na_to_K"].astype(float)

     # Map gender to colors
    color_map = {'M': 'red', 'F': 'blue'}
    df['color'] = df['Sex'].map(color_map)
    #plot the graph w
    plt.scatter(df["Age"], df["Na_to_K"], label="patients age to potasuim", c=df["color"])
    plt.legend()
    plt.title("patients plot")
    plt.xlabel("age of patients")
    plt.ylabel("potasuim of patients")
    plt.savefig("patientss.png")
    plt.show()
   
main()