#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from extensions import checkAge
from sanic import Sanic, Blueprint
from sanic_jinja2 import SanicJinja2
from sanic.response import text, redirect
from factory import getMogodbConnection, getLimiter
from sanic_limiter import Limiter, RateLimitExceeded, get_remote_address
from data_access import dataAccessFactory, getUsers, isUserUnique, addUser, isUserUniqueByDocAndId, updateUser, findUserById, destroyUserById

app = Sanic(__name__)
limiter = getLimiter(app)
settings =  getMogodbConnection()
app.config.update(settings)
dataAccessFactory(app)
jinja = SanicJinja2(app, autoescape=True)

@app.route("/")
async def index(request):
    cur = await getUsers()
    return jinja.render('index.html', request, users=cur.objects)

@app.route('/new', methods=('GET', 'POST'))
async def new(request):
    if request.method == 'POST':
        name = request.form.get('name', '').strip().lower()
        age = request.form.get('age', '').strip()
        if name:
            is_uniq = await isUserUnique(doc=dict(name=name))
            if age:
                if age.isdigit() :
                    if is_uniq in (True, None) and checkAge(age):
                        await addUser(dict(name=name, age=int(age)))
                        request['flash']('User was added successfully', 'success')
                        return redirect(app.url_for('index'))
                    else:
                        request['flash']('This name was already taken', 'error')
        request['flash']('User name is required', 'error')
    return jinja.render('form.html', request, user={})

@app.route('/edit/<id>', methods=('GET', 'POST'))
async def edit(request, id):
    user = await findUserById(id)
    if not user:
        request['flash']('User not found', 'error')
        return redirect(app.url_for('index'))
    if request.method == 'POST':
        name = request.form.get('name', '').strip().lower()
        age = request.form.get('age', '').strip()
        if name:
            if age:
                if age.isdigit() :
                    doc = dict(name=name, age=int(age))
                    is_uniq = await isUserUniqueByDocAndId(doc=doc, id=user.id)
                    if is_uniq in (True, None):
                        # remove non-changed items
                        user.clean_for_dirty(doc)
                        if doc:
                            await updateUser({'_id': user.id}, {'$set': doc})

                        request['flash']('User was updated successfully', 'success')
                        return redirect(app.url_for('index'))
                    else:
                        request['flash']('This name was already taken', 'error')
        request['flash']('User name is required', 'error')
    return jinja.render('form.html', request, user=user)

@app.route('/destroy/<id>')
async def destroy(request, id):
    user = await findUserById(id)
    if not user:
        request['flash']('User not found', 'error')
        return redirect(app.url_for('index'))
    await destroyUserById(id)
    request['flash']('User was deleted successfully', 'success')
    return redirect(app.url_for('index'))

@app.exception(RateLimitExceeded)
@limiter.exempt
async def handle_429(request, exception):
    return jinja.render('error.html', request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)