from flask import render_template, flash, request, url_for, redirect
from flask_login import login_required, current_user
from .models import products
from app import app, dbase
from string import capwords

@app.route('/itemlist')
@login_required
def index():
    allData = products.query.all()

    return render_template('index.html', name=current_user.username, products = allData)

#   CRUD System   #
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['itemName']
        desc = request.form['itemDesc']
        if request.form['rarity'] == 'None':
            rarity = None
        else:
            rarity = request.form['rarity']
        type = request.form['itemType']

        product = products(capwords(name), desc, rarity, type)
        dbase.session.add(product)
        dbase.session.commit()

        flash('Item Register Successful')

        return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        product = products.query.get(request.form.get('id'))

        product.itemName = capwords(request.form['itemName'])
        product.itemDesc = request.form['itemDesc']
        if request.form['rarity'] == 'None':
            product.rarity = None
        else:
            product.rarity = request.form['rarity']
        product.type = request.form['type']

        dbase.session.commit()
        flash('Item Update Successful')

        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    product = products.query.get(id)
    dbase.session.delete(product)
    dbase.session.commit()
    flash('Item Deleted Successfully')

    return redirect(url_for('index'))

#   Error handlers  #
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('error404.html')

@app.errorhandler(500)
def pageNotFound(e):
    return render_template('error500.html')