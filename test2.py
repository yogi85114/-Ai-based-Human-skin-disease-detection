import traceback
try:
    from predict import predict_disease
    r = predict_disease('static/0198796099f44715b1af3809aaf35b94.jpeg')
    print("SUCCESS:", r[0], r[1])
except:
    traceback.print_exc()

