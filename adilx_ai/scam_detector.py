import onnxruntime as ort
import numpy as np

# ONNX model load karna
model_path = "scam_detection.onnx"
session = ort.InferenceSession(model_path)

# Dummy input data (Baad me blockchain data ke saath replace karenge)
dummy_input = np.random.rand(1, 512).astype(np.float32)

# Model prediction lena
outputs = session.run(None, {"input": dummy_input})

print("🔍 Scam Detection AI Output:", outputs)
