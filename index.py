from flask import Flask, jsonify, render_template, request
from Hash_Function_MD import MD4,MD5
from Hash_Function_SHA import SHA1,SHA256
from Hash_Function_HMAC import HMAC

app = Flask(__name__) #este se debe especificar en el Procfile asi : web: gunicorn index:app

# app variable para crear rutas del servidor y crear urls

@app.route('/') # ruta de pagina inicial
def home():
    return render_template('home.html')

##MD4
@app.route('/Hash_Function_MD4') # url Hash_Function_MD4: usando esta url puedo enviar mensaje por get, post o etc
#para llamar a esta funcion mediante esta llamada {{url_for('HF_MD4')}} en href
def HF_MD4():
    type_ = "MD4"
    return render_template('HF_MD4.html',HF_type = type_)

@app.route('/generate_HF_MD4' , methods=['POST']) 
def generateHFMD4():
    message= request.form['message_']
    result = MD4(message)
    return jsonify({'result' : result})

##MD5
@app.route('/Hash_Function_MD5') 
def HF_MD5():
    type_ = "MD5"
    return render_template('HF_MD5.html',HF_type = type_)

@app.route('/generate_HF_MD5' , methods=['POST']) 
def generateHFMD5():
    message= request.form['message_']
    result = MD5(message)
#     # print(result)
    return jsonify({'result' : result})

##SHA1
@app.route('/Hash_Function_SHA1') 
def HF_SHA1():
    type_ = "SHA1"
    return render_template('HF_SHA1.html',HF_type = type_)

@app.route('/generate_HF_SHA1' , methods=['POST']) 
def generateHFSHA1():
    message= request.form['message_']
    result = SHA1(message)
#     # print(result)
    return jsonify({'result' : result})


##SHA256
@app.route('/Hash_Function_SHA256') 
def HF_SHA256():
    type_ = 'SHA256'
    return render_template('HF_SHA256.html', HF_type = type_)

@app.route('/generate_HF_SHA256' , methods=['POST']) 
def generateHFSHA256():
    
    message= request.form['message_']
    result = SHA256(message)
#     # print(result)
    return jsonify({'result' : result})

##HMAC
@app.route('/Hash_Function_HMAC') 
def HF_HMAC():
    type_ = "HMAC"
    return render_template('HF_HMAC.html', HF_type = type_)

@app.route('/generate_HF_HMAC' , methods=['POST']) 
def generateHFHMAC():
    message= request.form['message_']
    key= request.form['key_']
    agl = request.form['agl_']
    # print(message)
    # print(key)
    # print(agl)
    result = HMAC(message,key,agl)
#     # print(result)
    return jsonify({'result' : result})


# este es el archivo que arrancara la aplicacion
if __name__ == "__main__":
    app.run(debug=True);