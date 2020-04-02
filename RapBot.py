import tensorflow as tf
import tokenizer


def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim,
                                  batch_input_shape=[batch_size, None]),
        tf.keras.layers.LSTM(rnn_units,
                             return_sequences=True,
                             stateful=True,
                             recurrent_initializer='glorot_uniform'),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model


def generate_text(model, start_words, txt2id, id2txt):
    # Evaluation step (generating text using the learned model)
    start_string=""
    for w in start_words:
        start_string+=w+" "
    # Number of characters to generate
    num_generate = 1000

    # Converting our start string to numbers (vectorizing)
    input_eval = [txt2id[s] for s in start_words]
    input_eval = tf.expand_dims(input_eval, 0)

    # Empty string to store our results
    text_generated = []

    # Low temperatures results in more predictable text.
    # Higher temperatures results in more surprising text.
    # Experiment to find the best setting.
    temperature = 1.0

    # Here batch size == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # remove the batch dimension
        predictions = tf.squeeze(predictions, 0)

        # using a categorical distribution to predict the character returned by the model
        predictions = predictions / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()

        # We pass the predicted character as the next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(id2txt[predicted_id])

    return (start_string + ' '.join(text_generated))


MODEL = 'PHONEME-LEVEL'

if MODEL == "WORD-LEVEL":
    checkpoint_dir = './training_checkpoints_word_level'
else:
    checkpoint_dir = './training_checkpoints_phoneme_level'

print(tf.train.latest_checkpoint(checkpoint_dir))
txt2id, id2txt, text_as_int = tokenizer.getDictionaries_Phoneme_Level()

# Length of the vocabulary in chars
vocab_size = len(id2txt)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024

model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.build(tf.TensorShape([1, None]))

print(generate_text(model, ["<BEGINSONG>"], txt2id, id2txt))

