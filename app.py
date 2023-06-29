import streamlit as st
import requests
import json

def main():
    st.title("API Frontend")
    url_API =st.text_input("Inserisci url")
    RdSpend = st.text_input("Inserisci Rd")
    Administration = st.text_input("Inserisci Admin")
    Marketing = st.text_input("Inserisci Mark")

  
    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?Rdspend={RdSpend}&Administration={Administration}&Marketing={Marketing}"
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
                                                   "Rdspend":RdSpend,
                                                   "Administration":Administration,
                                                   "Marketing":Marketing,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result['result']}")

if __name__ == '__main__':
    main()