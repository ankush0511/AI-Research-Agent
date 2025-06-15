import requests

def get_embedding(prompt,model='nomic-embed-text'):
     url="http://localhost:11434/api/embeddings"
     headers={"Content-Type":"application/json"}
     data={"prompt":prompt,"model":model}
     response=requests.post(url,headers=headers,json=data)

     if response.status_code==200:
          return response.json().get("embedding",[])
     else:
          raise Exception(
               f"error fet embed,{response.status_code},{response.text}"
          )
     

if __name__=="__main__" :
    sam_p="The sky is blue because of Rayleigh scattering"
    try:
        embedding=get_embedding(sam_p)
        print("emd dim",len(embedding))
        print(embedding)
    except Exception as e:
        print("failed to get embedding")