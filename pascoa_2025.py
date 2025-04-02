import pandas as pd
import streamlit as st






df = pd.read_csv("pascoa_2025.csv")  # Tenta carregar o arquivo existente



tmh = ""
    
    
def tamanho(sabores):
    
    global df 
    tmh = ""  
    if sabores == "Maracuja_chocolate":
        tamanho = st.selectbox(
        "Qual tamanho?",
        ("375g", "160g"))
        
        if tamanho == "375g":
            tmh = "Quantidade_grande"
            add = 1
            valor = 92
            
        else:
            tmh = "Quantidade_pequeno"
            add = 1
            valor = 45
            
            
            
    elif sabores == "Brulee":
        tamanho = st.selectbox(
        "Qual tamanho?",
        ("370g", "165g"))
        
        if tamanho == "370g":
            tmh = "Quantidade_grande"
            add = 1
            valor = 92
            
        else:
            tmh = "Quantidade_pequeno"
            add = 1
            valor = 45
            

    elif sabores == "Brownie_caramelo":
        tamanho = st.selectbox(
        "Qual tamanho?",
        ("360g", "160g"))
        
        if tamanho == "360g":
            tmh = "Quantidade_grande"
            add = 1
            valor = 88

            
        else:
            tmh = "Quantidade_pequeno"
            add = 1
            valor = 42


        
        
    elif sabores == "Cookie_brigadeiro":
        tamanho = st.selectbox(
        "Qual tamanho?",
        ("360g", "160g"))
        
        if tamanho == "360g":
            tmh = "Quantidade_grande"
            add = 1
            valor = 92

        else:
            tmh = "Quantidade_pequeno"
            add = 1
            valor = 45



        
    elif sabores == "Ninho_nutella":
        tmh = "Quantidade_grande"
        add = 1
        valor = 120




    elif sabores == "Pistache_caramelo":
        tamanho = st.selectbox(
        "Qual tamanho?",
        ("590g", "160g"))
        
        if tamanho == "590g":
            tmh = "Quantidade_grande"
            add = 1
            valor = 135

        else:
            tmh = "Quantidade_pequeno"
            add = 1
            valor = 50

        
    elif sabores == "Trio_ovos":
        tmh = "Quantidade_grande"
        add = 1
        valor = 130

        
    elif sabores == "Cupcakes":
        tamanho = st.selectbox(
        "Qual tamanho?",
        ("Caixa com 1", "Caixa com 2", "caixa com 4"))
        
        if tamanho == "Caixa com 1":
            tmh = "Quantidade_grande"
            add = 1
            valor = 15
            

        elif tamanho == "Caixa com 2":
            tmh = "Quantidade_grande"
            add = 2
            valor = 32

            
        else:
            tmh = "Quantidade_grande"
            add = 4
            valor = 60

            
    if st.button("Adicionar", type="primary"):
        df.loc[df["Sabores"] == sabores, tmh] += add
        df.loc[df["Sabores"] == sabores, "Valor_arrecadado"] += valor
        df.to_csv("pascoa_2025.csv", index=False)

    st.divider()



        
    if st.button("Remover", type="tertiary"):
        df.loc[df["Sabores"] == sabores, tmh] -= add
        df.loc[df["Sabores"] == sabores, "Valor_arrecadado"] -= valor
        df.to_csv("pascoa_2025.csv", index=False)



            
        
def escolha():
    sabor = st.selectbox(
    "Qual sabor você quer adicionar?",
    ("Maracuja e Chocolate", "Bruleé", "Brownie e Caramelo", "Cookie e Brigadeiro", "Ninho e Nutella", "Pistache e Caramelo","Trio de Ovos", "Cupcakes"),
    )
    if sabor == "Maracuja e Chocolate":
        x = "Maracuja_chocolate"
        tamanho(x)


    elif sabor == "Bruleé":
        x = "Brulee"
        tamanho(x)


    elif sabor == "Brownie e Caramelo":
        x = "Brownie_caramelo"
        tamanho(x)


    elif sabor == "Cookie e Brigadeiro":
        x = "Cookie_brigadeiro"
        tamanho(x)


    elif sabor == "Ninho e Nutella":
        x = "Ninho_nutella"
        tamanho(x)


    elif sabor == "Pistache e Caramelo":
        x = "Pistache_caramelo"
        tamanho(x)


    elif sabor == "Trio de Ovos":
        x = "Trio_ovos"
        tamanho(x)


    elif sabor == "Cupcakes":
        x = "Cupcakes"
        tamanho(x)
    

escolha()

st.dataframe(df)

st.metric(label="Valor Total", value= f"R$ {df["Valor_arrecadado"].sum()}" , border= True)
