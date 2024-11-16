import tensorflow as tf
if tf.config.list_physical_devices("GPU"):
    print("GPU available")
else:
    print("GPU not found")