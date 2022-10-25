# Standalone Build com Python Tests

Esse repositório demonstra alguns testes automatizados utilizando o modelo de PageObjects e AltUnityTester.

## Build instrumentado
O app/game deve passar pelo processo de build instrumentado através do asset AltUnity Tester a ser instalado dentro da plataforma de desenvolvimento Unity. 
O Game deve ficar na pasta App/  junto com todos os outros arquivos gerados durante o build.


### Instalando as dependências de projeto
Certifique-se de ter instalado uma versão Python a partir da 3.7, na raiz do projeto crie um ambiente virtual com pyhthon:
```
python3 -m venv venv
```

Ative o ambiente virtual com:
```
source venv/Scripts/activate
```

Agora instale as depedências do projeto:
```
pip install -r requirements.txt
```

### Executando os testes no Windows
Os testes devem ser executados em uma máquina Windows. o game fornecido neste repositório está localizado na pasta App/.
Para executar os testes:
```
./run_test_windows.sh
```

OBS: Lembre-se de sempre ativar o ambiente virtual do Python (venv) antes de executar os testes automatizados.

O script de testes irá executar:

- Abertura do game .exe no computador
- executar os testes automatizados
- encerrar o game após a execução dos testes
