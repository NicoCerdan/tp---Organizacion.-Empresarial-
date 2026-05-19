#aca creo el archivo analisis.py dentro de la carpeta scripts
print("El trabajo practico me pide que haga comentarios tecnicos, esto no lo entendi muy bien, pero creo que es asi como lo estoy haciendo")
print("Investigue y si usas un solo signo % solo se guarda lo que escribo en una misma linea (%writefile scripts/analisis.py print(Algo asi entendi))")
print("Y al usar %% se guarda en el archivo creado todo lo que escriba debajo sin necesidad de hacerlo en una misma linea")

%%writefile /content/tp---Organizacion.-Empresarial-/README.md
# TRABAJO PRÁCTICO – GESTIÓN COLABORATIVA, CONTROL DE VERSIONES Y ORGANIZACIÓN EMPRESARIAL

## Integrantes
- Nicolás Cerdán

## Escenario elegido
**Escenario D – Resultados Deportivos**

## Descripción del dataset
El archivo `annual.csv` contiene registros de resultados segun datahub.io    
Los datos fueron almacenados en la carpeta `/datos`.

## Estructura del repositorio
- /datos/ → contiene el dataset (`annual.csv`).  
- /scripts/ → contiene el script `analisis.py` con comentarios técnicos.  
- /resultados/ → incluye gráficos e informes generados (`resultados.jpg`).  
- README.md → documentación del proyecto.  
- .gitignore → exclusión de archivos innecesarios.

## Instrucciones de ejecución
1. Clonar el repositorio.  
2. Ejecutar el script `scripts/analisis.py` en Python Colab.  
3. Los resultados se guardaron en la carpeta `/resultados`.

## Trazabilidad con Jira
Los commits realizados en GitHub están vinculados a issues en Jira.  
Ejemplo: `NC32-2: Creación de analisis.py`.
