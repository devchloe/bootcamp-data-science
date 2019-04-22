import plotly
from plotly.offline import plot, init_notebook_mode
init_notebook_mode(True)


lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann" \
         " You Got Me Rockin'And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann ...More Lyrics..." \
         " Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"
print(lyrics)

list_of_lyrics = lyrics.split(' ')
list_of_lyrics
unique_words = set(list_of_lyrics)
word_histogram = dict.fromkeys(unique_words, 0)
for word in list_of_lyrics:
    word_histogram[word] = word_histogram[word] + 1
    print(word_histogram[word])

print(len(unique_words))

trace = {'type': 'bar', 'x': list(unique_words), 'y': list(word_histogram.values())}

plot({'data': [trace]})
