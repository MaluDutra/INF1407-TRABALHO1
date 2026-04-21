# INF1407 - TRABALHO 1

# Songlist

## Integrantes
- Érica Regnier
- Maria Luiza Dutra

## Descrição do Projeto
O **Songlist** é um site desenvolvido com o objetivo de permitir que cada usuário monte e gerencie sua própria playlist pessoal.

Para utilizar o sistema, o usuário pode criar uma conta e realizar login. Após estar autenticado, ele pode cadastrar músicas em sua playlist, visualizar todas as músicas cadastradas, editar informações de músicas já existentes e removê-las quando desejar.

Além do gerenciamento da playlist, o sistema também oferece funcionalidades relacionadas à conta do usuário, como visualização de perfil, atualização de dados, troca de senha e redefinição de senha.

---

## Escopo do Site
O sistema foi desenvolvido com a proposta de funcionar como um gerenciador de playlist pessoal, permitindo ao usuário:

- criar uma conta;
- realizar login;
- cadastrar músicas;
- visualizar suas músicas cadastradas;
- editar músicas;
- remover músicas;
- acessar a página de perfil;
- atualizar dados do usuário;
- trocar a senha;
- redefinir a senha, caso necessário.

---

## Tecnologias Utilizadas
- **Python**
- **Django**
- **HTML**
- **CSS**
- **SQLite** (banco de dados padrão do Django)

---

## Funcionalidades Implementadas

### Controle de usuário
- cadastro de usuário;
- login;
- logout;
- visualização de perfil;
- atualização de dados do usuário;
- troca de senha;
- redefinição de senha.

### Playlist
- cadastro de músicas;
- listagem de músicas;
- edição de músicas;
- remoção de músicas.

### Dados das músicas
Cada música pode conter:
- título;
- artista;
- álbum;
- gênero;
- ano de lançamento;
- imagem por URL;
- link para ouvir a música;

### Dados do usuário
Cada usuário pode possuir:
- nome de usuário;
- e-mail;
- senha;
- foto de perfil por URL;
- música favorita;
---

## Navegação do Site

### Usuário não autenticado
Ao acessar o sistema sem estar logado, o usuário encontra as seguintes opções principais:

- **Início**: leva à página inicial do site;
- **Login**: permite entrar no sistema com nome de usuário e senha;
- **Criar conta**: permite o cadastro de um novo usuário.

### Usuário autenticado
Após realizar login, o usuário passa a ter acesso às funcionalidades principais do sistema:

- **Início**: retorna para a página principal;
- **Músicas**: mostra a playlist pessoal do usuário;
- **Adicionar música**: permite cadastrar uma nova música;
- **Perfil**: exibe as informações do usuário;
- **Atualizar dados**: permite editar informações do usuário;
- **Trocar senha**: permite alterar a senha da conta;
- **Sair**: encerra a sessão do usuário.

---

## Manual do Usuário

Esta seção descreve o funcionamento do site de forma que qualquer pessoa consiga utilizá-lo.

### 1. Acesso à página inicial
Ao abrir o site, o usuário visualiza a página inicial, que apresenta a proposta do sistema e sua navegação principal.

### 2. Cadastro
Caso ainda não tenha uma conta, o usuário deve acessar a opção **Criar conta** e preencher os dados solicitados. Após o cadastro, o sistema permite o acesso às funcionalidades internas.

### 3. Login
Se o usuário já estiver cadastrado, ele pode acessar a página de **Login** e informar seu nome de usuário e senha para entrar no sistema.

### 4. Perfil
Após entrar no sistema, o usuário pode acessar sua página de **Perfil**, onde visualiza:
- nome de usuário;
- e-mail;
- foto de perfil;
- música favorita.

### 5. Atualização de dados
Na área de atualização de dados, o usuário pode alterar:
- nome de usuário;
- e-mail;
- foto de perfil por URL;
- música favorita.

### 6. Cadastro de músicas
Na funcionalidade de cadastro, o usuário pode adicionar músicas à sua playlist, preenchendo os dados disponíveis no formulário.

### 7. Visualização da playlist
Na página de músicas, o usuário pode visualizar apenas as músicas cadastradas por ele no sistema.

### 8. Edição de músicas
Caso deseje alterar dados de uma música já cadastrada, o usuário pode acessar a funcionalidade de edição.

### 9. Remoção de músicas
Caso deseje excluir uma música da playlist, o usuário pode utilizar a funcionalidade de remoção.

### 10. Troca de senha
O sistema possui uma funcionalidade específica para troca de senha, permitindo ao usuário atualizar suas credenciais de acesso.

### 11. Redefinir senha
Caso o usuário esqueça a senha, ele pode utilizar a funcionalidade de redefinição de senha.

Ao solicitar essa ação, as instruções de redefinição são exibidas no terminal/console da aplicação. Assim, para utilizar corretamente essa funcionalidade em ambiente de desenvolvimento, é necessário observar a mensagem gerada no terminal.

### 12. Logout
Ao finalizar o uso do sistema, o usuário pode sair da conta por meio da funcionalidade de logout.

---

## O que Foi Testado e Funcionou
Durante o desenvolvimento do projeto, foram testadas e funcionaram as seguintes funcionalidades:

- cadastro de usuário;
- login;
- logout;
- listagem de músicas;
- cadastro de músicas;
- edição de músicas;
- remoção de músicas;
- visualização do perfil do usuário;
- atualização de dados do usuário;
- seleção de música favorita;
- salvamento de foto de perfil por URL;
- troca de senha;
- redefinição de senha com exibição das instruções no terminal;
- navegação entre as principais páginas do sistema.

---

## O que Foi Testado e Não Funcionou
Até o momento da entrega, não foram identificadas falhas relevantes nas funcionalidades principais do sistema.

---

## Observações Importantes
- Cada usuário visualiza e gerencia apenas suas próprias músicas.
- O projeto foi desenvolvido com foco em organização de playlists pessoais.
- A foto de perfil é armazenada por meio de URL.
- A música favorita é selecionada entre as músicas cadastradas pelo próprio usuário.
- A funcionalidade de redefinição de senha exibe as instruções no terminal/console da aplicação.

---

## Como Executar o Projeto

1. Abrir o terminal na pasta do projeto.
2. Criar e ativar o ambiente virtual, se necessário.
3. Instalar o Django.
4. Rodar as migrações.
5. Executar o servidor local.


### Link para o site hospedado no render

https://inf1407-trabalho1.onrender.com/


### Comandos

```bash
python -m venv venv
source venv/bin/activate

(venv) pip install -r requirements.txt

(venv) python manage.py makemigrations
(venv) python manage.py migrate
(venv) python manage.py runserver


