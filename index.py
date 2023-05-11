import pandas as pd
import json


# Colocar el nombre del archivo json en la misma carpeta que este archivo
with open('datos.json', 'r') as file:
    data = json.load(file)

# Aca Colocar el campo de donde se quieren extraeran los datos
data_field = data['data']


filtered_data = []


for obj in data_field:
    filtered_obj = {}
    
    # Aca se coloca que campos se quieren extraer dentro que estan dentro de data
    filtered_obj['lastName'] = obj.get('lastName')
    filtered_obj['name'] = obj.get('name')
    filtered_obj['cuil'] = obj.get('cuil')
    
    # Verificar si el campo "role" contiene la etiqueta "Proveedor", en caso de querer chequear otra etiqueta cambiar el valor de proveedor por la etiqueta deseada
    roles = obj.get('role')
    if roles:
        for role in roles:
            if 'label' in role and role['label'] == 'Proveedor':
                filtered_obj['role'] = 'Proveedor'
                break
    
    filtered_data.append(filtered_obj)

df = pd.DataFrame(filtered_data)

# Aqui escribir el nombre que se le quiere dar al archivo excel
df.to_excel('datos.xlsx', index=False)
