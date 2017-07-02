import binascii
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation

training_data = [
    ('0a1c429bc6f204cc323ba25ef802fc2c', 'ogjx'),
    ('0b07e5e8458107a37074a3f9413697df', 'd1xz'),
    ('0b67ee034c1f65c319cba123fa6c85df', 'mrth'),
    ('0b93e6d64fd4d3c8d537b2aac3dc43b4', 'bkqr'),
    ('0b6414582322cbcb87cf3859d27c7af7', 'r9fd'),
    ('7fd700f74a37bf98e1c1d8be2dbec240', '2581'),
    ('9e37b011828dd2058547fdef5c685a8d', 'cy1w'),
    ('9604ff600095f2ee051c0ee065c031c9', 'by92'),
    ('a462c2e6fab64b16191993d7452ffe21', '1uf7'),
    ('ca9cb83731dd4bd3a6d649c589993e83', '7xx2'),
    ('cdb3205e060d7366023b76790e7e06ef', '8d8y'),
    ('d70497e568bc6de31e651241ccb55dfc', 'gcbz'),
    ('dd6fb5c48cd33b3944b461fa565d5a61', 'd7dh'),
    ('fcf7e7f1643020bb4233f8ae23332259', 'zzaq'),
    ('f858e8eac73b61abf3b8cd190ebe8906', 'hgyb')
]

predict = 'ff27f7ac3c4596b03d39f04263fab616'
answer = '3obg'

def to_bin_array(string):
    bin_string = binascii.unhexlify(string)
    arr = []
    for char in bin_string:
        arr.append(char == '1')
    return arr

def to_target_array(string):
    bin_string = ''.join(format(ord(x), 'b') for x in string)

    arr = []
    for char in bin_string:
        arr.append(char == '1')
    return arr

def from_target_array(arr):
    bin_string = ''
    for val in arr:
        if val:
            bin_string += 1
        else:
            bin_string += 0
    bin_string = binascii.hexlify(bin_string)
    return bin_string.decode("hex")

model = Sequential()
model.add(Dense(units=64, input_shape=(128,)))
model.add(Activation('relu'))
model.add(Dense(64))
model.add(Activation('softmax'))
model.add(Dense(32))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.05, momentum=0.9, nesterov=True))

bin_arrays = []
targets = []
for datum in training_data:
    bin_arrays.append(to_bin_array(datum[0]))
    targets.append(to_target_array(datum[1]))

model.fit(bin_arrays, targets)
print from_target_array(model.predict(predict))
