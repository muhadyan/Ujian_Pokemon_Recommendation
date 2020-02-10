from flask import Flask, render_template, request
import requests
import saveModel as sm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil', methods = ['POST', 'GET'])
def hasil():
    if request.method == 'POST':
        input = request.form
        indexSuka = sm.df[sm.df['Name'] == str(input['pokemon'])].index[0]
        pokemonSama = list(enumerate(sm.cosScore[indexSuka]))
        pokemonSama = sorted(pokemonSama, key=lambda x:x[1], reverse=True)
        sm.df['Type 1'] = sm.label.inverse_transform(sm.df['Type 1'])
        d = {True: 'Legend',False: 'Not Legend'}
        sm.df['Legendary'] = sm.df['Legendary'].replace(d)
        PokRek = []
        for i in pokemonSama[:7]:
            PokRek.append(sm.df.iloc[i[0]][['Name', 'Type 1', 'Generation', 'Legendary']])
        # image = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu/').json()
        # image = image['sprites']['front_default']
        return render_template('hasil.html',
            data=input, recm=PokRek)

if __name__ == '__main__':
    app.run(debug=True)