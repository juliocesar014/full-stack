# import json
import boto3

s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cessao_fundo")


def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    nome_do_arquivo = event["Records"][0]["s3"]["object"]["key"]
    csv_object = s3_client.get_object(Bucket=bucket, Key=nome_do_arquivo)
    file = csv_object["Body"].read().splitlines()

    print(len(file))
    for line in file[1:]:
        campos = str(line).split(";")
        print(campos[11])
        table.put_item(
            Item={
                "originador": campos[0],
                "doc_originador": campos[1],
                "cedente": campos[2],
                "doc_cedente": campos[3],
                "ccb": campos[4],
                "id_externo": campos[5],
                "cliente": campos[6],
                "cpf_cnpj": campos[7],
                "endereco": campos[8],
                "cep": campos[9],
                "cidade": campos[10],
                "uf": campos[11],
                "valor_do_emprestimo": campos[12],
                "valor_parcela": campos[14],
                "total_parcelas": campos[19],
                "parcela": campos[20],
                "data_de_emissao": campos[23],
                "data_de_vencimento": campos[24],
                "preco_de_aquisicao": campos[26],
            }
        )

    return "Sucesso!!"
