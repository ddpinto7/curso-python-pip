import utils
import read_csv
import charts
import pandas as pd
def run():
    '''
    data = read_csv.read_csv('world_population.csv')
    
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentage = list(map(lambda x: x['World Population Percentage'], data))
    '''
    df = pd.read_csv('world_population.csv')
    df = df[df['Continent'] == 'Africa']

    countries = df['Country/Territory'].values 
    percentage = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentage)

    data = read_csv.read_csv('world_population.csv')

    country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]

        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
        


if __name__ == '__main__':
    run()

            
        