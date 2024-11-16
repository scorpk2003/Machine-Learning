from keras.models import load_model
from keras.utils import plot_model

model = load_model('fake_news_rnn_model.h5')

# model.summary()

# plot_model(model, to_file="Fake_News.png")