# -*- coding: utf-8 -*-
#!/usr/bin/env python
import csv
import validador_archivo
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
import consultas, forms
from forms import Ingreso, Registro, BusquedaCliente, BusquedaProducto


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'un string que funcione como llave'


#Se valida que el archivo cumpla todas las condiciones necesarias para poder trabajar con el (validador_archivo.validate(archivo))
#Luego se Abre el archivo con la base de ventas, se verifica el formato de las columnas y el metodo "loadFile" devuelve el archivo en forma de lista
elarchivo = 'listado.csv'
validador_archivo.validate(elarchivo)
registros = forms.loadFile(elarchivo)


@app.route('/')
def index():
    return render_template('index.html', fecha_actual=datetime.utcnow())


@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500

@app.route("/login", methods = ["GET", "POST"])
def login():
    form = Ingreso()
    if form.validate_on_submit():
        with open('usuarios') as archivo:
            archivo_csv = csv.reader(archivo)
            registro = next(archivo_csv)
            while registro:
                if form.username.data == registro[0] and form.password.data == registro[1]:
                    flash("Sesion iniciada como " + form.username.data)
                    session['username'] = form.username.data
                    return render_template('home.html', usuario= form.username.data)
                registro = next(archivo_csv, None)
            else:
                flash("Usuario o contrasenia incorrectos")
                return redirect(url_for('login'))
    return render_template('ingresar.html', form = form)

@app.route("/returnhome", methods = ['GET', 'POST'])
def returnhome():
    if 'username' in session:
        return render_template('home.html', usuario= session['username'])    
    else:
        flash("Usuario o contrasenia incorrectos")
    return redirect(url_for('login'))    
         

@app.route("/registrarse", methods = ['GET', 'POST'])
def registrarse():
    form = Registro()
    if form.validate_on_submit():
        if form.password.data == form.re_password.data:
            with open ('usuarios', 'a+') as archivo:
                archivo_csv = csv.writer(archivo)
                registro = [form.username.data, form.password.data]
                archivo_csv.writerow(registro)
            flash('Usuario creado correctamente')
            return redirect(url_for('login'))
        else:
            flash('Las contrasenias deben ser iguales')
    return render_template('registrarse.html', formrg=form)


@app.route('/secret', methods=['GET'])
def secreto():
    if 'username' in session:
        return render_template('private.html', username=session['username'])
    else:
        return render_template('sin_permiso.html')

@app.route("/logout", methods = ['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template("index.html",fecha_actual=datetime.utcnow())
    else:
        flash('Salio correctamente')
        return redirect(url_for('login'))



@app.route("/home", methods = ['GET','POST'])
def home():
    if 'username' in session:
        return render_template("home.html")
    else:
        flash('Primero inicia sesion')
        return redirect(url_for('login'))

@app.route("/ultimasventas", methods = ['GET', 'POST'])
def show():
    if 'username' in session:
        cantidadregistros = 5
        listaventas = []
        listaventas = consultas.ultimas_ventas(registros, cantidadregistros)
        return render_template('ultimasventas.html', listaventas = listaventas)
    else:
        flash('Tenes que iniciar sesion')
        return redirect(url_for('login'))               

@app.route("/busquedaclientes", methods = ['GET', 'POST'])
def busquedaclientes():
    if 'username' in session:
        formcliente = BusquedaCliente()
        if formcliente.validate_on_submit():
            cliente = formcliente.campocliente.data.upper()
            if len(cliente) < 3:
                flash('Debe ingresar minimamente 3 caracteres')
                return render_template('busquedaclientes.html', form = formcliente)
            else:
                buscarclientes = consultas.buscar_cliente(registros, cliente)
                if len(buscarclientes) == 0:
                    flash('No hay resultados')
                elif len(buscarclientes) == 1:
                    listar = consultas.productos_cliente(registros, cliente)
                    return render_template('busquedaclientes.html', form = formcliente, listar = listar, cliente = formcliente.campocliente.data.upper())
                else:
                    return render_template('busquedaclientes.html', form = formcliente, clientes = buscarclientes)
        return render_template('busquedaclientes.html', form = formcliente)
    else:
        flash('Primero inicia sesion')
        return redirect(url_for('login'))

@app.route("/clientesmasgastaron", methods = ['GET', 'POST'])
def clientesregulares():
    if 'username' in session:
        clientes = []
        cantidad = 5
        clientes = consultas.clientes_masgastaron(registros = registros, cantidad = cantidad)
        return render_template('clientesmasgastaron.html', listaclientes = clientes)
    else:
        flash('Primero inicia sesion')
        return redirect(url_for('login'))        

@app.route("/busquedaproductos", methods = ['GET', 'POST'])
def buscarproductos():
    if 'username' in session:
        formproducto = BusquedaProducto()
        if formproducto.validate_on_submit():
            producto = formproducto.campoproducto.data.upper()
            if len(producto) < 3:
                flash('Debe ingresar minimamente 3 caracteres')
                return render_template('busquedaproducto.html', form = formproducto)
            else:
                res_pr = consultas.buscar_productos(registros, producto)
                if len(res_pr) == 0:
                    flash('No se encontraron productos')
                elif len(res_pr) == 1:
                    listar = consultas.lista_producto(registros, producto)
                    return render_template('busquedaproducto.html', form = formproducto, listar = listar, producto= formproducto.campoproducto.data.upper())
        return render_template('busquedaproducto.html', form = formproducto)
    else:
        flash ('Primero inicia sesion')
        return redirect(url_for('login'))  

@app.route("/masvendidos", methods = ['GET', 'POST'])
def masvendidos():
    if 'username' in session:
        productos = [] 
        cantidad = 5
        productos = consultas.masvendidos(registros = registros, cantidad = cantidad)
        return render_template('masvendidos.html', masvendidos = productos)
    else:
        flash('Primero inicia sesion')
        return redirect(url_for('login'))


if __name__ == "__main__":
    manager.run()
