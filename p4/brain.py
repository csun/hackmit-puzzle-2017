import sys
import random
import image_gen
from keras.models import load_model
from PIL import Image
import numpy

from keras.models import model_from_json
with open('model.json', 'r') as myfile:
    model_json=myfile.read().replace('\n', '')
model = model_from_json(model_json)
model.load_weights('model.hdf5')
population = []
scores = [0] * 100
for _ in range(100):
    population.append(numpy.uint8(numpy.random.rand(1, 32, 32, 3) * 255))


def gen_population():
    global population, scores

    winners = sorted(zip(population, scores), key=lambda x: x[1], reverse=True)[:5]
    print('Current best score: ' + str(winners[0][1]))

    population = [x[0] for x in winners]
    while len(population) < 100:
        parent = population[random.randint(0, 4)]
        child = numpy.array(parent, copy=True)
        mutate(child)
        population.append(child)


def mutate(child):
    for _ in range(100):
        x = random.randint(0, 31)
        y = random.randint(0, 31)
        chan = random.randint(0, 2)
        delta = random.randint(-50, 50)

        child[0][x][y][chan] = max(0, min(255, child[0][x][y][chan] + delta))

while(image_gen.predimage() != 1):
    for index, indiv in enumerate(population):
        result = model.predict(indiv)

        if result[0][1] == max(result[0]):
            #print('DONE')
            img = Image.fromarray(indiv[0])
            img.save('automobile.png')
            #sys.exit(0)
        img = Image.fromarray(indiv[0])
        img.save('automobile.png')
        scores[index] = result[0][1]

    gen_population()
