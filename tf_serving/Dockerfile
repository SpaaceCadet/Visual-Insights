# Use the official TensorFlow Serving image as the base image
FROM tensorflow/serving

# Set the working directory to /models
WORKDIR /models

# Copy the model configurations and models to the container
COPY model_config.config .
COPY models/Multivariate_cnn_lstm /models/varcnnlstm
COPY models/MultivariateLstm3 /models/vanillalstm
COPY models/Multivariate_Lstm /models/varlstm

# Expose the ports required by TensorFlow Serving
EXPOSE 8500
EXPOSE 8501

# Set the command to run TensorFlow Serving with the specified model configurations
CMD ["tensorflow_model_server", "--model_config_file=/models/model_config.config"]
