import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Generate synthetic dataset
    np.random.seed(42)
    n_students = 1000
    genders = np.random.choice(["Male", "Female"], size=n_students, p=[0.6, 0.4])
    marks_math = np.random.randint(40, 100, size=n_students)
    marks_physics = np.random.randint(35, 95, size=n_students)
    marks_chemistry = np.random.randint(30, 90, size=n_students)

    df = pd.DataFrame({
        "Gender": genders,
        "Math": marks_math,
        "Physics": marks_physics,
        "Chemistry": marks_chemistry,
        "Total": marks_math + marks_physics + marks_chemistry
    })

    # Visualization: subject-wise performance
    plt.hist(df["Math"], bins=10, alpha=0.7, label="Math")
    plt.hist(df["Physics"], bins=10, alpha=0.7, label="Physics")
    plt.hist(df["Chemistry"], bins=10, alpha=0.7, label="Chemistry")
    plt.legend()
    plt.title("Subject-wise Performance Distribution")
    plt.show()

    # Gender-based comparison
    df.groupby("Gender")["Total"].mean().plot(kind="bar", color=["blue", "pink"])
    plt.title("Average Total Marks by Gender")
    plt.show()

if __name__ == "__main__":
    main()
