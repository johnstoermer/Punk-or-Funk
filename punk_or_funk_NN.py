import tensorflow as tf

#input layer
x = tf.placeholder(tf.float32, [None, 12])

#ground truth output
y = tf.placeholder(tf.float32, [None, 2])

#weights and biases for the first layer
W1 = tf.Variable(tf.zeros([12, 20]))
b1 = tf.Variable(tf.zeros([20]))

#weights and biases for second layer
W2 = tf.Variable(tf.zeros([20, 2]))
b2 = tf.Variable(tf.zeros([2]))

#model output
y_hat = tf.nn.softmax(tf.matmul(tf.nn.sigmoid(tf.matmul(x , W1 ) + b1), W2) + b2)

#cross entropy loss
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(y_hat), reduction_indices=[1]))

#train model using gradient descent
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#initialize tf session
sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

#training loop


#Checks if the final model guess is equal to the ground truth value
correct_prediction = tf.equal(tf.argmax(y_hat,1), tf.argmax(y,1))

#Casts the correct_prediction vector to floating point numbers to calculate mean accuracy
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#Prints accuracy of model
print("Accuracy: ", sess.run(accuracy, feed_dict={x: , y: }))
