import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout, SpatialDropout1D
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.callbacks import EarlyStopping
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Bước 1: Tải dữ liệu
data = pd.read_csv('train.csv', delimiter = ";")  # Đảm bảo tên file là đúng với file dữ liệu của bạn
data_test = pd.read_csv('test.csv', delimiter = ";")
# Giả định dữ liệu có 2 cột: 'text' (nội dung bài báo) và 'label' (0 là tin thật, 1 là tin giả)

# Xử lý dữ liệu
X_train = data['title'].values + data['text'].values
Y_train = data['label'].values

X_test = data_test['title'].values + data_test['text'].values
Y_test = data_test['label'].values

# Chia tập dữ liệu thành train/test
# x_train, y_train = train_test_split(X_train, Y_train)
# x_test, y_test = 

# Tokenization
tokenizer = Tokenizer(num_words=5000, oov_token='<OOV>')
tokenizer.fit_on_texts(X_train)

# Chuyển đổi văn bản thành chuỗi số
X_train_sequences = tokenizer.texts_to_sequences(X_train)
X_test_sequences = tokenizer.texts_to_sequences(X_test)

# Đệm chuỗi để có độ dài bằng nhau
max_sequence_len = 250
X_train_padded = pad_sequences(X_train_sequences, maxlen=max_sequence_len, padding='post')
X_test_padded = pad_sequences(X_test_sequences, maxlen=max_sequence_len, padding='post')

# Bước 2: Tạo mô hình LSTM
embedding_dim = 128
model = Sequential([
    Embedding(input_dim=5000, output_dim=embedding_dim, input_length=max_sequence_len),
    SpatialDropout1D(0.2),
    LSTM(100, dropout=0.2, recurrent_dropout=0.2),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Bước 3: Huấn luyện mô hình
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
history = model.fit(X_train_padded, Y_train, validation_data=(X_test_padded, Y_test),
                    epochs=10, batch_size=64, callbacks=[early_stopping], verbose=1)

# Bước 4: Đánh giá mô hình và xuất độ chính xác
y_pred_prob = model.predict(X_test_padded)
y_pred = (y_pred_prob > 0.5).astype(int)

accuracy = accuracy_score(Y_test, y_pred)
print(f"Độ chính xác của mô hình: {accuracy:.4f}")
print("Báo cáo phân loại:")
print(classification_report(Y_test, y_pred))

# Lưu mô hình
model.save('fake_news_rnn_model.h5')

# Lưu tokenizer để dùng lại khi dự đoán
with open('tokenizer.pkl', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
