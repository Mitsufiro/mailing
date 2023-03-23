from models import Client as ModelClient
from models import Message as ModelMessage
from models import User as ModelUser
from fastapi_sqlalchemy import db


def get_client_by_tag(client_tag):
    client = db.session.query(ModelClient).filter(ModelClient.tag == client_tag).all()
    return client


def get_user_by_name(name):
    user = db.session.query(ModelUser).filter(ModelUser.username == name).first()
    return user.username


def get_client_by_telnum(telnum):
    tel_num = db.session.query(ModelClient).filter(ModelClient.tel_num == telnum).first()
    return tel_num.tel_num


def get_item(model, item_id):
    return db.session.query(model).get(item_id)


def get_items(model):
    items = db.session.query(model).all()
    return items


def delete_item(model, item_id):
    if get_item(model, item_id):
        deleted_item = get_item(model, item_id)
        db.session.delete(get_item(model, item_id))
        db.session.commit()
        return deleted_item
    else:
        return 'Wrond id'


def filter_of_messages(id_of_mailing: int, status: str):
    filtred_message_by_status = db.session.query(ModelMessage).filter(ModelMessage.mailing_id == id_of_mailing).filter(
        ModelMessage.status == status)
    return filtred_message_by_status
