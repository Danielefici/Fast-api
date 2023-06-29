import streamlit as st
import requests
import json

def main():
    st.title("API Frontend")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8001/predict")
    rdSpend = st.number_input("Inserisci rd",0, 1000000, 5)
    administration = st.number_input("Inserisci Admin", 0, 1000000, 5)
    marketing = st.number_input("Inserisci Mark", 0, 1000000, 5)

    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?RdSpend={rdSpend}&Administration={administration}&Marketing={marketing}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result['result']}")

    
    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "Rdspend":rdSpend,
                                                   "Administration":administration,
                                                   "Marketing":marketing,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result['result']}")

if __name__ == '__main__':
    main()