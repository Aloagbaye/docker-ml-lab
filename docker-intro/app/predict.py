import sys
import json
import numpy as np


def predict(x):
    x = np.array(x, dtype=float)
    return (3.0 * x + 1.0).tolist()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        xs = json.loads(sys.argv[1])
    else:
        xs = [0, 1, 2, 3]
    ys = predict(xs)
    print(json.dumps({"input": xs, "output": ys}))
