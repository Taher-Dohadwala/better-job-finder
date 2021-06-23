"""
This script trains and retrains the recommendation model for the job finder platform

All self supervised job description labels are stored in data/searches

This script takes that labeled data, and fine-tunes the DistilBert transformer model from Huggingface

The model will train for 20 epochs which will take ~5-10 mins to train (on gpu)
*Recommended to copy data and training script into colab for execution*
"""
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification
import os

PATH = "data/searches"
SAVE_PATH = "models/recommendation"
# uncomment below to train on google colab
'''
from google.colab import drive
drive.mount('/content/drive')
PATH = "/content/drive/My Drive/data/searches"
'''

def prepare_dataset():
    pass
    sentences = []
    labels = []
    # read each csv
    # find all that are interesting and label 1, find all unintesting and label 0
    # ignore unread
    files = [f"{PATH}/{file}" for file in os.listdir(PATH) if file.endswith(".csv")]
    
    X_train, X_test, y_train, y_test = train_test_split(sentences, labels, test_size=0.1,stratify=labels, random_state=42)
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
    train_encodings = tokenizer(X_train,truncation=True,padding=True)
    val_encodings = tokenizer(X_test,truncation=True,padding=True)


    train_dataset = tf.data.Dataset.from_tensor_slices((
        dict(train_encodings),
        y_train
    ))
    val_dataset = tf.data.Dataset.from_tensor_slices((
        dict(val_encodings),
        y_test
    ))
    return train_dataset, val_dataset

if __name__ == '__main__':
    train_dataset, val_dataset = prepare_dataset()
    model = TFDistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased',num_labels=2)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
        loss=model.compute_loss)
    
    model.fit(
        train_dataset.shuffle(16).batch(8),
        epochs=20,
        batch_size=8,
        validation_data=val_dataset.shuffle(16).batch(8),
        )
    model.save_pretrained(SAVE_PATH)
