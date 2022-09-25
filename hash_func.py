import pandas as pd
import hashlib as hl
import os

def getSentences():    
    dict1 = {
        'sentence' : "A primeira das instituições criadas por Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.",
        'sha256' : "dc22d5778028c3a9764c17f6b3525faed47acab8ce52adb974e5b4740e7df584",
        'md5' : "1fb73598032cdddd59edbd1361eab82e"
    }

    dict2 = {
        'sentence' : "A FEI é uma Instituição vinculada estatutariamente à Companhia de Jesus",
        'sha256' : "bcdc1b145c216e7672616cd4fd65e743dcbcb7dfbd7898da207623c46608bba2",
        'md5' : "8375bf9b5e583cac0480dceda0e0af32"
    }
    
    dict3 = {
        'sentence' : "Em 20 de janeiro de 1952 foi realizada a sessão solene da Congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.",
        'sha256' : "ca11b74ca85c72a15d9f488eec58813a7aece4245d79b4947f34353f08f349a3",
        'md5' : "cefa90b6b32782cc41e899f8ccc3ef2c"
    }
    
    dict4 = {
        'sentence' : "A Capela Santo Inácio de Loyola foi construída em 1978, em concreto aparente.",
        'sha256' : "2507c795af00411e4531856ac3ff6f8e1230ed2c7bce0ce625fd9253b6c1616a",
        'md5' : "72926471d5bc7796431cbd8a46d26376"
    }
    
    dict5 = {
        'sentence' : "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o Instituto de Especialização em Ciências Administrativas e Tecnológicas (IECAT) foi criado em 1981",
        'sha256' : "9203bb285e2ba6b59017b82e43a54785a068ec72c41216f2f0b40fd727630c4e",
        'md5' : "736062a2b1aa98f8d841e176c2ed690a"
    }
    
    dict6 = {
        'sentence' : "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI em 2002.",
        'sha256' : "44841459e6b3f2d8ef183983e9d6c196824d5fe912864c5e92ec1c205b66c3a6",
        'md5' : "16bf5ee5409000f2700f1376b88d9f16"
    }
    
    dict7 = {
        'sentence' : "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
        'sha256' : "da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6",
        'md5' : "2e20bfbece6fdc62de4c4bb80a77ba1f"
    }
    
    dict8 = {
        'sentence' : "Em 2016 foi realizada a primeira edição do Congresso de Inovação - Megatendências 2050.",
        'sha256' : "611b412b62e3111769de22a808a266e1a80bde3b3b11d2fc5c859726d1ffb401",
        'md5' : "3217881f995a0c50201061505e4060aa"
    }
    
    dict9 = {
        'sentence' : "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 60 mil profissionais altamente qualificados para o setor empresarial, entre administradores, engenheiros e cientistas da computação.",
        'sha256' : "b86e3f2658ed39384b6812464413ab931309e1cfcc5104c724b855300a1f13cb",
        'md5' : "82c1616d6130272adb3b4048d58296e0"
    }
    
    dict10 = {
        'sentence' : "Em 1999 iniciam-se as atividades da Faculdade de Informática - FCI, como o curso de Ciência da Computação.",
        'sha256' : "c64dca8c81cc379cc4618056e2801201882cbf53d8786dd4108c7aa9775bfa91",
        'md5' : "1013976891617a120472e629ccdf3858"
    }

    list_of_dictionary = [dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10]
    
    return list_of_dictionary

def generateHashes(dict):
    # Gera a Hash SHA256 para a frase no dicionário
    dict['generated_sha256'] = hl.sha256(dict['sentence'].encode('utf-8')).hexdigest()
    # Gera a Hash MD5 para a frase no dicionário
    dict['generated_md5'] = hl.md5(dict['sentence'].encode('utf-8')).hexdigest()
    
    # Verifica se as hashes geradas estão de acordo com as hashes recebidas
    if(dict['generated_sha256'] == dict['sha256'] and dict['generated_md5'] == dict['md5']):
        dict['result'] = 'SHA256 e MD5 corretos'
        
    elif(dict['generated_sha256'] == dict['sha256']):
        dict['result'] = 'Apenas SHA256 correto'
        
    elif(dict['generated_md5'] == dict['md5']):
        dict['result'] = 'Apenas MD5 correto'
        
    else:
        dict['result'] = 'Nenhuma Hash correta'
        
def createOutputDir():
    if not os.path.exists("output"):
        os.mkdir("output")
    
        
def generateExcel(dict_list):
    df = pd.DataFrame()
    
    sentences = []
    sha256 = []
    md5 = []
    generated_sha256 = []
    generated_md5 = []
    result = []
    
    # Adiciona o conteúdo as listas
    for i in range(len(dict_list)):
        sentences.append(dict_list[i]['sentence'])
        sha256.append(dict_list[i]['sha256'])
        md5.append(dict_list[i]['md5'])
        generated_sha256.append(dict_list[i]['generated_sha256'])
        generated_md5.append(dict_list[i]['generated_md5'])
        result.append(dict_list[i]['result'])
        
    # Cria as colunas com as listas
    df['Frase'] = sentences
    df['Hash SHA256'] = sha256
    df['Hash MD5'] = md5
    df['Hash SHA256 Geada'] = generated_sha256
    df['Hash MD5 Gerada'] = generated_md5
    df['Resultado'] = result
    
        
    createOutputDir()
        
    df.to_excel(excel_writer="output/HashValidationResult.xlsx", index=False)
    

def main():
    dict_list = getSentences()
    
    for i in range(len(dict_list)):
        generateHashes(dict_list[i])
            
    generateExcel(dict_list)
    
main()