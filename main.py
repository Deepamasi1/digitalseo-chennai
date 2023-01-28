import streamlit as st
import textrazor
import re

def calculator():
    st.title("Get Top Entities from Target Articles")

    limit = st.text_input("How many Entities do you expect - Min 5, Max 15:")
    url = st.text_input("Website URL:")
    doclink = st.text_input("Curated Document:")
    textinput = st.text_area("Text Snippet")

    operations = st.selectbox("Select operation", ["Entities from URL", "Entities from Document", "Entities from Text"])

    if st.button("Entities from URL"):
        if operations == "Entities from URL":
            result = getentityfromurl(url,limit)
            st.success(f"The top entities from {url} :  {result}")
        elif operations == "Entities from Document":
            result = getentityfromcuration(doclink)
            st.success(f"The top entities from {doclink} :  {result}")
        elif operations == "Entities from Text":
            result = getentityfromgiventext(textinput)
            st.success(f"The top entities from {textinput} :  {result}")
        #else:
        #    if num2==0:
        #        st.error("Cannot divide by zero")
        #    else:
        #        result = num1 / num2
        #        st.success(f"The result of {num1} / {num2} is {result}")

def getentityfromcuration(doclink):
    return "B"

def getentityfromgiventext(textsnippet):
    return "C"

def getentityfromurl(url, limit):
    textrazor.api_key = "f511eff44a834d7483864b36216e94c4dd40b69d9d8924d7748c5be6"
    client = textrazor.TextRazor(extractors=["entities", "topics"])
    response = client.analyze_url(url)

    entities = list(response.entities())
    entities.sort(key=lambda x: x.confidence_score, reverse=True)
    seen = set()
    entityFreeze = ''
    counter = 0
    for entity in entities:
        if counter < limit:
            if entity.id not in seen:
                # spllettersremoved = re.sub('[^a-zA-Z0-9.]|(?<!\d)\.|\.(?!\d)', '', entity.id)
                pattern = re.compile(r'([+-]?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?|[^\W_])|.', re.DOTALL)
                spllettersremoved = pattern.sub(lambda x: x.group(1) or " ", entity.id)
                entityFreeze = spllettersremoved +  "," + entityFreeze
                seen.add(entity.id)
                counter = counter + 1
    print(entityFreeze)
    return entityFreeze

if __name__=="__main__":
    calculator()
