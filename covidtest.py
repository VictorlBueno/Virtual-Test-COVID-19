print('Choose a language - Escolha um idioma')
idioma = input('English or/ou Português? ')

while True:
    if 'En' in idioma or 'en' in idioma or 'ng' in idioma or 'gl' in idioma or 'li' in idioma or 'is' in idioma or 'sh' in idioma or 'EN' in idioma or 'NG' in idioma or 'GL' in idioma or 'LI' in idioma or 'IS' in idioma or 'SH' in idioma:
        idioma = 'en'
        break
    
    elif 'Po' in idioma or 'po' in idioma or 'or' in idioma or 'rt' in idioma or 'tu' in idioma or 'ug' in idioma or 'gu' in idioma or 'ue' in idioma or 'uê' in idioma or 'es' in idioma or 'ês' in idioma or 'PO' in idioma or 'OR' in idioma or 'RT' in idioma or 'TU' in idioma or 'UG' in idioma or 'GU' in idioma or 'UE' in idioma or 'UÊ' in idioma or 'ES' in idioma or 'Ês' in idioma or 'pt' in idioma or 'PT' in idioma or 'Pt' in idioma:
        idioma = 'pt'
        break

    else:
        print('Opção inválida - Invalid option')
        print('Choose a language - Escolha um idioma')
        idioma = input('English or/ou Português? ')

if idioma == 'pt':
    print('Teste Iniciado--------------------------------')
    print('Descubra se você está com COVID')
    print('Referência do teste: World Health Organization')
    print('----------------------------------------------')

    print('Responda com "Sim" ou "Não" de acordo com os sintomas presentes durante as últimas 2 semanas')
    resp1 = input('Você apresenta tosse? ') ###
    resp2 = input('Você está com dificuldade de respirar? ') ####
    resp3 = input('Você sente calafrios ou tremores? ') ##
    resp4 = input('Você sente dor muscular? ') #
    resp5 = input('Você sente dor de garganta? ') #
    resp6 = input('Percebeu perda do oufato ou paladar? ') ####
    resp7 = input('Teve Náuseas, vomitou ou teve diarréia? ') #
    resp8 = input('Sentiu dor de cabeça? ') #
    resp9 = input('Sensação de febre ou febre medida maior ou igual a 37,8? ') ###
    resp10 = input('Alguém com quem tenha tido contacto teve ou está a ter COVID? ') ####
    pts = 0

    if 's' in resp1 or 'S' in resp1 or 'i' in resp1 or 'm' in resp1:
        pts = pts + 3
    if 's' in resp2 or 'S' in resp2 or 'i' in resp2 or 'm' in resp2:
        pts = pts + 4
    if 's' in resp3 or 'S' in resp3 or 'i' in resp3 or 'm' in resp3:
        pts = pts + 2
    if 's' in resp4 or 'S' in resp4 or 'i' in resp4 or 'm' in resp4:
        pts = pts + 1
    if 's' in resp5 or 'S' in resp5 or 'i' in resp5 or 'm' in resp5:
        pts = pts + 1
    if 's' in resp6 or 'S' in resp6 or 'i' in resp6 or 'm' in resp6:
        pts = pts + 4
    if 's' in resp7 or 'S' in resp7 or 'i' in resp7 or 'm' in resp7:
        pts = pts + 1
    if 's' in resp8 or 'S' in resp8 or 'i' in resp8 or 'm' in resp8:
        pts = pts + 1
    if 's' in resp9 or 'S' in resp9 or 'i' in resp9 or 'm' in resp9:
        pts = pts + 3
    if 's' in resp10 or 'S' in resp10 or 'i' in resp10 or 'm' in resp10:
        pts = pts + 4

    if pts >= 18:
        result = 'Sintomas fortes. Vista uma máscara e procure um médico imediatamente.'
    if pts >= 8 and pts <= 17:
        result = 'Sintomas existentes. Vista uma máscara e procure um médico.'
    if pts >= 4 and pts <= 7:
        result = 'Sintomas leves de COVID ou outra doença. Vista uma máscara e mantenha a distância das pessoas, casos persistir, procure um médico.'
    if pts <= 3:
        result = 'Não há sinal de COVID. Vista uma máscara e mantenha a distância das pessoas, casos dúvidas persistir, procure um médico.'

    print(f'RESULTADO-------------------------------------------------------------------------------------------------')
    print(f'{result}')
    print(f'AVISO-----------------------------------------------------------------------------------------------------')
    print(f'Este teste é apenas uma Anamnese virtual, não tome nenhuma decisão sem antes consultar um médico!')

elif idioma == 'en':
    print('Test Started-----------------------------')
    print('Find out if you have COVID')
    print('Test reference: World Health Organization')
    print('-----------------------------------------')

    print('Answer with "Yes" or "No" according to the symptoms present during the past 2 weeks')
    resp1 = input('Do you have a cough? ') ###
    resp2 = input('Are you having difficulty breathing? ') ####
    resp3 = input('Do you feel chills or shakes? ') ##
    resp4 = input('Do you feel muscle pain? ') #
    resp5 = input('Do you have a sore throat? ') #
    resp6 = input('Have you noticed a loss of taste or smell? ') ####
    resp7 = input('Have you had nausea, vomiting, or diarrhea? ') #
    resp8 = input('Did you feel a headache? ') #
    resp9 = input('Fever sensation or fever measured greater than or equal to 37.8? ') ###
    resp10 = input('Has anyone with whom you have had contact had or is having COVID? ') ####
    pts = 0

    if 'y' in resp1 or 'Y' in resp1 or 'e' in resp1 or 's' in resp1:
        pts = pts + 3
    if 'y' in resp2 or 'Y' in resp2 or 'e' in resp2 or 's' in resp2:
        pts = pts + 4
    if 'y' in resp3 or 'Y' in resp3 or 'e' in resp3 or 's' in resp3:
        pts = pts + 2
    if 'y' in resp4 or 'Y' in resp4 or 'e' in resp4 or 's' in resp4:
        pts = pts + 1
    if 'y' in resp5 or 'Y' in resp5 or 'e' in resp5 or 's' in resp5:
        pts = pts + 1
    if 'y' in resp6 or 'Y' in resp6 or 'e' in resp6 or 's' in resp6:
        pts = pts + 4
    if 'y' in resp7 or 'Y' in resp7 or 'e' in resp7 or 's' in resp7:
        pts = pts + 1
    if 'y' in resp8 or 'Y' in resp8 or 'e' in resp8 or 's' in resp8:
        pts = pts + 1
    if 'y' in resp9 or 'Y' in resp9 or 'e' in resp9 or 's' in resp9:
        pts = pts + 3
    if 'y' in resp10 or 'Y' in resp10 or 'e' in resp10 or 's' in resp10:
        pts = pts + 4

    if pts >= 18:
        result = 'Strong symptoms. Wear a mask and seek medical attention immediately.'
    if pts >= 8 and pts <= 17:
        result = 'Existing symptoms. Wear a mask and consult a doctor.'
    if pts >= 4 and pts <= 7:
        result = 'Mild symptoms of COVID or other illness. Wear a mask and keep away from others; if this persists, seek medical attention.'
    if pts <= 3:
        result = 'No sign of COVID. Wear a mask and keep a distance from people, if doubts persist, seek medical attention.'

    print(f'RESULT---------------------------------------------------------------------------------------------')
    print(f'{result}')
    print(f'WARNING--------------------------------------------------------------------------------------------')
    print(f'This test is only a virtual anamnesis, do not make any decision without first consulting a doctor!')

else:
    print('Erro - Error')
