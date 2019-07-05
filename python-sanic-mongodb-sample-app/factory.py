from sanic_limiter import Limiter, get_remote_address

def getMogodbConnection():
    return  dict(MOTOR_URI='mongodb://mongodbx:27017/main',
                    LOGO=None,
                    )
def getLimiter(app):                    
    return Limiter(app, global_limits=['5 per minute'], key_func=get_remote_address)                    