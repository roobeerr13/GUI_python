from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "sqlite:///movimientos.db"  # Cambia la URL si usas otra base de datos
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definición del modelo Movimiento
class Movimiento(Base):
    __tablename__ = 'movimientos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    monto = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)  # Ejemplo: "ingreso" o "egreso"

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Función para agregar un movimiento
def agregar_movimiento(descripcion, monto, tipo):
    nuevo_movimiento = Movimiento(descripcion=descripcion, monto=monto, tipo=tipo)
    session.add(nuevo_movimiento)
    session.commit()

# Función para obtener todos los movimientos
def obtener_movimientos():
    return session.query(Movimiento).all()

# Ejemplo de uso
if __name__ == "__main__":
    # Agregar un movimiento
    agregar_movimiento("Venta de producto", 150.0, "ingreso")
    agregar_movimiento("Compra de insumos", -50.0, "egreso")

    # Obtener y mostrar todos los movimientos
    movimientos = obtener_movimientos()
    for movimiento in movimientos:
        print(f"ID: {movimiento.id}, Descripción: {movimiento.descripcion}, Monto: {movimiento.monto}, Tipo: {movimiento.tipo}")