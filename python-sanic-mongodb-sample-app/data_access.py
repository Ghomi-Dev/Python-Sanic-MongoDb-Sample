from sanic_motor import BaseModel

def dataAccessFactory(app):
    BaseModel.init_app(app)

class User(BaseModel):
    __coll__ = 'users'
    __unique_fields__ = ['name']

async def getUsers(): 
    return await User.find(sort='name, age desc')

async def isUserUnique(doc):
    return await User.is_unique(doc)

async def addUser(doc):
    return await User.insert_one(doc)

async def isUserUniqueByDocAndId(doc, id):
    return await User.is_unique(doc, id)

async def updateUser(id, doc):
    return await User.update_one({'_id': id}, {'$set': doc})

async def findUserById(id):
    return await User.find_one(id)

async def destroyUserById(id):
    user = await findUserById(id)
    return user.destroy()