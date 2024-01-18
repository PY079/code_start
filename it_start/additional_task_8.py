import os, turtle as tr
from sqlalchemy import create_engine, Column, Integer, String, Table
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import create_engine

path = fr'{os.path.dirname(__file__)}\database.db'

# Создайте асинхронный движок SQLAlchemy
engine = create_engine(f'sqlite:///{path}', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine) 


class DB(Base):
    __tablename__ = 'data_cords'
    id=Column(Integer,default=1,primary_key=True)
    x=Column(String)
    y=Column(String)

# Base.metadata.create_all(bind=engine)

def add_x(x):
    with Session() as session:
        x_=session.query(DB).where(DB.id==1)
        x_x=x_.scalar()
        if x_x:
            x_x.x=x
            
        else:
            new_x=DB(x=x)
            session.add(new_x)
        session.commit()


def add_y(y):
    with Session() as session:
        y_=session.query(DB).where(DB.id==1)
        y_y=y_.scalar()
        if y_y:
            y_y.y=y
            
        else:
            new_y=DB(y=y)
            session.add(new_y)
        session.commit()


def get_x():
    with Session() as session:
        x_=session.query(DB).where(DB.id==1)
        x_x=x_.scalar()
        if x_x: return x_x.x

def get_y():
    with Session() as session:
        y_=session.query(DB).where(DB.id==1)
        y_y=y_.scalar()
        if y_y: return y_y.y



def turl(x,y):
    obj=tr.Turtle()
    obj.speed(10)
    obj.penup()
    obj.goto(x)
    obj.pendown()
    obj.goto(y)



while True:
    print('1. Изменить X\n2. Изменить Y\n0. Выйти')
    inp=int(input('Введи номер.. '))
    if inp ==1:
        inp2=int(input('Введи значение x.. '))
        add_x(inp2)

    elif inp==2:        
        inp3=int(input('Введи значение y.. '))
        add_y(inp3)
    elif inp==0: break
    os.system('cls')
    x=get_x()
    y=get_y()
    print(f'В бд --- x: {x}, y:{y}')
    turl(x,y)


    
    
