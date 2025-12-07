import matplotlib.pyplot as plt

# Dataset: 2024 Quarterly Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
mrr_growth = [4.28, 4.1, 9.21, 10.5]

# Benchmarks
industry_target = 15
calculated_average = sum(mrr_growth) / len(mrr_growth) # This equals 7.02

def analyze_performance():
    print(f"Average MRR Growth: {calculated_average}")
    print(f"Target: {industry_target}")
    
    if calculated_average < industry_target:
        print("Status: Underperforming against industry benchmarks.")

def create_visualization():
    plt.figure(figsize=(10, 6))
    
    # Plotting the MRR Growth
    plt.plot(quarters, mrr_growth, marker='o', label='Actual MRR Growth', color='blue', linewidth=2)
    
    # Plotting the Target Line
    plt.axhline(y=industry_target, color='red', linestyle='--', label=f'Industry Target ({industry_target})')
    
    # Plotting the Average Line
    plt.axhline(y=calculated_average, color='green', linestyle=':', label=f'Year Avg ({calculated_average})')

    plt.title('SaaS MRR Growth vs Industry Target (2024)', fontsize=14)
    plt.xlabel('Quarter')
    plt.ylabel('Growth Percentage')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the plot
    plt.savefig('growth_trend.png')
    print("Visualization saved as growth_trend.png")

if __name__ == "__main__":
    analyze_performance()
    create_visualization()
