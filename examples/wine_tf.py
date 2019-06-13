dataset = tf.data.Dataset.from_tensor_slices(
  (tf.cast(X, tf.float32), tf.cast(y, tf.int32)))

dataset = dataset.shuffle(1000).batch(32)

model = tf.keras.Sequential([
  tf.keras.layers.Dense(25, activation=tf.nn.relu, input_shape=(len(attributes),)),  # input shape required
  tf.keras.layers.Dense(25, activation=tf.nn.relu),
  tf.keras.layers.Dense(3)
])

def loss(mod, x, y):
    return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=mod(x))

def grad(mod, x, y):
    
    with tf.GradientTape() as tape:
        loss_value = loss(mod, x, y)
    return loss_value, tape.gradient(loss_value, mod.trainable_variables)

optimizer = tf.train.AdamOptimizer(learning_rate=0.01)

global_step = tf.train.get_or_create_global_step()

num_epochs = 100

for epoch in range(num_epochs):
    epoch_loss_avg = tfe.metrics.Mean()
    epoch_accuracy = tfe.metrics.Accuracy()

    # Training loop - using batches of 32
    for features, label in dataset:
        # Optimize the model
        loss_value, grads = grad(model, features, label)
        optimizer.apply_gradients(zip(grads, model.variables),
                                                            global_step)

        # Track progress
        epoch_loss_avg(loss_value)    # add current batch loss
        # compare predicted label to actual label
        epoch_accuracy(tf.argmax(model(features), axis=1, output_type=tf.int32), label)


epoch_accuracy.result()