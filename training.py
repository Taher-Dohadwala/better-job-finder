import pandas as pd
import numpy as np
import tensorflow as tf
from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow, blue

df = pd.read_csv("data/combined_data_withlabels_300.csv")

last_label = int(df.index[df["Label"] == 999].tolist()[0])
sentences = df["Job Description"].iloc[0:last_label].values.tolist()
labels = df["Label"].iloc[0:last_label].values.tolist()

train_percentage = 0.9

training_size = int(len(sentences)*train_percentage)
training_sentences = sentences[0:training_size]
validation_sentences = sentences[training_size:]
training_labels = labels[0:training_size]
validation_labels = labels[training_size:]
print(type(training_sentences))

tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

train_encodings = tokenizer(training_sentences,truncation=True,padding=True)
val_encodings = tokenizer(validation_sentences,truncation=True,padding=True)


train_dataset = tf.data.Dataset.from_tensor_slices((
    dict(train_encodings),
    training_labels
))
val_dataset = tf.data.Dataset.from_tensor_slices((
    dict(val_encodings),
    validation_labels
))

model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased',
                                                              num_labels=2)
print(model.summary())

optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)
model.compile(optimizer=optimizer, loss=model.compute_loss, metrics=[tf.keras.metrics.Recall(),tf.keras.metrics.Precision()])
model.fit(train_dataset.shuffle(50).batch(16),
          epochs=1,
          batch_size=8,
          validation_data=val_dataset.shuffle(50).batch(16))

model.save_pretrained("tmp/job_interest")

"""
def make_prediction(loaded_model,example):
    predict_input = tokenizer.encode(example,
                                 truncation=True,
                                 padding=True,
                                 return_tensors="tf")
    tf_output = loaded_model.predict(predict_input)[0]
    tf_prediction = tf.nn.softmax(tf_output, axis=1).numpy()[0]
    pred = tf.argmax(tf_prediction)
    return pred


loaded_model = TFDistilBertForSequenceClassification.from_pretrained("/tmp/job_interest")

#make_prediction(loaded_model,validation_sentences)
results = []
for s in validation_sentences:
    results.append(make_prediction(loaded_model,s))

for p in results:
    if p == 0:
        print(red("NOT INTERESTING"))
    else:
        print(green("INTERSTING"))
"""