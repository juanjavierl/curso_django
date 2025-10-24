from django.db import models

# Create your models here.
# los modelos son las tablas de la base de datos
# cada modelo representa una tabla en la base de datos
# los atributos del modelo representan las columnas de la tabla
""""
CREATE TABLE Categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    descripcion TEXT
);
    """
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"