import requests

apiEndpoint = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
response = requests.get(apiEndpoint)
data = response.json()

print(data)
population_data = data['data']
source = data['source'][0]['annotations']['source_name']
years = len(population_data)
start_year = population_data[0]['Year']
end_year = population_data[-1]['Year']

# Getting peak growth and lowest growth
peak_growth = max(population_data, key=lambda x: x['Population'])['Population']
peak_growth_year = max(population_data, key=lambda x: x['Population'])['Year']
lowest_growth = min(population_data, key=lambda x: x['Population'])['Population']
lowest_growth_year = min(population_data, key=lambda x: x['Population'])['Year']

# Growth percentages
peak_growth_percentage = (peak_growth - population_data[0]['Population']) / population_data[0]['Population'] * 100
lowest_growth_percentage = (lowest_growth - population_data[0]['Population']) / population_data[0]['Population'] * 100

output = f"According to {source}, in {years} years from {start_year} to {end_year}, peak population growth was {peak_growth_percentage:.2f}% in {peak_growth_year} and the lowest population increase was {lowest_growth_percentage:.2f}% in {lowest_growth_year}."
print(output)