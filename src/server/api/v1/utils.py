import datetime

import jwt
from werkzeug.security import generate_password_hash, check_password_hash

from api.v1.db import db_helper
from api.v1.db.db_models import UserModel
from api.v1.config import SECRET_KEY


def encode_auth_token(user_id):
    """
    Creating the token
    :param user_id: user's id which is recorded to th DB
    :return: unique token
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256')
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Decoding of the token
    :param auth_token: user's token
    :return: user's id
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please sign-in again"
    except jwt.InvalidTokenError:
        return "Invalid token. Please sign-in again"


def default(req, *args, **kwargs):
    """
    Root endpoint available at '/'
    :param req: request object
    :param args:
    :param kwargs:
    :return: server reply with status code 'OK' and message
    """
    req.serv_reply(200, {'message': 'Welcome to Warship Battle! Visit \'/register\' to get registered!'})


def path_not_found(req, *args, **kwargs):
    """
    Default handler called when client tries to access non-existed endpoint
    :param req: request object
    :param args:
    :param kwargs:
    :return: server reply with status code 'Not found' and message
    """
    req.serv_reply(404, {'message': 'Requested path is not found, please check the endpoint and try again'})


def login(req, data):
    """
    Functionality to perform login actions.
    Possible use cases:
    1. Provided correct credentials and user exists in DB -> token is generated and user's db data updated
    2. Provided incorrect credentials - 401 error returned
    3. Provided only username or only password - 401 error returned
    :param req: request object
    :param data: dict with provided username and password
    :return: user's token in case of success, 'Unauthorized' error in case if credentials validation failed
    """
    user = db_helper.UserDBHelper.user_exists(data)
    if not (data.get('nickname') and data.get('password')):
        req.serv_reply(401, {'message': 'Unauthorized. Username or password is invalid'})

    elif not (user and check_password_hash(user.passwd, data.get('password'))):
        req.serv_reply(401, {'message': 'Unauthorized. Username or password is invalid'})
    else:
        token = encode_auth_token(user.id)

        # data to be updated in the DB {<field_name>: <value>}
        data = {'token': token}
        db_helper.UserDBHelper.update(user.id, data)
        db_helper.db_connection.commit()
        req.serv_reply(200, {'token': token.decode('utf-8')})


def register(req, data):
    """
    New user registration procedure.
    Possible use cases:
    1. User provides credentials and user does not exist - new user registered
    2. User provides the nickname which is already exists in the DB - 'Conflict' status returned
    3. User does not provided whether username or password - 'Bad request' status returned
    :param req: request object
    :param data: dict with provided username and password
    :return: 'Created' status code in case of successful registration, 'Bad request' or 'Conflict' in case of
            credentials validation failed
    """
    if not (data.get('nickname') and data.get('password')):
        req.serv_reply(400, {'message': 'Username and password are mandatory'})
    elif not db_helper.UserDBHelper.user_exists(data):
        user_obj = db_helper.UserDBHelper(db_helper.db_connection)
        passwd = generate_password_hash(data.get('password'))
        user_obj.create(data.get('nickname'), passwd)
        req.serv_reply(201, {'message': 'User successfully created'})
    else:
        req.serv_reply(409, {'message': 'Username is already taken'})


def users(req):
    """
    Get all users list
    :param req: request object
    :return: json with all registered users
    """
    users = db_helper.db_connection.query(UserModel).all()
    response = {'users': []}
    for user in users:
        data = {'id': user.id, 'name': user.nickname}
        response['users'].append(data)
    req.serv_reply(200, response)


def get_user(req, uid):
    """
    Get particular user by id
    :param req: request object
    :param uid: user's id
    :return: json with user's data
    """
    try:
        user = db_helper.db_connection.query(UserModel).filter_by(id=uid).first()
        response = {'id': user.id, 'name': user.nickname}
        req.serv_reply(200, response)
    except AttributeError:
        req.serv_reply(400, {'message': f'User with id {uid} is not found'})


def dispatch_handler(req_obj, *args, **kwargs):
    """
    Mapper for endpoints accessed and handler functions
    :param req_obj: request object
    :param args:
    :param kwargs:
    :return: mapped function call with passed params
    """
    # I believe this is not the best solution to handle user id's in such way
    url_parts = req_obj.path.split('/')
    if req_obj.command == 'GET' and url_parts[-1].isdigit():
        return get_user(req_obj, (url_parts[-1]))

    elif req_obj.command == 'GET':
        return {
            '/': default,
            '/users': users,
            }.get(req_obj.path, path_not_found)(req_obj, *args, **kwargs)

    elif req_obj.command == 'POST':
        return {
            '/login': login,
            '/register': register
            }.get(req_obj.path, path_not_found)(req_obj, *args, **kwargs)
