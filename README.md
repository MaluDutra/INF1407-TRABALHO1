# INF1407-TRABALHO1

# Songlist

## Integrantes
- Érica Regnier
- Maria Luiza Dutra

## Descrição do Projeto
O **Songlist** é um site desenvolvido com o objetivo de permitir que cada usuário monte e gerencie sua própria playlist pessoal.

Para utilizar o sistema, o usuário pode criar uma conta e realizar login. Após estar autenticado, ele pode cadastrar músicas em sua playlist, visualizar todas as músicas cadastradas, editar informações de músicas já existentes e removê-las quando desejar.

Além do gerenciamento da playlist, o sistema também oferece funcionalidades relacionadas à conta do usuário, como visualização de perfil, atualização de dados, troca de senha e redefinição de senha.

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

## Tecnologias Utilizadas
- **Python**
- **Django**
- **HTML**
- **CSS**
- **SQLite** (banco de dados padrão do Django)

## Funcionalidades Implementadas
As funcionalidades previstas para o sistema incluem:

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
- imagem;
- link para ouvir a música;
- música favorita no perfil do usuário.

## Manual do Usuário
Esta seção descreve como utilizar o sistema.

### 1. Acessar a página inicial
Ao abrir o site, o usuário encontra a página inicial, que apresenta a proposta do sistema e a navegação principal.

### 2. Criar conta
Caso ainda não tenha cadastro, o usuário deve acessar a opção **Criar conta** e preencher os dados solicitados.

### 3. Fazer login
Após o cadastro, o usuário pode entrar no sistema utilizando seu nome de usuário e senha.

### 4. Editar dados do usuário
Depois de autenticado, o usuário pode acessar sua área de perfil e editar informações pessoais, como nome de usuário, e-mail, foto de perfil e música favorita.

### 5. Cadastrar músicas
Na área da playlist, o usuário pode adicionar músicas à sua lista, informando os dados disponíveis no formulário.

### 6. Visualizar músicas
O sistema possui uma página onde o usuário pode visualizar todas as músicas cadastradas em sua playlist pessoal.

### 7. Editar músicas
Caso deseje alterar informações de uma música já cadastrada, o usuário pode acessar a opção de edição.

### 8. Remover músicas
Caso deseje excluir uma música da playlist, o usuário pode utilizar a funcionalidade de remoção.

### 9. Trocar senha
Na área do usuário, existe a opção de troca de senha para atualização das credenciais da conta.

### 10. Redefinir senha
Caso o usuário esqueça a senha, ele pode solicitar a redefinição da senha por meio da funcionalidade correspondente.

## O que foi testado e funcionou
> **Preencher com o que está funcionando de fato no projeto.**

Exemplo de estrutura:
- [ ] cadastro de usuário;
- [ ] login;
- [ ] logout;
- [ ] listagem de músicas;
- [ ] cadastro de músicas;
- [ ] edição de músicas;
- [ ] remoção de músicas;
- [ ] perfil do usuário;
- [ ] atualização de dados;
- [ ] troca de senha;
- [ ] redefinição de senha;
- [ ] seleção de música favorita;
- [ ] foto de perfil por URL.

## O que foi testado e não funcionou
> **Preencher com honestidade aquilo que foi testado e apresentou erro, ou que não foi concluído.**

Exemplo de estrutura:
- [ ] redefinição de senha por e-mail;
- [ ] atualização de foto de perfil;
- [ ] seleção de música favorita;
- [ ] estilização de determinada página;
- [ ] links externos para ouvir música;
- [ ] outros comportamentos incompletos.

## Observações Importantes
- Cada usuário visualiza e gerencia apenas suas próprias músicas.
- O projeto foi desenvolvido com foco em organização de playlists pessoais.
- Algumas funcionalidades podem depender de configuração adicional do ambiente para funcionar corretamente.

## Como executar o projeto
1. Abrir o terminal na pasta do projeto.
2. Criar e ativar o ambiente virtual, se necessário.
3. Instalar o Django.
4. Rodar as migrações.
5. Executar o servidor local.

Exemplo de comandos:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver