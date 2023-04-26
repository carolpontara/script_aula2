#!/usr/bin/env python3

import subprocess

#Definindo o nome do usuário e a senha

new_user_name = "Carol"
new_user_password = "password123"


#Cria uo usúario no sistema Linux

subprocess.run(["sudo","useradd",new_user_name])
subprocess.run(["sudo","passwd",new_user_name], input=f"{new_user_password}\n{new_user_password}\n".encode())

