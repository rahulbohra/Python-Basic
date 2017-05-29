def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print greet('en'), "World"
print greet('es'), "Mundo"
print greet('fr'), "le monde"
