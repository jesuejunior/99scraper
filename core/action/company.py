from alchemytools.context import managed
from core.db import Session
from core.db.company import Company

__author__ = 'jesuejunior'

def company_create(data):
    with managed(Session) as session:
        company = session.query(Company).filter_by(title=data['title']).all()
    if company:
        return False
    else:
        with managed(Session) as session:
            company = Company(path=data['path'], about=data['about'], mission=data['mission'], follows=data['follows'],
                              vacancy=data['vacancy'], rank=data['rank'], title=data['title'], thumb=data['thumb'])
            session.add(company)
        return True

def _set_path(data):
    with managed(Session) as session:
        company = session.query(Company).filter_by(title=data['title']).all()[0]
        company.path = data['path']
        session.add(company)

def updater(data):
    with managed(Session) as session:
        company = session.query(Company).filter_by(title=data['title']).all()[0]
        company.path = data['path']
        session.add(company)
