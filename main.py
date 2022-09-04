import Grafo as gf
import os



def get_emails(file):
    txt_filtre = [i.replace(" ", "").replace("\n", "").replace("\t", "") for i in file.readlines()]
    get_Subject = [i for i in txt_filtre if "Subject:" in i][0]
    real_txt = txt_filtre[:txt_filtre.index(get_Subject)]
    get_From = [i for i in txt_filtre if "From:" in i][0].split(":")[1]
    get_To = [i for i in txt_filtre if "To:" in i][0]
    list_To = real_txt[real_txt.index(get_To):]
    list_To = [i.replace("To:", "").replace("'", "").replace(">", "").split(",") for i in list_To]
    all_emails_to = []
    for i in list_To:
        if type(i) == list:
            for email in i:
                if email != '':
                    all_emails_to.append(email)
        elif i != '':
            all_emails_to.append(i)
    return [get_From, all_emails_to]

def condition_From_To(file):
    txt_filtre = [i.replace(" ", "").replace("\n", "").replace("\t", "") for i in file.readlines()]
    get_Subject = [i for i in txt_filtre if "Subject:" in i][0]
    real_txt = txt_filtre[:txt_filtre.index(get_Subject)]
    if len([i for i in real_txt if "From:" in i or "To:" in i]) >= 2:
        return True
    return False



def main():
    grafo = gf.GRAFO()
    for files in os.listdir("./dataset"):
        for emails in os.listdir("./dataset/"+files):
            for txt in os.listdir("./dataset/"+files+"/"+emails):
                file1 = open("./dataset/" + files + "/" + emails + "/" + txt, "r")
                if condition_From_To(file1):
                    file = open("./dataset/"+files+"/"+emails+"/"+txt, "r")
                    From, To = get_emails(file)
                    grafo.adiciona_vertice(From)
                    for email in To:
                        grafo.adiciona_vertice(email)
                        grafo.adiciona_aresta(From, email, 1)
    grafo.imprime_lista_adjacencias()
    print(grafo.numero_vertices())
    print(grafo.numero_arrestas())



if __name__ == '__main__':
    main()