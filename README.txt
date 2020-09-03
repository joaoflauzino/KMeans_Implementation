# KMeans_Implementation

- Para executar o código é necessário:

    - incluir o arquivo que será processado na pasta dataset.

    - informar os argumentos de acordo com a lista abaixo:

        inputFile - o nome do arquivo que será processado. É importante que ele não tenha espaços no nome, pois o código entenderá como um novo argumento e dará erro.
        
        sep - identificador de nova coluna
        
        dec - identificador de casa decimal
        
        outputFile - nome do arquivo que será gerado com os resultados
        
        K - numero de grupos 
        
        n_iter - numero de iterações que será realizada pelo algoritmo

    - exemplo de chamada do código no prompt:
        python kmeans.py -inputFile Mall_Customers.csv -sep , -dec . -outputFile results.csv -K 3

    - o arquivo processado será escrito na pasta output.

    - serão gerados dois gráficos na pasta output

    - é necessário que tenha as bibliotecas matplotlib, argparse e pandas instaladas no ambiente, caso não tenha, instalar utilizando os seguintes comandos no prompt:
        - pip install matplotlib
        - pip install argparse
        - pip install pandas