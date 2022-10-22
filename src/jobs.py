import csv
from functools import lru_cache


@lru_cache
def read(path):

    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        jobs_list = [row for row in jobs_reader]
        return jobs_list


# noqa linha 38 estou dizendo que só vai rodar quando name tiver o valor de main ou seja
# noqa quando eu chamar diretamente se for chamado por outro lugar ou pelo teste  o nome main
# noqa muda para quem esta chamando entao nao atende a condiçao
# noqa linha 39 como minha funçao é read ou seja ela vai ler no caso um caminho path eu estou
# noqa passando e com a possiçao 0 pq sei que é uma lista, mas se eu nao sei o que é eu
# noqa nao passo a possiçao para ver o que esta trazendo
# if __name__ == "__main__":
#     print(read("src/jobs.csv")[0])
