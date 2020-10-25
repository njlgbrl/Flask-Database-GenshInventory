from flask import render_template, flash, redirect, url_for, request
from app.merchants import merchant
from app.models import merchants, wares, products
from app import dbase
from string import capwords

@merchant.route('/')
def all():
    allData = merchants.query.all()

    return render_template('merchants.html', merchants=allData)

#   CRUD System for all merchants   #
@merchant.route('/insert', methods=["POST", "GET"])
def allInsert():
    if request.method == "POST":
        name = capwords(request.form['name'])
        type = request.form['type'].capitalize()
        location = request.form['location'].capitalize()

        merchant = merchants(name, type, location)
        dbase.session.add(merchant)
        dbase.session.commit()
        flash('Merchant Register Successful')

        return redirect(url_for('merchant.all'))

@merchant.route('/update', methods=['POST', 'GET'])
def allUpdate():
    if request.method == "POST":
        merchant = merchants.query.get(request.form.get('id'))

        merchant.name = capwords(request.form['name'])
        merchant.type = request.form['type'].capitalize()
        merchant.location = request.form['location'].capitalize()

        dbase.session.commit()
        flash('Merchant Update Successful')

        return redirect(url_for('merchant.all'))

@merchant.route('/delete/<id>', methods=['POST', 'GET'])
def allDelete(id):
    merchant = merchants.query.get(id)
    
    dbase.session.delete(merchant)
    dbase.session.commit()
    flash('Merchant Deleted Successfully')

    return redirect(url_for('merchant.all'))

#   Merchants in Monstadt   #
@merchant.route('/mondstadt')
def mondstadt():
    allData = merchants.query.filter_by(location="Mondstadt").all()

    return render_template('mondstadt.html', merchants=allData)

@merchant.route('/mondstadt/<name>/wares', methods=['POST', 'GET'])
def mondstadtWares(name):
    merchantData = merchants.query.filter_by(name=name).first()
    allProducts = products.query.all()
    allData = wares.query.join(merchants, wares.merchantID == merchants.id).join(products, wares.productID == products.id).add_columns(products.itemName, wares.stock, wares.price, wares.productID, merchants.name, wares.ID, merchants.location, merchants.id).filter(wares.merchantID==merchantData.id).order_by(wares.price.asc())

    return render_template('wares.html', wares=allData, merchant=merchantData, allProducts=allProducts)

#   CRUD for Mondstadt   #
@merchant.route('/mondstadt/insert', methods=["POST", "GET"])
def mondstadtInsert():
    if request.method == "POST":
        name = capwords(request.form['name'])
        type = request.form['type'].capitalize()
        location = request.form['location'].capitalize()

        merchant = merchants(name, type, location)
        dbase.session.add(merchant)
        dbase.session.commit()
        flash('Merchant Register Successful')

        return redirect(url_for('merchant.mondstadt'))

@merchant.route('/monstadt/update', methods=['POST', 'GET'])
def mondstadtUpdate():
    if request.method == "POST":
        merchant = merchants.query.get(request.form.get('id'))

        merchant.name = capwords(request.form['name'])
        merchant.type = request.form['type'].capitalize()
        merchant.location = request.form['location'].capitalize()

        dbase.session.commit()
        flash('Merchant Update Successful')

        return redirect(url_for('merchant.mondstadt'))

@merchant.route('/mondstadt/delete/<id>', methods=['POST', 'GET'])
def mondstadtDelete(id):
    merchant = merchants.query.get(id)
    
    dbase.session.delete(merchant)
    dbase.session.commit()
    flash('Merchant Deleted Successfully')

    return redirect(url_for('merchant.mondstadt'))

#   Merchants in Liyue   #
@merchant.route('/liyue')
def liyue():
    allData = merchants.query.filter_by(location="liyue").all()

    return render_template('liyue.html', merchants=allData)

@merchant.route('/liyue/<name>/wares', methods=['POST', 'GET'])
def liyueWares(name):
    merchantData = merchants.query.filter_by(name=name).first()
    allProducts = products.query.all()
    allData = wares.query.join(merchants, wares.merchantID == merchants.id).join(products, wares.productID == products.id).add_columns(products.itemName, wares.stock, wares.price, wares.productID, merchants.id, wares.ID, merchants.location, merchants.name).filter(wares.merchantID==merchantData.id).order_by(wares.price.asc())

    return render_template('wares.html', wares=allData, merchant=merchantData, allProducts=allProducts)

#   CRUD for Liyue   #
@merchant.route('/liyue/insert', methods=["POST", "GET"])
def liyueInsert():
    if request.method == "POST":
        name = capwords(request.form['name'])
        type = request.form['type'].capitalize()
        location = request.form['location'].capitalize()

        merchant = merchants(name, type, location)
        dbase.session.add(merchant)
        dbase.session.commit()
        flash('Merchant Register Successful')

        return redirect(url_for('merchant.liyue'))

@merchant.route('/liyue/update', methods=['POST', 'GET'])
def liyueUpdate():
    if request.method == "POST":
        merchant = merchants.query.get(request.form.get('id'))

        merchant.name = capwords(request.form['name'])
        merchant.type = request.form['type'].capitalize()
        merchant.location = request.form['location'].capitalize()

        dbase.session.commit()
        flash('Merchant Update Successful')

        return redirect(url_for('merchant.liyue'))

@merchant.route('/liyue/delete/<id>', methods=['POST', 'GET'])
def liyueDelete(id):
    merchant = merchants.query.get(id)
    
    dbase.session.delete(merchant)
    dbase.session.commit()
    flash('Merchant Deleted Successfully')

    return redirect(url_for('merchant.liyue'))

#   CRUD FOR WARES   #
@merchant.route('/wares/update', methods=['POST'])
def wareUpdate():
    if request.method == 'POST':
        ware = wares.query.get(request.form.get('ID'))
        merchantName = request.form['merchantName']
        location = request.form['location'].lower()

        ware.merchantID = request.form['mID']
        ware.productID = request.form['pID']
        ware.stock = request.form['stock']
        ware.price = request.form['price']

        dbase.session.commit()
        flash('Ware Update Successful')

        return redirect(f'/merchants/{location}/{merchantName}/wares')

@merchant.route('/<location>/<name>/wares/delete/<id>')
def wareDelete(id, name, location):
    ware = wares.query.get(id)

    dbase.session.delete(ware)
    dbase.session.commit()
    flash('Ware Deleted Successfully')

    return redirect(f'/merchants/{location}/{name}/wares')

@merchant.route('/wares/insert', methods=['POST'])
def wareInsert():
    location = request.form['location'].lower()
    merchantName = request.form['merchantName']
    if request.method == 'POST':
        merchantID = request.form['merchantID']
        productID = request.form['item']
        stock = request.form['stock']
        price = request.form['price']

        ware = wares(merchantID, productID, stock, price)
        dbase.session.add(ware)
        dbase.session.commit()
        flash('Ware Register Successful')

        return redirect(f'/merchants/{location}/{merchantName}/wares')