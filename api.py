from flask import Flask, request, jsonify, make_response
import joblib
import pandas as pd
import mapper_data
import db

app = Flask(__name__)
lda = joblib.load("lda_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = mapper_data.MapperData.mapper(request.json)
    sample = pd.DataFrame([data])
    for col, le in label_encoders.items():
        if col != "class":
            sample[col] = sample[col]

    # Certifique-se de que a amostra tem a forma correta
    if len(sample.shape) == 1:
        sample = pd.DataFrame([sample])
    else:
        sample = pd.DataFrame(sample)

    prediction = lda.predict(sample)
    result = label_encoders["class"].inverse_transform(prediction)
    if result[0] == "1":
        resposta = "Digno de Crédito"
    elif result[0] == "0":
        resposta = "Não é digno de Crédito"
    dadoCombinado = {"resposta": resposta, "dados": data}
    db.SaveData(dadoCombinado)
    return make_response(jsonify(resultado=resposta, atrubutos=data))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
